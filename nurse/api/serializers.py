
from rest_framework.serializers import ModelSerializer
from ..models import Costom_User, Comment, Tender

class TenderSerializer(ModelSerializer):
    class Meta:
        model = Tender
        fields = '__all__'

class CostomUserSerializer(ModelSerializer): 
    class Meta:
        model = Costom_User
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'