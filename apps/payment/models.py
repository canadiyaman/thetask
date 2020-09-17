from django.utils.translation import gettext_lazy as _

from django.db import models
from django.conf import settings


class PaymentLog(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'))
    data = models.JSONField()

    class Meta:
        verbose_name = _('payment log')
        verbose_name_plural = _('payment logs')

    def __str__(self):
        return f'{self.user}'
