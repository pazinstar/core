from django.urls import path

from .import views

urlpatterns = [
    path('', views.home_view, name='payments-home'),
    path('success/', views.success_view, name='payments-success'),   # only for the Coinbase charges approach
    path('cancel/', views.cancel_view, name='payments-cancel'),      # only for the Coinbase charges approach
    path('webhook/', views.coinbase_webhook),  # new
]