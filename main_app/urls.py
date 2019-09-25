from django.urls import path
from . import views


urlpatterns = [
    path('', include('main_app.urls')),

]