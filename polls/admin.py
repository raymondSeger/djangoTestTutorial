from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    # the first parameter of the tuple is the title
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

# Register your models here.
admin.site.register(Question, QuestionAdmin)