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
            print(Tender_text)
            openai.api_key = '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'

            prompt = f"{Tender_text}"

            response = openai.Completion.create(
                engine="davinci",  # You can experiment with different engines
                prompt=prompt,
            )

            sentiment = response.choices[0].text.strip()

            return sentiment

        result = analyze_Tender(Tender_text)

        return Response({"result": result}, status=status.HTTP_200_OK)