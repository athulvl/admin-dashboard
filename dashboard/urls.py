from django.urls import URLPattern,path

from . import views

urlpatterns = [
    path('login', views.login),
    path('login_user', views.login_user),
    path('logout-user', views.logout_user,name="logout"),

    path('', views.index,name='dashboard'),
    path('products', views.products,name='products'),
]