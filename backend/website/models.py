from django.db import models


class HeaderConfig(models.Model):
    """Configuration du header du site"""
    title = models.CharField(max_length=200, default="Mon Site")
    logo_text = models.CharField(max_length=100, default="Logo")
    show_login_button = models.BooleanField(default=True)
    
    # Logo
    logo_image = models.CharField(max_length=500, blank=True, null=True, help_text="URL de l'image du logo")
    logo_size = models.IntegerField(default=40, help_text="Hauteur du logo en pixels")
    logo_position = models.CharField(max_length=20, default="left", choices=[
        ('left', 'Gauche'),
        ('center', 'Centre'),
        ('right', 'Droite')
    ])
    
    # Styles personnalisables
    background_color = models.CharField(max_length=7, default="#333333", help_text="Couleur de fond (ex: #333333)")
    text_color = models.CharField(max_length=7, default="#ffffff", help_text="Couleur du texte (ex: #ffffff)")
    font_family = models.CharField(max_length=100, default="Arial, sans-serif", help_text="Police (ex: Arial, sans-serif)")
    
    # Bouton connexion
    login_button_color = models.CharField(max_length=7, default="#007bff", help_text="Couleur du bouton connexion")
    login_button_position = models.CharField(max_length=20, default="right", choices=[
        ('left', 'Gauche'),
        ('center', 'Centre'),
        ('right', 'Droite')
    ])
    
    # Bouton déconnexion
    logout_button_color = models.CharField(max_length=7, default="#dc3545", help_text="Couleur du bouton déconnexion")
    logout_button_position = models.CharField(max_length=20, default="right", choices=[
        ('left', 'Gauche'),
        ('center', 'Centre'),
        ('right', 'Droite')
    ])
    
    # Options avancées
    is_fixed = models.BooleanField(default=False, help_text="Header fixe en haut de page")
    opacity = models.FloatField(default=1.0, help_text="Opacité (0.0 à 1.0)")
    blur = models.IntegerField(default=0, help_text="Flou en pixels")
    border_width = models.IntegerField(default=0, help_text="Largeur de la bordure en pixels")
    border_color = models.CharField(max_length=7, default="#000000", help_text="Couleur de la bordure")
    height = models.IntegerField(default=70, help_text="Hauteur du header en pixels")
    padding_vertical = models.IntegerField(default=15, help_text="Padding vertical en pixels")
    padding_horizontal = models.IntegerField(default=20, help_text="Padding horizontal en pixels")
    shadow = models.CharField(max_length=100, default="0 2px 4px rgba(0,0,0,0.1)", help_text="Ombre CSS")
    exclude_pages = models.TextField(blank=True, help_text="Pages où ne pas afficher le header (une par ligne)")
    
    class Meta:
        verbose_name = "Configuration Header"
        verbose_name_plural = "Configuration Header"
    
    def __str__(self):
        return f"Header: {self.title}"
    
    @classmethod
    def get_config(cls):
        """Récupère ou crée la configuration unique"""
        config, created = cls.objects.get_or_create(pk=1)
        return config


class HeaderButton(models.Model):
    """Boutons personnalisables du header"""
    header_config = models.ForeignKey(HeaderConfig, on_delete=models.CASCADE, related_name='buttons')
    label = models.CharField(max_length=100, help_text="Texte du bouton")
    url = models.CharField(max_length=500, help_text="URL de destination")
    order = models.IntegerField(default=0, help_text="Ordre d'affichage")
    is_visible = models.BooleanField(default=True, help_text="Visible ou non")
    position = models.CharField(max_length=20, default="left", choices=[
        ('left', 'Gauche'),
        ('center', 'Centre'),
        ('right', 'Droite')
    ], help_text="Position du bouton dans le header")
    
    class Meta:
        ordering = ['order']
        verbose_name = "Bouton Header"
        verbose_name_plural = "Boutons Header"
    
    def __str__(self):
        return f"{self.label} ({self.url})"


class FooterConfig(models.Model):
    """Configuration du footer du site"""
    text = models.TextField(default="© 2026 Mon Site. Tous droits réservés.", help_text="Texte du footer")
    background_color = models.CharField(max_length=7, default="#222222", help_text="Couleur de fond")
    text_color = models.CharField(max_length=7, default="#ffffff", help_text="Couleur du texte")
    show_social_links = models.BooleanField(default=True, help_text="Afficher les réseaux sociaux")
    links = models.JSONField(default=list, blank=True, help_text="Liens du footer (JSON)")
    
    class Meta:
        verbose_name = "Configuration Footer"
        verbose_name_plural = "Configuration Footer"
    
    def __str__(self):
        return "Footer Configuration"
    
    @classmethod
    def get_config(cls):
        """Récupère ou crée la configuration unique"""
        config, created = cls.objects.get_or_create(pk=1)
        return config


class Theme(models.Model):
    """Thèmes visuels du site"""
    name = models.CharField(max_length=100, unique=True, help_text="Nom du thème")
    is_active = models.BooleanField(default=False, help_text="Thème actif")
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Polices
    font_pack = models.CharField(max_length=100, default="system", help_text="Pack de polices")
    base_font_size = models.IntegerField(default=16, help_text="Taille de base (px)")
    heading_font = models.CharField(max_length=200, default="Arial, sans-serif")
    body_font = models.CharField(max_length=200, default="Arial, sans-serif")
    button_font = models.CharField(max_length=200, default="Arial, sans-serif")
    
    # Palette de couleurs (5 couleurs principales)
    primary_color = models.CharField(max_length=7, default="#0066cc")
    secondary_color = models.CharField(max_length=7, default="#6c757d")
    accent_color = models.CharField(max_length=7, default="#28a745")
    background_color = models.CharField(max_length=7, default="#ffffff")
    text_color = models.CharField(max_length=7, default="#333333")
    
    # Boutons
    button_radius = models.IntegerField(default=4, help_text="Rayon des bords (px)")
    button_padding = models.CharField(max_length=50, default="10px 20px")
    
    # Espacement
    spacing_unit = models.IntegerField(default=8, help_text="Unité de base pour les espacements (px)")
    
    class Meta:
        verbose_name = "Thème"
        verbose_name_plural = "Thèmes"
        ordering = ['-is_active', 'name']
    
    def __str__(self):
        return f"{self.name} {'(Actif)' if self.is_active else ''}"
    
    def save(self, *args, **kwargs):
        if self.is_active:
            # Désactiver les autres thèmes
            Theme.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class Page(models.Model):
    """Représente une page du site"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    order = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    is_homepage = models.BooleanField(default=False, help_text="Page d'accueil")
    meta_description = models.TextField(blank=True, help_text="Description SEO")
    meta_keywords = models.CharField(max_length=500, blank=True, help_text="Mots-clés SEO")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Page"
        verbose_name_plural = "Pages"
    
    def __str__(self):
        return self.title
    
    def get_full_path(self):
        """Retourne le chemin complet de la page"""
        if self.is_homepage:
            return "/"
        if self.parent:
            return f"{self.parent.get_full_path()}/{self.slug}"
        return f"/{self.slug}"
    
    def save(self, *args, **kwargs):
        if self.is_homepage:
            # S'assurer qu'il n'y a qu'une seule homepage
            Page.objects.filter(is_homepage=True).update(is_homepage=False)
        super().save(*args, **kwargs)


class PageSection(models.Model):
    """Section d'une page avec son contenu"""
    SECTION_TYPES = [
        ('text', 'Texte'),
        ('form', 'Formulaire'),
        ('product', 'Produit'),
        ('event', 'Événement'),
        ('quote', 'Citation'),
        ('images', 'Images'),
        ('video', 'Vidéo'),
        ('chart', 'Graphique'),
        ('audio', 'Audio'),
        ('map', 'Carte GPS'),
        ('html', 'HTML Personnalisé'),
    ]
    
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='sections')
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, default='text')
    title = models.CharField(max_length=200, blank=True, help_text="Titre de la section")
    content = models.JSONField(default=dict, help_text="Contenu structuré de la section")
    order = models.IntegerField(default=0, help_text="Ordre d'affichage")
    is_visible = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Section de Page"
        verbose_name_plural = "Sections de Page"
    
    def __str__(self):
        return f"{self.page.title} - {self.get_section_type_display()} ({self.order})"

class SEOConfig(models.Model):
    """Configuration SEO du site"""
    # Meta Tags
    site_title = models.CharField(max_length=200, default="Mon Site", help_text="Titre du site")
    site_description = models.TextField(default="", blank=True, help_text="Description du site")
    keywords = models.TextField(default="", blank=True, help_text="Mots-clés (séparés par des virgules)")
    author = models.CharField(max_length=200, default="", blank=True, help_text="Auteur du site")
    
    # Open Graph
    og_title = models.CharField(max_length=200, default="", blank=True, help_text="Titre OG")
    og_description = models.TextField(default="", blank=True, help_text="Description OG")
    og_image = models.CharField(max_length=500, default="", blank=True, help_text="URL image OG")
    
    # Twitter Card
    twitter_card = models.CharField(max_length=50, default="summary_large_image", help_text="Type de carte Twitter")
    twitter_title = models.CharField(max_length=200, default="", blank=True, help_text="Titre Twitter")
    twitter_description = models.TextField(default="", blank=True, help_text="Description Twitter")
    twitter_image = models.CharField(max_length=500, default="", blank=True, help_text="URL image Twitter")
    
    # Indexation
    allow_indexing = models.BooleanField(default=True, help_text="Autoriser l'indexation par les moteurs de recherche")
    robots_txt = models.TextField(default="", blank=True, help_text="Contenu du fichier robots.txt")
    
    # Analytics
    google_analytics_id = models.CharField(max_length=50, default="", blank=True, help_text="ID Google Analytics")
    google_site_verification = models.CharField(max_length=100, default="", blank=True, help_text="Code de vérification Google")
    facebook_pixel_id = models.CharField(max_length=50, default="", blank=True, help_text="ID Facebook Pixel")
    custom_head_scripts = models.TextField(default="", blank=True, help_text="Scripts personnalisés à ajouter dans <head>")
    
    # Sitemap
    site_url = models.CharField(max_length=500, default="", blank=True, help_text="URL complète du site")
    auto_generate_sitemap = models.BooleanField(default=True, help_text="Générer automatiquement le sitemap")
    sitemap_changefreq = models.CharField(max_length=20, default="weekly", help_text="Fréquence de mise à jour")
    
    class Meta:
        verbose_name = "Configuration SEO"
        verbose_name_plural = "Configuration SEO"
    
    def __str__(self):
        return "Configuration SEO"
    
    @classmethod
    def get_config(cls):
        """Récupère ou crée la configuration unique"""
        config, created = cls.objects.get_or_create(pk=1)
        return config