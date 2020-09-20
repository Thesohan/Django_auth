from django.conf.urls import url
from .views import CreateUserAPIView,LoginView,UpdateRetriveUserAPIView
 
urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^login/$',LoginView.as_view()),
    url(r'update-retrive/',UpdateRetriveUserAPIView.as_view())
]