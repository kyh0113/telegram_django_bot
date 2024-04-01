from django.contrib import admin
from .models import DATA_WORKER
from .models import DATA_IMAGE
from .models import QUESTION
from .models import ANSWER

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['QUESTION_ID', 'QUESTION', 'QUESTION_CNT', 'IMAGE_ID', 'STATUS']
    search_fields= ['QUESTION']

# Register your models here.
admin.site.register(DATA_WORKER)
admin.site.register(DATA_IMAGE)
admin.site.register(QUESTION, QuestionAdmin)
admin.site.register(ANSWER)