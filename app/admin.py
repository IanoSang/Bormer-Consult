from django.contrib import admin
from .models import Profile, Consultation, Message, CallRequest, Inquiry
# Register your models here.
admin.site.register(Profile)
admin.site.register(Consultation)
admin.site.register(Message)
admin.site.register(CallRequest)
admin.site.register(Inquiry)
