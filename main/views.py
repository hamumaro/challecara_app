from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings


def home(request):
    """
    Home page view
    """
    return render(request, 'home.html')


def documents(request):
    """
    Documents list view
    """
    return render(request, 'documents.html')


def document_detail(request):
    """
    Document detail view
    """
    return render(request, 'document_detail.html')


def document_edit(request):
    """
    Document edit/create view
    """
    return render(request, 'document_edit.html')


def settings_view(request):
    """
    Settings page view
    """
    return render(request, 'settings.html')

def syuukatu_view(request):
    """
    Syuukatu data view
    """
    return render(request, 'syuukatudata.html')


# Legacy view for backward compatibility
def index(request):
    """
    Legacy index page - redirects to home
    """
    return render(request, 'home.html')


def api_hello(request):
    """
    Hello API endpoint
    """
    return JsonResponse({
        'message': 'Hello from Challenge Cara App API!',
        'status': 'success',
        'version': settings.APP_VERSION
    })


def api_status(request):
    """
    Status API endpoint
    """
    return JsonResponse({
        'status': 'running',
        'app': settings.APP_NAME,
        'version': settings.APP_VERSION
    })
