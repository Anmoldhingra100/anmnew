from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Sum
from django.db.models.functions import TruncWeek
from solar_app.models import MySolarrr
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta
from solar_app.models import MySolarrr
from .serializers import EnergyDataSerializer
# Create your views here.


def home_page_view(request):
    return request(request,'solarr.html')



class WeeklyDataAPIView(APIView):
    def get(self, request):
        today = timezone.now()
        start_of_week = today - timedelta(days=today.weekday())  # Monday of the current week
        end_of_week = start_of_week + timedelta(days=6)  # Sunday of the current week

        # Querying the database for records within the current week
        weekly_data = MySolarrr.objects.filter(date__range=[start_of_week, end_of_week])
        serializer = EnergyDataSerializer(weekly_data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



    




