from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('allitem/', views.all_item,name='all_item'),
    path('search/', views.search,name='search'),
    path('searchurl/', views.searchurl,name='searchurl'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
