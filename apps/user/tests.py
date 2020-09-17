from django.contrib.admin import AdminSite
from django.test import TestCase, RequestFactory

from apps.user.admin import UserAdmin
from apps.user.models import User


REQUEST_FACTORY = RequestFactory()


class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create(username="leyla")
        cls.user2 = User.objects.create(username="mecnun")

        cls.site = AdminSite()
        cls.admin = UserAdmin(User, cls.site)

        cls.request = REQUEST_FACTORY.get('/admin')

    def test_crud_user(self):
        # create
        test_user = User.objects.create(username="test")

        # read
        self.assertEqual(self.user1.pk, self.user1.id)
        qs_user = User.objects.all().order_by('id')
        self.assertEqual(list(qs_user.values_list('username', flat=True)), ['leyla', 'mecnun', 'test'])

        # update
        self.user1.username = "çimen"
        self.user2.username = "hüsnü"
        self.user1.save()
        self.user2.save()

        qs_user = User.objects.all().order_by('id')
        self.assertEqual(list(qs_user.values_list('username', flat=True)), ['çimen', 'hüsnü', 'test'])

        # delete

        deleted = test_user.delete()
        self.assertEqual(
            deleted, (1, {'user.User': 1})
        )
        self.assertQuerysetEqual(list(User.objects.all()), ['<User: çimen>', '<User: hüsnü>'])

    def test_user_admin(self):
        self.assertEqual(str(self.admin), 'user.UserAdmin')

        self.assertEqual(list(self.admin.get_form(self.request).base_fields), ['password',
                                                                               'is_superuser',
                                                                               'groups',
                                                                               'user_permissions',
                                                                               'username',
                                                                               'first_name',
                                                                               'last_name',
                                                                               'email',
                                                                               'is_staff',
                                                                               'is_active',
                                                                               ])

        self.assertEqual(list(self.admin.get_fields(self.request)), ['password',
                                                                     'is_superuser',
                                                                     'groups',
                                                                     'user_permissions',
                                                                     'username',
                                                                     'first_name',
                                                                     'last_name',
                                                                     'email',
                                                                     'is_staff',
                                                                     'is_active',
                                                                     'last_login',
                                                                     'date_joined'
                                                                     ])
