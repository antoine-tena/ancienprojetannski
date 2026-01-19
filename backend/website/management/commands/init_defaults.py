from django.core.management.base import BaseCommand
from website.models import HeaderConfig, FooterConfig, Theme, Page, PageSection


class Command(BaseCommand):
    help = 'Crée les données par défaut (header, footer, homepage, theme)'

    def handle(self, *args, **options):
        # Créer le header par défaut
        header, created = HeaderConfig.objects.get_or_create(
            pk=1,
            defaults={
                'title': 'Mon Site',
                'logo_text': 'Logo',
                'show_login_button': True,
                'background_color': '#333333',
                'text_color': '#ffffff',
                'font_family': 'Arial, sans-serif'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Header créé'))
        else:
            self.stdout.write(self.style.WARNING('✓ Header existe déjà'))

        # Créer le footer par défaut
        footer, created = FooterConfig.objects.get_or_create(
            pk=1,
            defaults={
                'text': '© 2026 Mon Site. Tous droits réservés.',
                'background_color': '#222222',
                'text_color': '#ffffff',
                'show_social_links': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Footer créé'))
        else:
            self.stdout.write(self.style.WARNING('✓ Footer existe déjà'))

        # Créer le thème par défaut
        theme, created = Theme.objects.get_or_create(
            name='Défaut',
            defaults={
                'is_active': True,
                'font_pack': 'system',
                'base_font_size': 16,
                'heading_font': 'Arial, sans-serif',
                'body_font': 'Arial, sans-serif',
                'button_font': 'Arial, sans-serif',
                'primary_color': '#0066cc',
                'secondary_color': '#6c757d',
                'accent_color': '#28a745',
                'background_color': '#ffffff',
                'text_color': '#333333',
                'button_radius': 4,
                'button_padding': '10px 20px',
                'spacing_unit': 8
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Thème par défaut créé'))
        else:
            self.stdout.write(self.style.WARNING('✓ Thème par défaut existe déjà'))

        # Créer la page d'accueil
        homepage, created = Page.objects.get_or_create(
            slug='home',
            defaults={
                'title': 'Accueil',
                'is_homepage': True,
                'is_visible': True,
                'order': 0,
                'meta_description': 'Bienvenue sur notre site',
                'meta_keywords': 'accueil, site web'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Page d\'accueil créée'))
            
            # Créer une section de bienvenue
            PageSection.objects.create(
                page=homepage,
                section_type='text',
                title='Bienvenue',
                content={
                    'text': '<h1>Bienvenue sur notre site</h1><p>Découvrez nos contenus et services.</p>'
                },
                order=0,
                is_visible=True
            )
            self.stdout.write(self.style.SUCCESS('  ✓ Section de bienvenue ajoutée'))
        else:
            self.stdout.write(self.style.WARNING('✓ Page d\'accueil existe déjà'))

        self.stdout.write(self.style.SUCCESS('\n✨ Initialisation terminée!'))
