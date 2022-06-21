from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = CloudinaryField(default='https://res.cloudinary.com/dpww3jwgm/image/upload/v1654722449/default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    citizenship = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def delete_profile(self):
        self.delete()


class Consultation(models.Model):
    name = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='consultations')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Consultation'

    class Meta:
        ordering = ["-pk"]


class Inquiry(models.Model):
    title = models.CharField(max_length=100)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='inquiries')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='inquiries')
    created = models.DateTimeField(auto_now_add=True, null=True)


class Message(models.Model):
    name = models.CharField(max_length=250, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12, blank=True, null=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)


class CallRequest(models.Model):
    name = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
