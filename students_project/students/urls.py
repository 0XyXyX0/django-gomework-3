from django.urls import path
from .views import students_page_view, main_page_view


urlpatterns = [
    path('students/', students_page_view),
    path('main/', main_page_view)
]