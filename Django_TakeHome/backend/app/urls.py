from django.urls import path
from .views import searchfilter_page,products_api, categories_api, tags_api

urlpatterns = [
    path("", searchfilter_page),
    path("api/products/", products_api),
    path("api/categories/", categories_api),
    path("api/tags/", tags_api),
]

