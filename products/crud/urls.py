from django.urls import path
from . import views
from .views import *

app_name='crud'

urlpatterns=[
    # path('',views.home,name='home'),
    path('',HomeView.as_view(),name='home'),
    path('detail/product/<int:pk>',ProductView.as_view(),name='product'),
    # path('add',views.add,name='add'),
    path('add',AddView.as_view(),name='add'),
    # path('delete/<int:id>',views.delete,name='delete'),
    path('delete/<int:id>',DeleteView.as_view(),name='delete'),
    # path('update/<int:id>',views.update,name='update'),
    path('update/<int:id>',UpdateView.as_view(),name='update'),
]