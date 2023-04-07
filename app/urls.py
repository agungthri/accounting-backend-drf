from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

# create a router and register our viewsets with it

router = DefaultRouter()
router.register(r'transaction-journal', views.TransactionJournalViewSet, basename='transaction-account')
router.register(r'transactions', views.TransactionViewSet, basename='transaction')
router.register(r'accounts', views.AccountViewSet, basename='account')
router.register(r'journals', views.JournalViewSet, basename='journal')
router.register(r'report', views.ReportViewSet, basename='report')

# API Urls now are determined automatically with router
urlpatterns = [
    path('', include(router.urls)),
]