from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.homepage.views import HomepageModelViewSet, StatisticsViewSet, HeaderFooterAPIView, SectionsAPIView, ContentAPIView

router = DefaultRouter()
router.register(r'homepage', HomepageModelViewSet, basename='homepage')
router.register(r'statistics', StatisticsViewSet, basename='statistics')
router.register(r'header-footer', HeaderFooterAPIView, basename='header-footer')
router.register(r'sections', SectionsAPIView, basename='sections')
router.register(r'contents', ContentAPIView, basename='contents')

urlpatterns = [

]

urlpatterns += router.urls