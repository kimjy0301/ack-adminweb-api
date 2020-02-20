from django.core.management.base import BaseCommand
from faker import Faker
from emrif.models import EmrifPc, EmrifEquip
import random


class Command(BaseCommand):
    help = "PC 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default="1", type=int, help="몇개의 PC 생성할지 넘겨주는 인자"
        )

    def handle(self, *args, **options):

        number = options.get("number", 1)

        for i in range(number):
            fake = Faker("ko_KR")

            ip = fake.ipv4_private(network=False, address_class=None)
            all_equip = EmrifEquip.objects.all()
            equip = random.choice(all_equip)

            statuslist = ["SUCCESS", "ERROR"]

            rint = random.randint(0, 1)

            EmrifPc.objects.create(ip=ip, equip=equip, status=statuslist[rint])
        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))

