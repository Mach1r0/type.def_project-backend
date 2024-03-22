# Import necessary modules from Django
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Define a custom user manager
class UserManager(BaseUserManager):
    # Define a method to create and save a user
    def create_user(self, email, name, password=None):
        # Raise an error if no email is provided
        if not email:
            raise ValueError('The Email field must be set')
        # Normalize the email by lowercasing the domain part of it
        email = self.normalize_email(email)
        # Create a user object
        user = self.model(email=email, name=name)
        # Set user's password, this also hashes the password.
        user.set_password(password)
        # Save the user object to the database
        user.save(using=self._db)
        return user

# Define a custom user model
class User(AbstractBaseUser, PermissionsMixin):
    # Define fields for the model
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Specify the manager for the model
    objects = UserManager()

    # Specify the field to be used as username
    USERNAME_FIELD = 'email'
    # Specify the fields that will be prompted for when creating a superuser
    REQUIRED_FIELDS = ['name']

    # Define a many-to-many relationship with Group model
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="%(app_label)s_%(class)s_related",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    def __str__(self):
        return f'name: {self.name} | Email- {self.email}'