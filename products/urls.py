from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = [
    path('products/', views.ProductView, name='products'),
]

urlpatterns = format_suffix_patterns(urlpatterns)