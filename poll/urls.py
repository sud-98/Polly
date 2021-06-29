from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='poll-home'),
    path('create/', views.create, name='poll-create'),
    path('vote/<poll_id>/', views.vote, name='poll-vote'),
    path('result/<poll_id>', views.result, name='poll-result'),
]
