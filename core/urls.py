from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('contacto', views.frontpage, name='frontpage'),
    path('', views.base_pay, name="base_pay"),
    path('exito', views.success, name="success"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)