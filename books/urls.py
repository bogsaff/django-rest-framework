from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books import views
urlpatterns = [
    path('books/', views.BookList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)