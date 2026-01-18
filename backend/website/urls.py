from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'header', views.HeaderConfigViewSet, basename='header')
router.register(r'header-buttons', views.HeaderButtonViewSet, basename='header-buttons')
router.register(r'footer', views.FooterConfigViewSet, basename='footer')
router.register(r'themes', views.ThemeViewSet, basename='themes')
router.register(r'pages', views.PageViewSet, basename='pages')
router.register(r'page-sections', views.PageSectionViewSet, basename='page-sections')
router.register(r'seo', views.SEOConfigViewSet, basename='seo')

urlpatterns = [
    path('auth/csrf/', views.get_csrf_token, name='csrf_token'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/me/', views.current_user, name='current_user'),
    path('upload/', views.upload_image, name='upload_image'),
    path('', include(router.urls)),
]
