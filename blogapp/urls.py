from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="index"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('addblog/<int:id>',views.addblog,name="addblog"),
    path('signout',views.signout,name="signout"),
    path('showblog/<g_email>',views.showblog,name="showblog"),
    path('delete/<id>',views.deleteblog,name="deleteblog"),
    path('updatepr/<int:id>',views.updatepr,name="updatepr"),
    path('verify/<token>',views.verify_email,name="verifyemail"),
]
