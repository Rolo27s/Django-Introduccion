"""
URL configuration for EjIntro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Ejercicios.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('areatriangulo/', areatriangulo),              # areatriangulo/?base=4&altura=7
    path('arearectangulo/', arearectangulo),            # arearectangulo/?lado1=3&lado2=5
    path('areacirculo/', areacirculo),                  # areacirculo/?radio=2.24
    path('longitudtriangulo/', longitudtriangulo),      # longitudtriangulo/?lado1=2&lado2=3&lado3=4
    path('longitudrectangulo/', longitudrectangulo),    # longitudrectangulo/?lado1=3&lado2=5
    path('longitudcuadrado/', longitudcuadrado),        # longitudrectangulo/?lado1=3
    path('longitudcirculo/', longitudcirculo),          # longitudcirculo/?radio=31.24
    path('cantidadvocales/', cantidadvocales),          # cantidadvocales?palabra=Hola mundo
    path('minimo/', minimo),                            # minimo/?numeros=1,2,3,4,5,6,7,8
    path('posnegcero/', posnegcero),                    # posnegcero/?numero=4
]
