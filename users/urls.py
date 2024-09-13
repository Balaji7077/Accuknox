from django.urls import path
from .views import trigger_signal_view

urlpatterns = [
    path('trigger-signal_view/', trigger_signal_view, name='trigger-signal_view'),
]
