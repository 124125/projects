from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="books"),
    path('maths/',views.maths,name="Mathsbooks"),
    path('physics/',views.physics,name="physicsbooks"),
    path('English/',views.english,name="englishbooks"),
    path('BE/',views.be,name="bebooks"),
    path('BME/',views.bme,name="bmebooks"),
    path('Bme(w.)/',views.bmew,name="bmewbooks"),
    path('Bc(w.)/',views.ecw,name="ecwbooks"),
    path('Be(w.)/',views.bew,name="bewbooks")
]   
