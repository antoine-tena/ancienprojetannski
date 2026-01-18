from rest_framework import serializers
from django.contrib.auth.models import User
from .models import HeaderConfig, HeaderButton, FooterConfig, Theme, Page, PageSection, SEOConfig


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'is_superuser']


class HeaderButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderButton
        fields = ['id', 'label', 'url', 'order', 'is_visible', 'position', 'header_config']


class HeaderConfigSerializer(serializers.ModelSerializer):
    buttons = HeaderButtonSerializer(many=True, read_only=True)
    
    class Meta:
        model = HeaderConfig
        fields = '__all__'


class FooterConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterConfig
        fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'


class PageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSection
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    full_path = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    sections = PageSectionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'parent', 'order', 'is_visible', 'is_homepage',
                  'meta_description', 'meta_keywords', 'created_at', 'updated_at', 
                  'full_path', 'children', 'sections']
    
    def get_full_path(self, obj):
        return obj.get_full_path()
    
    def get_children(self, obj):
        children = obj.children.all()
        return PageSerializer(children, many=True).data

class SEOConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEOConfig
        fields = '__all__'