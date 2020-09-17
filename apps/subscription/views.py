from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from apps.subscription.book_api import get_adapter
from apps.subscription.models import Subscription
from apps.subscription.serializers import BookListSerializer


class SubscriptionView(TemplateView):
    template_name = 'home.html'

    @method_decorator(login_required(login_url=reverse_lazy('user:login')))
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        try:
            subscription = Subscription.objects.get(subscriber=request.user, is_active=True)
            page = request.GET.get('page', 1)
            results = get_adapter().books(page)
            serializer = BookListSerializer(results, request)
            context['books'] = serializer.data
        except Subscription.DoesNotExist:
            subscription = None
        context['subscription'] = subscription
        return self.render_to_response(context)

    @method_decorator(login_required(login_url=reverse_lazy('user:login')))
    def post(self, request):
        try:
            subscription = Subscription.objects.get(subscriber=request.user, is_active=True)
            subscription.is_active = False
            subscription.save()
        except Subscription.DoesNotExist:
            print("user haven't any subscription")
        return HttpResponseRedirect(reverse_lazy('home'))


def start_subscription(subscriber):
    start_date = timezone.now()
    end_date = start_date + timedelta(days=30)
    Subscription.objects.create(
        subscriber=subscriber,
        start_date=start_date,
        end_date=end_date
    )
