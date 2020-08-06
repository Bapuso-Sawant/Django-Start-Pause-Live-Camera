from django.conf.urls import url
from livecam import views

urlpatterns = [
    url('dashboard',views.dashboard),
    url('startcam',views.startcam),    
]
