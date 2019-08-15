from django.urls import path
from demoapp.views import HelloPageView
from django.conf.urls import url, include
urlpatterns = [
    # path(r'', HelloPageView, name='helloo')
    path('', HelloPageView.as_view(), name='hello')
]
