from django.contrib import admin
from qa.models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
