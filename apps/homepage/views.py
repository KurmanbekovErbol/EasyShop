from rest_framework import viewsets
from apps.homepage.models import HeaderFooter, Homepage, Statistics, Sections, Content
from apps.homepage.serializers import ContentSerializer, HeaderFooterSerializer, HomepageModelSerializer, SectionsSerializer, StatisticsSerializer

class HomepageModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Homepage.objects.all()
    serializer_class = HomepageModelSerializer

class StatisticsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

class HeaderFooterAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = HeaderFooter.objects.all()
    serializer_class = HeaderFooterSerializer

class SectionsAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer
    
class ContentAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer