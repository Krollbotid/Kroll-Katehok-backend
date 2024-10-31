from django.urls import path
from users import views
# from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
    # path('logout/', LogoutView.as_view(), name = 'logout'), # не работает с методом GET
]
