from rest_framework.viewsets import ModelViewSet
from ..models import Costom_User, Comment, Tender
from .serializers import CostomUserSerializer, CommentSerializer, TenderSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import openai

class TenderViewSet(ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer


class CostomUserViewSet(ModelViewSet):
    queryset = Costom_User.objects.all()
    serializer_class = CostomUserSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TenderAnalysisView(ModelViewSet):
    model = Tender
    def get_queryset(self):
        try:
            Tender = self.model.objects.get(pk=self.kwargs['pk'])
            # Assuming you have a 'text' field in the Tender model
            Tender_text = Tender.chatgpt
        except Tender.DoesNotExist:
            return Response({"error": "Tender not found"}, status=status.HTTP_404_NOT_FOUND)

        def analyze_Tender(Tender_text):
            openai.api_key = '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'

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