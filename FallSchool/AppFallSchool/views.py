from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserInfo
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from . import models, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def first__screen(request):
  print(request, request.method)
  # if request.method == "POST":
  #     return HttpResponseRedirect(redirect_to= {url('second__screen')})
  return render(request, 'AppFallSchool/first__screen.html')


def second__screen(request):
  print(request, request.method)
  return render(request, 'AppFallSchool/second__screen.html')
class ItemAPIView(APIView):
    serializer_class = serializers.UserSerializer
    def get(self, request):
        items = models.User.objects.all()
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ItemViewSet(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

@api_view(['GET', 'POST'])
def item_view(request):
    if request.method == 'GET':
        items = models.Item.objects.all()
        serializer = serializers.UserSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)