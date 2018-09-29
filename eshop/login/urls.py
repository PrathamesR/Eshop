from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.log, name='login'),
    path('index/', views.index, name='index'),
    path('logout/',views.out, name='logout'),
    path('itempage/<int:item_id>', views.itempage, name='itempage'),
    path('type/<int:item_type>', views.typee, name='type'),
    path('confirm/<int:item_id>', views.confirm, name='confirmation'),
    path('signup/', views.UserFormView.as_view(), name='signup'),
    path('profile/', views.profile, name='profile')
]
