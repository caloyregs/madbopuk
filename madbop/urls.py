"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from contents import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('/', views.home, name='home'),
    path('admin/', admin.site.urls),    
    path('jukeboxes/', views.jukeboxes, name='jukeboxes'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('common-questions/', views.common_questions, name='common_questions'),
    path('community/', views.community, name='community'),
    path('terms-of-use/', views.terms_of_use, name='terms-of-use'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('artists/', views.artists, name='artists'),
    path('help/', views.help, name='help'),
    path('blog/', views.blog, name='blog'),
    path('the-team/', views.team, name='team'),
    path('video-moments/', views.video_moments, name='video-moments'),
    path('signed-pictures/', views.signed_pictures, name='signed-pictures'),
    path('redeemable-merchandise/', views.redeemable_merchandise, name='redeemable-merchandise')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
