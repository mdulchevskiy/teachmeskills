# pip install django
# pip install djangorestframework


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from task_23.serializers import FioSerializer
from task_23.models import Fio
from rest_framework import (status, 
                            generics, )


# 23. Покрыть модель Fio CRUD с использованием Django REST framework.
# a. С использованием декоратора api_view.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_fio(request, pk=None):
    data = Fio.objects.all() if not pk else Fio.objects.get(id=pk)
    many = True if not pk else False
    if request.method == 'GET':
        serializer = FioSerializer(data, many=many)
        return Response(serializer.data)
    elif many and request.method == 'POST':
        serializer = FioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif not many and request.method == 'PUT':
        serializer = FioSerializer(data, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif not many and request.method == 'DELETE':
        data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# b. С использованием контроллера класса.
class APIFioAll(APIView):
    @staticmethod
    def get(request, pk=None):
        data = Fio.objects.all() if not pk else Fio.objects.get(id=pk)
        many = True if not pk else False
        serializer = FioSerializer(data, many=many)
        return Response(serializer.data)

    @staticmethod
    def post(request, pk=None):
        if not pk:
            serializer = FioSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, pk=None):
        if pk:
            data = Fio.objects.get(id=pk)
            serializer = FioSerializer(data, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk=None):
        if pk:
            data = Fio.objects.get(id=pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# c. С использованием контроллера класса высокого уровня.
class APIFio(generics.ListCreateAPIView):
    queryset = Fio.objects.all()
    serializer_class = FioSerializer


class APIFioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fio.objects.all()
    serializer_class = FioSerializer


# d. С использованием мета контроллера.
class APIFioViewSet(ModelViewSet):
    queryset = Fio.objects.all()
    serializer_class = FioSerializer
