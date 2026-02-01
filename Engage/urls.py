from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from dashboard import views as dash_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/', dash_views.register, name = 'register'),
    path('signin/', auth_views.LoginView.as_view(template_name = "dashboard/signin.html"), name = 'signin'),
    # path('signout/', auth_views.LogoutView.as_view(template_name = "dashboard/signout.html"), name = 'signout'),
    path('signout/', auth_views.LogoutView.as_view(next_page='home'), name='signout'),

    path('profile/', dash_views.profile, name = 'profile'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    
    path('accounts/', include('allauth.urls')),
    # path('<std:username>/', dash_views.profile, name = 'user_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
