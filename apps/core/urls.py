from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('toggle-dark-mode/', views.toggle_dark_mode, name='toggle_dark_mode'),
]
