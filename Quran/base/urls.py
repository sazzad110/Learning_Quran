from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('dis/', views.home, name="home"),
    path('', views.index, name="index"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    
    #chapter url now started
    path('shururkotha/', views.shurur_kotha, name='shurur-kotha'),
    path('okkhor/', views.okkhor, name='okkhor'),
    path('makhraj/', views.makhraj, name='makhraj'),
    path('shobdo_chinno/', views.shobdo, name='shobdo'),
    path('kolkola/', views.kolkola, name='kolkola'),
    path('madd/', views.madd, name='madd'),
    path('gunnah/', views.gunnah, name='gunnah'),
    path('nunmim/', views.nunmim, name='nunmim'),
    path('other/', views.other, name='other'),
    path('quiz/', views.quiz, name='quiz'),

    #telawat test
    path('telawat_home/', views.telawat_home, name='telawat-home'),
    path('telawat_form/', views.telawat_form, name='telawat-form'),
    path('telawat_test/', views.telawat_test, name='telawat-test'),



]
