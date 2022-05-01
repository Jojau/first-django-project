from django.contrib import admin

from monApp.models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['text']

admin.site.register(Question)