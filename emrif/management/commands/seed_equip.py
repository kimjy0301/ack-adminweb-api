from django.core.management.base import BaseCommand
from faker import Faker
from emrif.models import EmrifLab, EmrifEquip
import random


class Command(BaseCommand):
    help = "EQUIP 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default="1", type=int, help="몇개의 장비를 생성할지 넘겨주는 인자"
        )

    def handle(self, *args, **options):

        number = options.get("number", 1)

        for i in range(number):
            fake = Faker("ko_KR")

            company = fake.company()
            center = fake.numerify(text="####")
            last = fake.numerify(text="####")
            callnumber = f"010-{center}-{last}"

            all_lab = EmrifLab.objects.all()
            lab = random.choice(all_lab)

            equip_name = fake.name()

            EmrifEquip.objects.create(
                name=fake.cryptocurrency_name(),
                equip_company=company,
                equip_name=equip_name,
                equip_number=callnumber,
                lab=lab,
            )

        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))

