from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from bookshelf.views import add_book, edit_book, delete_book


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
