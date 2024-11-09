from django.contrib import admin
from .models import Practise
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Practise)
class PractiseOne(SummernoteModelAdmin):
    summernote_fields=('content',)
    search_fields=['title']
    




# Register your models here.
