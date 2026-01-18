from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Crée le superuser admin/admin'

    def handle(self, *args, **options):
        username = 'admin'
        password = 'admin'
        email = 'admin@admin.com'
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'Le superuser "{username}" existe déjà')
            )
            return
        
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Superuser créé avec succès:\n'
                f'  Username: {username}\n'
                f'  Password: {password}'
            )
        )
