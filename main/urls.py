from django.urls import path
from . import views

urlpatterns = [
    path('',views.lobby ),
    path('room/',views.room ),
    path('get_token/',views.getToken ),
    path('create_user/',views.createUser ),
    path('get_user/',views.getUser ),
    path('del_user/',views.deleteUser ),

]