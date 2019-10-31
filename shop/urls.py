from django.urls import path
from shop import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/', views.product_view, name='products'),
    path('grooming_tips/', views.grooming_tips_view, name='grooming_tips'),
    path('contact_us/', views.contact_us_view, name='contact_us'),
]