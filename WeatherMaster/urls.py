"""
URL configuration for WeatherMaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from weather import views
from weather.forms import LoginForm

urlpatterns = [
    path('', views.show_cities, name='index'),
    path('edit_city/<int:id>/', views.edit_city, name='edit_city'),
    path('delete_city/<int:id>/', views.delete_city),
    path('temp_records/<int:city_id>/', views.show_temp_records),
    path('edit_temp_record/<int:city_id>/<int:id>/', views.edit_temp_record, name='edit_temp_record'),
    path('delete_temp_record/<int:city_id>/<int:id>/', views.delete_temp_record),
    path('login/', LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
