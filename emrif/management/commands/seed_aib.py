from django.core.management.base import BaseCommand
from faker import Faker
from emrif.models import EmrifPc, EmrifAib
import random


class Command(BaseCommand):
    help = "AIB테이블 데이터 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default="1", type=int, help="몇개의 데이터를 생성할지 넘겨주는 인자"
        )

    def handle(self, *args, **options):

        number = options.get("number", 1)

        for i in range(number):
            fake = Faker("ko_KR")
            all_EmrifPc = EmrifPc.objects.all()
            emrifpc = random.choice(all_EmrifPc)

            state_flag = ["O", "O"]

            rint = random.randint(0, 1)

            created = fake.date_time_between(
                start_date="-2y", end_date="now", tzinfo=None
            )

            rstdate = created.strftime("%Y%m%d")

            EmrifAib.objects.create(
                pid=fake.random_number(digits=10, fix_len=False),
                rstseqno=fake.random_int(min=1, max=999, step=1),
                emrifpc=emrifpc,
                state_flag=state_flag[rint],
                created=created,
                rstdate=rstdate,
            )
        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))

