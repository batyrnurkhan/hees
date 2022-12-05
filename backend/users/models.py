from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.


class UserManager(auth_models.BaseUserManager):
    def create_user(self, fullname: str, 
                    email:str , 
                    password: str = None, is_staff = False, 
                    is_superuser = False) -> "User":
        if not email:
            raise ValueError("no email")
        if not fullname:
            raise ValueError("no fullname")

        user = self.model(email=self.normalize_email(email))
        user.fullname = fullname
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(self, fullname: str, 
                    email:str , 
                    password: str) -> "User":
        user = self.create_user(
            fullname= fullname,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )

        user.save()

        return user



class User(auth_models.AbstractUser):
    fullname = models.CharField(verbose_name="First Name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname"]


class Role(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name