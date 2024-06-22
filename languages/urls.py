from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from languages import views
urlpatterns = [
    path('lang/', views.language_list)

]

urlpatterns = format_suffix_patterns(urlpatterns)