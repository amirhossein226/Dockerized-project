from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Creating superuser"

    def handle(self, *args, **kwargs):
        admin = User.objects.filter(username='admin').exists()
        if not admin:
            User.objects.create_superuser(
                username='admin',
                email='admin@gmail.com',
                password='admin'
            )

            self.stdout.write(self.style.SUCCESS(
                "====================Admin Created===================="))
        else:
            self.stdout.write(self.style.NOTICE(
                "xxxxxxxxxxxxxxxxxxxxxxxxxxx Admin already exists xxxxxxxxxxxxxxxxxxxxxxxxxx"))
