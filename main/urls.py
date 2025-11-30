from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('documents/', views.documents, name='documents'),
    path('documents/detail/', views.document_detail, name='document_detail'),
    path('documents/edit/', views.document_edit, name='document_edit'),
    path('settings/', views.settings_view, name='settings'),

    # Legacy support
    path('index/', views.index, name='index'),

    # API endpoints
    path('api/hello', views.api_hello, name='api_hello'),
    path('api/status', views.api_status, name='api_status'),
]
