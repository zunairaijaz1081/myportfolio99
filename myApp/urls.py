# from django.contrib import admin
# from django.urls import path
# from myApp import views

# urlpatterns = [
#      path('', views.index , name='about'),
#      path('resume/', views.resume , name='resume'),
#      path('portfolio/', views.portfolio , name='portfolio'),
#      path('blog/', views.blog, name='blog'),
#      path('contact/', views.contact, name='contact'),


# ]
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.index, name='about'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
