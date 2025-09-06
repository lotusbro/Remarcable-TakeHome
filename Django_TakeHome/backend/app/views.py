from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Tag
from .serializers import ProductSerializer, CategorySerializer, TagSerializer
from django.shortcuts import render 

@api_view(["GET"])
def products_api(request):
    description= request.GET.get("search", "").strip()
    category_id= request.GET.get("category_id")   
    tag_ids= request.GET.get("tag_id")           

    combine_search = Product.objects.all() 
    if description:
        combine_search = combine_search.filter(description__contains=description)              
    if category_id:
        combine_search = combine_search.filter(category_id=category_id)      
    if tag_ids:
        combine_search = combine_search.filter(tags__id__in=tag_ids).distinct()   

    return Response(ProductSerializer(combine_search, many=True).data)

@api_view(["GET"])
def categories_api(request):
    serializer = CategorySerializer(Category.objects.order_by("name"), many=True)
    return Response(serializer.data)

@api_view(["GET"])
def tags_api(request):
    serializer = TagSerializer(Tag.objects.order_by("name"), many=True)
    return Response(serializer.data) 

def searchfilter_page(request):
    return render(request, "searchfilter.html")
