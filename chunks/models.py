# -*- coding: utf-8 -*-
from django.db import models
from django.utils import six
from django.utils.translation import ugettext_lazy as _


@six.python_2_unicode_compatible
class Chunk(models.Model):
    """
    A Chunk is a piece of content associated
    with a unique key that can be inserted into
    any template with the use of a special template
    tag
    """
    key = models.CharField(_('Key'), help_text=_("A unique name for this chunk of content"), blank=False, max_length=255, unique=True)
    content = models.TextField(_('Content'), blank=True)
    description = models.CharField(_('Description'), blank=True, max_length=64, help_text=_("Short Description"))

    class Meta:
        verbose_name = _('chunk')
        verbose_name_plural = _('chunks')

    def __six__(self):
        return "%s" % (self.key,)
