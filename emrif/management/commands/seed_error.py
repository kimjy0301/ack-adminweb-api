from django.core.management.base import BaseCommand
from faker import Faker
from emrif.models import EmrifPc, EmrifError
import random


class Command(BaseCommand):
    help = "EmrifError 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default="1", type=int, help="몇개의 EmrifError 생성할지 넘겨주는 인자"
        )

    def handle(self, *args, **options):

        number = options.get("number", 1)

        for i in range(number):
            fake = Faker("ko_KR")

            all_pc = EmrifPc.objects.all()
            pc = random.choice(all_pc)
            time = fake.date(pattern="%Y-%m-%d %H:%M:%S", end_datetime=None)
            title = f"Error {time}"
            content = fake.sentence()

            EmrifError.objects.create(emrifpc=pc, title=title, content=content)
        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))

