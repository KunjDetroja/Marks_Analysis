from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('<int:marks_id>', views.detail,name='detail'),
    path('student/<int:pk>/update/', views.marksupdate, name='marksupdate'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.loginacc,name='login'),
    path('logout/', views.logoutacc,name='logout'),
]
