from django.contrib import admin
from django.urls import path

from publisher import views

urlpatterns = ([
                   path('admin/', admin.site.urls),
                   path('', views.publisher_list, name='publisher_list'),
                   path('new/', views.create_publisher, name='create_publisher'),
                   path('edit/<int:pk>/', views.update_publisher, name='update_publisher'),
                   path('delete/<int:pk>/', views.delete_publisher, name='delete_publisher'),
               ], 'publisher')
