from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('cobrancas/', views.cobrancas, name='cobrancas'),
    path('notificacao/', views.notificacao, name='notificacao'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)