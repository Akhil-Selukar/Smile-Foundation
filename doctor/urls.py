from django.urls import path
from doctor import views

app_name = 'doctor'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.dr_login,name='login'),
]
