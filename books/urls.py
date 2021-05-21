from . import views
from django.urls import path

urlpatterns =[
    path('/',views.BookListView.as_view(),name='book.all'),
    path('/index',views.index,name='book.all.index'),
    path('/<int:pk>',views.BookDetailView.as_view(),name='book.show'),
    path('/book/<int:id>',views.show,name='book.show.index'),
    path('/<int:id>/review',views.review,name='book.review')
]