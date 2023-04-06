from cart.models import Cart
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Email must be specified")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        cart = Cart.objects.create(user=user)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Profile model"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
    ]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Учетная запись"
        verbose_name_plural = "Учетные записи"


class ProfileInfo(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self):
        return f"Profile for {self.user.name}"

    class Meta:
        verbose_name = "Доп. информация"
        verbose_name_plural = "Доп. информация"
