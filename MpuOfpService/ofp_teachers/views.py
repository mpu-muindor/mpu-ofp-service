from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status

class AttendanceListView(APIView):

    def get(self, request):
        attendance = Attendance.objects
        serializer = AttendanceListSerializer(attendance, many = True)
        return Response(serializer.data)

class AddAttendanceView(APIView):

    def post(self, request):
        user = request.user
        if user.user_type == 'professor':
            serializer = AddAttendanceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)