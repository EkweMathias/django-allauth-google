from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("signup/", views.signup_user, name='signup'),
    path("logout/", views.logout_user, name='logout'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)