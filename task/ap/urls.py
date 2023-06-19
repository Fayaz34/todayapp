from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.add, name='add'),
    path('delete/<int:taskid>/',views.Delete, name='delete'),
    path('update/<int:taskid>/',views.Update, name='update'),
]
