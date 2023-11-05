from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, CostomUserViewSet, TenderViewSet, TenderAnalysisView

post_router = DefaultRouter()
post_router.register(r'comment', CommentViewSet)
post_router.register(r'tender', TenderViewSet)
post_router.register(r'costomuser', CostomUserViewSet)
post_router.register(r'tenderanalysis', TenderAnalysisView, basename='TenderAnalysis')