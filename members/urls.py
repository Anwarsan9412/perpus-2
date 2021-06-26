from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('password_success', views.password_success, name='password-success'),
    # path('profile/', views.profile, name='members-profile'),
    path('registration/',HomeView.as_view(), name='members-home'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
