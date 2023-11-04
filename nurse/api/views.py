from rest_framework.viewsets import ModelViewSet
from ..models import Costom_User, Comment, Tender
from .serializers import CostomUserSerializer, CommentSerializer, TenderSerializer

class TenderViewSet(ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer


class CostomUserViewSet(ModelViewSet):
    queryset = Costom_User.objects.all()
    serializer_class = CostomUserSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer