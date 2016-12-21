from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Picture


class PicturePlugin(CMSPluginBase):
    model = Picture
    name = _("Picture")
    render_template = "cms/plugins/picture.html"
    module = "Basis"
    text_enabled = True

    def render(self, context, instance, placeholder):
        if instance.url:
            link = instance.url
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'picture': instance,
            'link': link,
            'placeholder': placeholder
        })
        return context

    def icon_src(self, instance):
        # TODO - possibly use 'instance' and provide a thumbnail image
        return settings.STATIC_URL + u"cms/img/icons/plugins/image.png"

plugin_pool.register_plugin(PicturePlugin)
