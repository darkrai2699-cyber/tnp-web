import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator


class AlumniManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        if 'id' not in extra_fields or not extra_fields['id']:
            extra_fields['id'] = str(uuid.uuid4())[:8]
        user = self.model(email=email, full_name=full_name, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, full_name, password, **extra_fields)


class Alumni(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=255, primary_key=True, unique=True, editable=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        help_text="Include country code with '+' and brackets if needed (e.g., +1 (555) 555-5555)"
    )
    password = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to='media/profile_photos/', blank=True, null=True)
    current_job_profile = models.CharField(max_length=255, blank=True, null=True)
    current_company = models.CharField(max_length=255, blank=True, null=True)
    current_job_location = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    sub_district = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    is_international = models.BooleanField(default=False)
    country = models.CharField(max_length=255, blank=True, null=True)
    full_address = models.TextField()
    graduation_year = models.PositiveIntegerField(
        default=2025,
        validators=[MinValueValidator(1900), MaxValueValidator(2025)]
    )
    experience = models.IntegerField(default=0)
    facebook = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    is_top_alumni = models.BooleanField(
        default=False,
        help_text="Mark as top alumni for display on the home page."
    )
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='alumni_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='alumni_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    objects = AlumniManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name


class Admin(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AlumniCoordinator(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    class Meta:
        db_table = 'alumni_coordinator'

    def __str__(self):
        return self.name


class GraduationYear(models.Model):
    year = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.year)


class BatchMentor(models.Model):
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to='media/mentor_photos/', blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    assigned_batches = models.ManyToManyField(
        GraduationYear,
        related_name='mentors_assigned',
        blank=True
    )

    def __str__(self):
        return self.full_name


class Batch(models.Model):
    graduation_year = models.IntegerField()
    mentors = models.ManyToManyField(
        BatchMentor,
        related_name='batches_assigned'
    )

    def __str__(self):
        return f"Batch {self.graduation_year}"


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    media = models.FileField(upload_to='events/', blank=True, null=True, max_length=255)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GalleryPhoto(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]


class Visitor(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Visitor: {self.count}"


class VisitorCount(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Visitor Count: {self.count}"
