from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from .models import HeaderConfig, HeaderButton, FooterConfig, Theme, Page, PageSection, SEOConfig
from .serializers import (UserSerializer, HeaderConfigSerializer, HeaderButtonSerializer,
                          FooterConfigSerializer, ThemeSerializer, PageSerializer, PageSectionSerializer,
                          SEOConfigSerializer)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def upload_image(request):
    """Upload d'une image"""
    if 'file' not in request.FILES:
        return Response({'error': 'Aucun fichier fourni'}, status=status.HTTP_400_BAD_REQUEST)
    
    file = request.FILES['file']
    
    # Vérifier que c'est une image
    if not file.content_type.startswith('image/'):
        return Response({'error': 'Le fichier doit être une image'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Créer un nom de fichier unique
    ext = os.path.splitext(file.name)[1]
    filename = f'uploads/{file.name}'
    
    # Sauvegarder le fichier
    path = default_storage.save(filename, ContentFile(file.read()))
    
    # Retourner l'URL du fichier
    url = default_storage.url(path)
    
    return Response({'url': url})


@api_view(['GET'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def get_csrf_token(request):
    """Obtenir le CSRF token"""
    return Response({'csrfToken': get_token(request)})


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """Connexion utilisateur"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return Response({
            'success': True,
            'user': serializer.data
        })
    else:
        return Response({
            'success': False,
            'error': 'Identifiants invalides'
        }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """Déconnexion utilisateur"""
    logout(request)
    return Response({'success': True})


@api_view(['GET'])
@permission_classes([AllowAny])
def current_user(request):
    """Récupère l'utilisateur courant"""
    if request.user.is_authenticated:
        serializer = UserSerializer(request.user)
        return Response({
            'authenticated': True,
            'user': serializer.data
        })
    return Response({
        'authenticated': False,
        'user': None
    })


class HeaderConfigViewSet(viewsets.ModelViewSet):
    """ViewSet pour la configuration du header"""
    queryset = HeaderConfig.objects.all()
    serializer_class = HeaderConfigSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'current']:
            return [AllowAny()]
        return [IsAdminUser()]
    
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def current(self, request):
        """Récupère la configuration actuelle du header"""
        config = HeaderConfig.get_config()
        serializer = self.get_serializer(config)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def save_with_buttons(self, request, pk=None):
        """Sauvegarde le header et ses boutons"""
        from django.utils.text import slugify
        
        header_config = self.get_object()
        
        # Mettre à jour tous les champs du header
        fields = ['title', 'logo_text', 'logo_image', 'logo_size', 'logo_position', 'show_login_button', 
                  'background_color', 'text_color', 'font_family',
                  'login_button_color', 'login_button_position',
                  'logout_button_color', 'logout_button_position',
                  'is_fixed', 'opacity', 'blur', 'border_width', 'border_color',
                  'height', 'padding_vertical', 'padding_horizontal', 'shadow', 'exclude_pages']
        
        for field in fields:
            if field in request.data:
                setattr(header_config, field, request.data[field])
        header_config.save()
        
        # Supprimer les anciens boutons
        header_config.buttons.all().delete()
        
        # Créer les nouveaux boutons et pages si nécessaire
        buttons_data = request.data.get('buttons', [])
        for btn_data in buttons_data:
            # Créer le bouton
            HeaderButton.objects.create(
                header_config=header_config,
                label=btn_data.get('text', btn_data.get('label', '')),
                url=btn_data.get('url', ''),
                order=btn_data.get('order', 0),
                position=btn_data.get('position', 'left'),
                is_visible=btn_data.get('is_visible', True)
            )
            
            # Créer la page si l'URL commence par / et que la page n'existe pas
            url = btn_data.get('url', '')
            if url.startswith('/') and url != '/':
                slug = url.strip('/').split('/')[0]  # Prendre le premier segment
                
                # Vérifier si la page existe déjà
                if not Page.objects.filter(slug=slug).exists():
                    Page.objects.create(
                        title=btn_data.get('text', btn_data.get('label', slug.capitalize())),
                        slug=slug,
                        is_visible=True,
                        order=btn_data.get('order', 0)
                    )
        
        serializer = self.get_serializer(header_config)
        return Response(serializer.data)


class HeaderButtonViewSet(viewsets.ModelViewSet):
    """ViewSet pour les boutons du header"""
    queryset = HeaderButton.objects.all()
    serializer_class = HeaderButtonSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]


class PageViewSet(viewsets.ModelViewSet):
    """ViewSet pour les pages"""
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'all_pages']:
            return [AllowAny()]
        return [IsAdminUser()]
    
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def tree(self, request):
        """Récupère l'arborescence complète des pages"""
        root_pages = Page.objects.filter(parent__isnull=True)
        serializer = self.get_serializer(root_pages, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def all_pages(self, request):
        """Récupère toutes les pages (incluant les enfants)"""
        pages = Page.objects.all()
        serializer = self.get_serializer(pages, many=True)
        return Response(serializer.data)


class FooterConfigViewSet(viewsets.ModelViewSet):
    """ViewSet pour la configuration du footer"""
    queryset = FooterConfig.objects.all()
    serializer_class = FooterConfigSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'current']:
            return [AllowAny()]
        return [IsAdminUser()]
    
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def current(self, request):
        """Récupère la configuration actuelle du footer"""
        config = FooterConfig.get_config()
        serializer = self.get_serializer(config)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        """Surcharge pour créer les pages automatiquement"""
        # Créer les pages pour les liens si nécessaire
        links = request.data.get('links', [])
        for link_data in links:
            url = link_data.get('url', '')
            if url.startswith('/') and url != '/':
                slug = url.strip('/').split('/')[0]  # Prendre le premier segment
                
                # Vérifier si la page existe déjà
                if not Page.objects.filter(slug=slug).exists():
                    Page.objects.create(
                        title=link_data.get('text', slug.capitalize()),
                        slug=slug,
                        is_visible=True,
                        order=0
                    )
        
        return super().update(request, *args, **kwargs)


class ThemeViewSet(viewsets.ModelViewSet):
    """ViewSet pour les thèmes"""
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'active']:
            return [AllowAny()]
        return [IsAdminUser()]
    
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def active(self, request):
        """Récupère le thème actif"""
        theme = Theme.objects.filter(is_active=True).first()
        if theme:
            serializer = self.get_serializer(theme)
            return Response(serializer.data)
        return Response({'message': 'Aucun thème actif'}, status=status.HTTP_404_NOT_FOUND)


class PageSectionViewSet(viewsets.ModelViewSet):
    """ViewSet pour les sections de page"""
    queryset = PageSection.objects.all()
    serializer_class = PageSectionSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

class SEOConfigViewSet(viewsets.ModelViewSet):
    """ViewSet pour la configuration SEO"""
    queryset = SEOConfig.objects.all()
    serializer_class = SEOConfigSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'config']:
            return [AllowAny()]
        return [IsAdminUser()]
    
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def config(self, request):
        """Récupère la configuration SEO unique"""
        config = SEOConfig.get_config()
        serializer = self.get_serializer(config)
        return Response(serializer.data)