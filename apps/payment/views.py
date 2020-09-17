from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.generic import TemplateView

from apps.payment.models import PaymentLog
from apps.payment.stripe import get_token, get_payment_charge
from apps.subscription.views import start_subscription


class ChargeView(TemplateView):
    template_name = 'payment/charge.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLISHABLE_KEY
        context['amount'] = 100
        context['currency'] = 'tl'
        return context

    def post(self, request):
        name = request.POST.get('name')
        card_number = request.POST.get('cardnumber')
        exp_month = int(request.POST.get('exp-date').split('/')[0])
        exp_year = int(request.POST.get('exp-date').split('/')[1])
        cvc = request.POST.get('cvc')
        card = {
            "name": name,
            "number": card_number,
            "exp_month": exp_month,
            "exp_year": exp_year,
            "cvc": cvc
        }
        token = get_token(card)
        charge = get_payment_charge(amount=100, currency="usd", description="test", token=token.stripe_id)
        if charge.paid:
            log_payment(user=request.user, data=charge)
            start_subscription(request.user)
        return HttpResponseRedirect('/')


def log_payment(user, data):
    PaymentLog.objects.create(user=user, data=data)
