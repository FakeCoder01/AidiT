from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="index_view"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('profile/', views.profile_view, name="profile_view"),
    path('signup/', views.signup_view, name="signup_view"),
    path('edit/<str:id>/', views.edit_and_save_photo, name="edit_and_save_photo"),
    path('dash/', views.dash_view, name="dash_view"),
    path('delete/<str:id>/', views.delete_photo, name="delete_photo"),
]
