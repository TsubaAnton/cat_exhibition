from .apps import CatConfig
from django.urls import path
from .views import (CatListAPIView, CatCreateAPIView, CatRetrieveAPIView, CatUpdateAPIView, CatDestroyAPIView,
                    BreedListAPIView, BreedCreateAPIView, RatingCreateAPIView)

app_name = CatConfig.name

urlpatterns = [
    path('', CatListAPIView.as_view(), name='cat_list'),
    path('cat/create/', CatCreateAPIView.as_view(), name='cat_create'),
    path('cat/<int:pk>/', CatRetrieveAPIView.as_view(), name='cat_retrieve'),
    path('cat/update/<int:pk>/', CatUpdateAPIView.as_view(), name='cat_update'),
    path('cat/destroy/<int:pk>/', CatDestroyAPIView.as_view(), name='cat_destroy'),

    path('breed/', BreedListAPIView.as_view(), name='breed_list'),
    path('breed/create/', BreedCreateAPIView.as_view(), name='breed_create'),

    path('rating/create/', RatingCreateAPIView.as_view(), name='rating_create'),
]
