from django.urls import path
from django.conf.urls import url

from .views import ( PollListCreate,PollRetriveUpdateDestroy)


urlpatterns = [
    path('', PollListCreate.as_view(), name='polls-list'),
    path('<int:pk>/', PollRetriveUpdateDestroy.as_view(), name='pool-details'),

]
