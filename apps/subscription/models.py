from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings


class Subscription(models.Model):
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    subscriber = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name='subscriptions', verbose_name=_('subscriber'))
    start_date = models.DateTimeField(auto_created=True, verbose_name=_('start date'))
    end_date = models.DateTimeField(verbose_name=_('end date'))

    class Meta:
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')

    def __str__(self):
        return f'{self.subscriber}'
