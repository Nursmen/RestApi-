from django.urls import path
from . import views

urlpatterns = [
    path('/tender/<int:pk>/neural/', views.TenderAnalysisView.as_view(), name='tender-neural'),
    # Other URL patterns specific to this app
]