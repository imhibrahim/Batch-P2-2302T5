from django.urls import path
from .import views
urlpatterns = [
    path('',views.fatchproduct,name="index"),
    path('insertproduct',views.Insertproduct),
    path('delproduct/<id>',views.delproduct,name='delp'),
    path('edit/<id>',views.edit,name='edit'),
]
