from django.urls import path
from . import views
from .views import form

app_name='schoolapp'

urlpatterns = [
      path('',views.index,name='index'),
      path('register/',views.register,name='register'),
      path('login/',views.login,name='login'),
      path('application/',views.application,name='application'),
      path('form/',views.form,name='form'),
      path('logout/',views.logout,name='logout')
    ]