# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_consultant, name='select_consultant'),  # Send Consultant page
    path('option_page/<int:consultant_id>/', views.option_page, name='option_page'),
    path('send_consultant/<int:consultant_id>/', views.selected_consultant, name='selected_consultant'),
    path('send_consultant_and_assistant/<int:consultant_id>/', views.selected_consultant_and_assistant, name='send_consultant_and_assistant'),
]
