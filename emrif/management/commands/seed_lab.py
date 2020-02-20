from django.core.management.base import BaseCommand
from faker import Faker
from emrif.models import EmrifLab, EmrifDept
import random


class Command(BaseCommand):
    help = "LAB 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default="1", type=int, help="몇개의 방 생성할지 넘겨주는 인자"
        )

    def handle(self, *args, **options):

        number = options.get("number", 1)

        for i in range(number):
            fake = Faker("ko_KR")
            count = EmrifLab.objects.all().count() + 1
            name = f"검사실 {count}"
            center = fake.numerify(text="###")
            last = fake.numerify(text="####")
            callnumber = f"02-{center}-{last}"
            all_dept = EmrifDept.objects.all()
            dept = random.choice(all_dept)

            EmrifLab.objects.create(
                name=name, dept=dept, call_number=callnumber)
        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))
