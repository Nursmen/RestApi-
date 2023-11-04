from django.shortcuts import render
import openai
from rest_framework import generics
from .models import Tender
from .serializers import TenderSerializer

# Create your views here.
# my view should parse my tender data through api
class TenderList(generics.ListCreateAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer

    def get_queryset(self):
        tender_id = self.kwargs['tender_id']
        return Tender.objects.filter(id=tender_id)