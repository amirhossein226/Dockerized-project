from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from blog.models import Post
import faker
import random
from django.db.utils import IntegrityError
from deep_translator import GoogleTranslator
from time import sleep
import jdatetime
UserModel = get_user_model()


class Command(BaseCommand):
    help = "Used for Initialize the blog.Post models"

    def handle(self, *args, **kwargs):
        users = UserModel.objects
        fake = faker.Faker()
        fa_fake = faker.Faker("fa_IR")
        if users.count() <= 3:
            for user in range(10):
                username = fake.name().lower()
                email = f"{username}@gmail.com"
                password = f'{username}1234'
                try:
                    get_user_model().objects.create_user(
                        username, email, password)
                except Exception as e:
                    print(e)
                    continue

        users = UserModel.objects.all()

        for _ in range(50):
            title = fa_fake.text(30)[:-1]
            # translating the fa title to pa for slugs
            trans_slugify = GoogleTranslator('fa', 'en').translate(
                title).lower().strip().split()
            slug = '-'.join(trans_slugify)
            body = fa_fake.paragraph(50)
            status = random.choice(Post.Status.values)
            authors = random.choices(users, k=random.randint(1, 3))
            spl_title = title.split()
            tags = random.choices(
                spl_title, k=random.randint(1, len(spl_title)))

            post = Post.objects.create(
                title=title,
                slug=slug,
                body=body,
                status=status,

            )
            post.author.add(*authors)
            for tag in tags:
                try:
                    post.tags.add(tag)
                except IntegrityError:
                    print(
                        '==============================================================')
                    print('already exists!')
                    continue
        self.stdout.write(self.style.SUCCESS('Initialization complete!'))
