from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', views.SignUp.as_view(), name = 'signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name = 'home'),
    path('create/', views.create, name = 'create'),
    path('viewmypost/', views.viewmy, name = 'viewMy'),
    path('delete/<post_id>', views.delete_post, name='delete'),
    path('like/<post_id>', views.like_post, name='like'),
    path('comment/<post_id>', views.comment, name='comment'),
]