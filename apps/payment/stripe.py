import stripe

from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_token(card):
    try:
        token = stripe.Token.create(card=card)
        return token
    except Exception as e:
        print(e)


def get_payment_charge(amount, currency, description, token):
    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            description=description,
            source=token,
        )
        return charge
    except Exception as e:
        print(e)







def retrieve():
    charge = stripe.Charge.retrieve(
        "ch_1HRQD0KLofdEoWTnCAxPFbi8",
        api_key=stripe.api_key
    )
    charge.save()  # Uses the same API Key.


def get_payment_intent(amount, currency, email):
    return stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        payment_method_types=['card'],
        receipt_email=email,
    )
