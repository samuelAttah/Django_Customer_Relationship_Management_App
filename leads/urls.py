from django.urls import path

from . import views

app_name = "leads"

urlpatterns = [
    path('', views.lead_list, name='lead-list'),
    path('<int:pk>/', views.lead_detail, name='lead-detail'),
    path('<int:pk>/update/', views.lead_update_view, name='lead-update'),
    path('<int:pk>/delete/', views.lead_delete_view, name='lead-delete'),
    path('create/', views.lead_create_view, name='lead-create')

]
