from django.urls import path
from django.conf.urls import url

from .views import ( PollListCreate,PollRetriveUpdateDestroy,ChoiceListCreate)


urlpatterns = [
    path('', PollListCreate.as_view(), name='polls-list'),
    path('choice/', ChoiceListCreate.as_view(), name='choice-list'),
    path('<int:pk>/', PollRetriveUpdateDestroy.as_view(), name='pool-details'),

]
