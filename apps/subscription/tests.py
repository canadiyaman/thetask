from datetime import timedelta

from django.contrib.admin import AdminSite
from django.test import TestCase, RequestFactory
from django.urls import reverse_lazy
from django.utils import timezone

from apps.subscription.admin import SubscriptionAdmin
from apps.subscription.models import Subscription
from apps.subscription.views import start_subscription, end_subscription
from apps.user.models import User


REQUEST_FACTORY = RequestFactory()


class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='test')

        cls.site = AdminSite()
        cls.admin = SubscriptionAdmin(Subscription, cls.site)

        cls.request = REQUEST_FACTORY.get('/admin')

    def test_crud_subscription(self):
        # create
        test_user = User.objects.create(username="test_user")

        start_date = timezone.now()
        end_date = start_date + timedelta(days=30)
        subscription = Subscription.objects.create(subscriber=test_user, start_date=timezone.now(), end_date=end_date)

        # read
        self.assertEqual(subscription.pk, subscription.id)
        qs_subscription = Subscription.objects.all().order_by('id')
        self.assertEqual(list(qs_subscription.values_list('subscriber__username', flat=True)), ['test_user'])

        # update
        subscription.is_active = False
        subscription.save()

        qs_subscription = Subscription.objects.all().order_by('id')
        self.assertEqual(list(qs_subscription.values_list('is_active', flat=True)), [False])

        # delete
        deleted = subscription.delete()
        self.assertEqual(
            deleted, (1, {'subscription.Subscription': 1})
        )
        self.assertQuerysetEqual(list(Subscription.objects.all()), [])

    def test_start_subscription_view(self):
        test_user = User.objects.create(username="test_user2")

        with self.assertRaises(Subscription.DoesNotExist):
            Subscription.objects.get(subscriber=test_user)

        start_subscription(test_user)

        self.assertTrue(Subscription.objects.get(subscriber=test_user))

    def test_end_subscription_view(self):
        test_user = User.objects.create(username="test_user2")

        start_subscription(test_user)
        Subscription.objects.filter(is_active=True).get(subscriber=test_user)

        end_subscription(test_user)

        with self.assertRaises(Subscription.DoesNotExist):
            Subscription.objects.filter(is_active=True).get(subscriber=test_user)

    def test_home_page(self):
        url = reverse_lazy('home')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/user/login/')

        test_user = User.objects.create(username="test_user2")
        test_user.set_password('12345')
        test_user.save()

        self.client.login(username='test_user2', password='12345')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_user_admin(self):
        self.assertEqual(str(self.admin), 'subscription.SubscriptionAdmin')

        self.assertEqual(list(self.admin.get_form(self.request).base_fields),
                         ['start_date', 'is_active', 'subscriber', 'end_date']
                         )

        self.assertEqual(list(self.admin.get_fields(self.request)),
                         ['start_date', 'is_active', 'subscriber', 'end_date'])
