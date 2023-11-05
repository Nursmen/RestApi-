from django.shortcuts import render
import openai
from rest_framework import generics
from .models import Tender
from .serializers import TenderSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import openai

# Create your views here.
class TenderAnalysisView(APIView):
    def get(self, request, pk):
        try:
            Tender = Tender.objects.get(pk=pk)
            # Assuming you have a 'text' field in the Tender model
            Tender_text = Tender.text
        except Tender.DoesNotExist:
            return Response({"error": "Tender not found"}, status=status.HTTP_404_NOT_FOUND)

        def analyze_Tender(Tender_text):
            openai.api_key = 'YOUR_OPENAI_API_KEY'

            prompt = f"{Tender_text}"

            response = openai.Completion.create(
                engine="davinci",  # You can experiment with different engines
                prompt=prompt,
                max_tokens=700,  # Limit the response to a single token (good or bad)
                temperature=0.0,  # Set to 0 for deterministic output
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["\n"]
            )

            sentiment = response.choices[0].text.strip()

            return sentiment

        result = analyze_Tender(Tender_text)

        return Response({"result": result}, status=status.HTTP_200_OK)