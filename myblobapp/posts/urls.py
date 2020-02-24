# from django.conf.urls import url
from django.urls import path
from . import views


# urlpatterns = [url(r'^$', views.index, name='index')]
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post_detail, name='post_detail')
]
