from django.urls import path
from . import views

app_name = "tvseries"

urlpatterns = [
    path("<int:tv_id>",views.tv_detail,name= "tv_detail"),
]