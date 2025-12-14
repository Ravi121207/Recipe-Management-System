"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from home.views import home
from home.views import*
from vege.views import *
from accounts.views import*
from counter.views import*
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static



from counter import views  # make sure this is correct

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graph/", views.graph, name="graph"),
    path("front/", views.front, name="front"),
    path("home_page/", views.home_page, name="home_page"),
    path("dashboard_page/", views.dashboard_page, name="dashboard_page"),
    path("register_page/", views.register_page, name="register_page"),
    path("login_page/", views.login_page, name="login_page"),
    path("video_feed/", views.video_feed, name="video_feed"),
    path('logout/',views.logout_view,name='logout'),
    
    path('receipes/',receipes,name="receipes"),
    path('delete-receipe/<id>/',delete_receipe,name="delete_receipe"),
    path('update-receipe/<id>/',update_receipe,name="update_receipe"),
    # path('logins/',logins,name="logins"),
    # path('logins/',logins, name='logins'),
    path('forgot/',forgot,name="forgot"),
    path('sign/',sign,name="sign"),
    
    # path('register/',register,name="register"),       
    # path('login/',login,name=login),
    
    path('login_view/',login_view,name="login_view"),
    path('register/',register,name="register"),
    path('logout_view/',logout_view,name="logout_view"),
 
    
]






# urlpatterns = [
#     # path('',home,name="home"),
#     path('receipes/',receipes,name="receipes"),
#     path('delete-receipe/<id>/',delete_receipe,name="delete_receipe"),
#     path('update-receipe/<id>/',update_receipe,name="update_receipe"),
#     # path('logins/',logins,name="logins"),
#     path('logins/',logins, name='logins'),
#     path('forgot/',forgot,name="forgot"),
#     path('sign/',sign,name="sign"),
    
#     path('about/',about,name="about"),
#     path('contact/',contact,name="contact"),
#     path('success-page/',success_page,name="success_page"),
#     path('ravi/', admin.site.urls),
#     path('login/',login_page,name="login_page"),
#     path('register/',register,name="register"),
    
#     path('register_page/',register_page,name="register_page"),
#     path('login_page/',login_page,name=login_page),
    
# ]

# from django.contrib import admin
# from django.urls import path
# from counter import views

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     # path('register_page/',views.register_page,name="register_page"),
#     # path('login_page/',views.login_page,name=login_page),
#     path("home_page/",views.home_page, name="home_page"),
#     # path('', views.home, name="home"),
#     path('register_page/',views.register_page, name="register_page"),
#     path('login_page/', views.login_page, name="login_page"),
#     path('dashboard_page/', views.dashboard_page, name="dashboard_page"),
#     path("video_feed/",views.video_feed, name="video_feed"),
# ]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()
