# pip install django
# pip install djangorestframework


from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from work_23.serializers import ProductSerializer
from work_23.models import Product
from rest_framework import (status, 
                            generics, )


# 23.02. Создать api метод для отображения информации об продуктах.
def api_products_1(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


# 23.03. Изменить апи метод с использованием декоратора.
@api_view(['GET'])
def api_products_2(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# 23.04. Написать метод по получению информации об одном продукте.
@api_view(['GET'])
def api_product(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


# 23.05. Изменить метод по получению продуктов. При POST запросе выполнять создание объекта.
@api_view(['GET', 'POST'])
def api_products_fin_ver(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 23.06. Изменить метод по получению конкретной записи. Добавить возможность изменять и удалять продукт.
@api_view(['GET', 'PUT', 'DELETE'])
def api_product_fin_ver(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# 23.07. Преобразовать код программы с использованием класса APIView.
class APIProducts1(APIView):
    @staticmethod
    def get(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIProductsDetail1(APIView):
    @staticmethod
    def get(request, product_id):
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @staticmethod
    def put(request, product_id):
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 23.08. Преобразовать код программы с использованием классов высокого уровня.
class APIProducts2(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class APIProductsDetail2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# 23.09. Преобразовать код программы с использованием ModelViewSet.
class APIProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
