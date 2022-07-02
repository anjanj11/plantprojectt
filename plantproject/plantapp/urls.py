from . import views
from django.urls import path
app_name='plantapp'
urlpatterns = [

    path('',views.index,name="index"),
    path('login',views.login,name='login'),
    path('reg/',views.reg,name='reg'),
    path('form/', views.form, name="form"),
    path('detail',views.detail,name="detail"),
    path('logout',views.logout,name="logout"),

]
