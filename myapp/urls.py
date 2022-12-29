from django.urls  import path
from django.conf.urls import url
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.display_data, name='index'),
    path('search/', views.search, name='search'),
    path('update/<int:pk>',  views.update, name='update'),
    #path('crypto/', views.get_crypto_price, name="crypto"),
    
]