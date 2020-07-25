from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class GymnasiumListView(APIView):
    # Вывод списка физкультурных залов
    def get(self, request):
        gymnasiums = Gymnasium.objects.all()
        serializer = GymmnasiumListSerializer(gymnasiums, many=True)
        return Response(serializer.data)

class GymnasiumDetailView(APIView):
    # Вывод конкретного зала
    def get(self, request, pk):
        gymnasium = Gymnasium.objects.get(id=pk)
        serializer = GymnasiumDetailView(gymnasium)
        return Response(serializer.data)