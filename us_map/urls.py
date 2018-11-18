
from django.conf.urls import  url
from .views import test_map
urlpatterns = [
    url(r'^test-map/$', test_map, name='test-map'),

]

