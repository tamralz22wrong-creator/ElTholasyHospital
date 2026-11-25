from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'مدير النظام'),
        ('doctor', 'طبيب'),
        ('nurse', 'تمريض'),
        ('employee', 'موظف'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='employee',
        verbose_name='الدور الوظيفي',
    )

    # ---------------------------------------------------------------------------
    # الحقول الإضافية لحل مشكلة التضارب (E304) نهائياً واجتياز فحص النظام
    # ---------------------------------------------------------------------------
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="accounts_user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="accounts_user_permissions",
        related_query_name="user",
    )

    def __str__(self):
        return self.username














