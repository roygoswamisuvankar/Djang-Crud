from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    #path('action_name',views.action_name, name='action_name'),
    path('new',views.new, name = 'new'),
    path('fibo',views.fibo, name = 'fibo'),
    path('show',views.show, name='show'),
    path('insertdata',views.insertdata, name='insertdata'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('edit/update',views.update, name='update'),
]