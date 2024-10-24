from django.urls import path
from deva import views
urlpatterns=[
    path('mama1',views.func1,name='p1'),
     path('mama2',views.func2,name='p1')
]