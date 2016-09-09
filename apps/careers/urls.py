from django.conf.urls import url

from .views import CareerDetailView, CareerListView

urlpatterns = [
    url(r'^$', CareerListView.as_view(), name='career_list'),
    url(r'^(?P<slug>[a-z-]+)/$', CareerDetailView.as_view(), name='career'),
]
