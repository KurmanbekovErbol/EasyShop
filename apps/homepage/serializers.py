from rest_framework import serializers
from apps.homepage.models import Brand, Content, HeaderFooter, Homepage, Partner, Sections, Statistics

class HomepageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homepage
        fields = ['id', 'title', 'content', 'file']

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ['users_count', 'bought_products_count', 'total_products_count']

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['name',]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name',]


class HeaderFooterSerializer(serializers.ModelSerializer):
    partners = PartnerSerializer(many=True, read_only=True)
    brands = BrandSerializer(many=True, read_only=True)
    
    class Meta:
        model = HeaderFooter
        fields = [
            'title', 
            'bottom_text', 
            'top_logo', 
            'bottom_logo',
            'instagram',
            'telagram',
            'vk',
            'partners', 
            'brands', 
        ]
        
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'description', 'image']


class SectionsSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Sections
        fields = ['id', 'name', 'description', 'image', 'contents']