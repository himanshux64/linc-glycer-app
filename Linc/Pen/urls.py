from django.urls import path
from .import views



urlpatterns = [
    path('',views.info,name='info'),
    path('<int:pen_id>/',views.pen_details,name='pen_deatils'),
]
