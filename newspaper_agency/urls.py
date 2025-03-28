"""
URL configuration for newspaper_agency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf.urls.static import static

from newspapers.views import UserRegisterView

urlpatterns = [
  path("admin/", admin.site.urls),
  path("", include("newspapers.urls", namespace="newspapers")),
  path("accounts/login/", LoginView.as_view(), name="login"),
  path("accounts/logout/", LogoutView.as_view(next_page='login'), name='logout'),
  path("accounts/register/", UserRegisterView.as_view(), name='register'),
  path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
