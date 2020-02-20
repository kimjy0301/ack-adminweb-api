from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, userid, date_of_birth, password=None):
        if not userid:
            raise ValueError("사용자 아이디는 필수 항목입니다.")

        user = self.model(userid=userid, date_of_birth=date_of_birth)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, date_of_birth, password):
        user = self.create_user(
            userid=userid, date_of_birth=date_of_birth, password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    userid = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "userid"
    REQUIRED_FIELDS = ["date_of_birth"]

    def __str__(self):
        return self.userid

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        managed = False
        db_table = "EMRIF_USER"

