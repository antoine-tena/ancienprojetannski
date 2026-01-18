from django.core.management.base import BaseCommand
from website.models import HeaderConfig, Page


class Command(BaseCommand):
    help = 'Crée des données de test pour le site'

    def handle(self, *args, **kwargs):
        # Créer la configuration du header
        header, created = HeaderConfig.objects.get_or_create(
            pk=1,
            defaults={
                'title': 'Mon Site Web',
                'logo_text': 'AnnSki',
                'show_login_button': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Header config créée'))
        else:
            self.stdout.write(self.style.WARNING('Header config existe déjà'))

        # Créer des pages de test
        home, _ = Page.objects.get_or_create(
            slug='home',
            defaults={
                'title': 'Accueil',
                'order': 1,
                'is_visible': True
            }
        )

        about, _ = Page.objects.get_or_create(
            slug='about',
            defaults={
                'title': 'À propos',
                'order': 2,
                'is_visible': True
            }
        )

        services, _ = Page.objects.get_or_create(
            slug='services',
            defaults={
                'title': 'Services',
                'order': 3,
                'is_visible': True
            }
        )

        # Sous-pages de Services
        Page.objects.get_or_create(
            slug='web-development',
            defaults={
                'title': 'Développement Web',
                'parent': services,
                'order': 1,
                'is_visible': True
            }
        )

        Page.objects.get_or_create(
            slug='mobile-development',
            defaults={
                'title': 'Développement Mobile',
                'parent': services,
                'order': 2,
                'is_visible': True
            }
        )

        contact, _ = Page.objects.get_or_create(
            slug='contact',
            defaults={
                'title': 'Contact',
                'order': 4,
                'is_visible': True
            }
        )

        self.stdout.write(self.style.SUCCESS('Pages de test créées avec succès !'))
