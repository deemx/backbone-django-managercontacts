from django.conf.urls import url
from .view import index, action_index, action_store, action_show, action_edit


urlpatterns = (
    url(r'^$', index),
    url(r'^contacts$', action_index),
    url(r'^contacts/index$', action_index),
    url(r'^contacts/show/(?P<id>[0-9]+)$', action_show),
    url(r'^contacts/(?P<id>[0-9]+)$', action_edit),
)
