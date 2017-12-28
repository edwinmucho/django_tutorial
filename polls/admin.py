from django.contrib import admin
from .models import Question,Choice

# class ChoiceInline(admin.StackedInline):   # StackedInline 은 공간을 많이 차지함.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # 제목             , 필드
        ('Date information', {'fields': ['pub_date']}),
        (None, {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # fields = ['pub_date', 'question_text']  # 간단한 경우 해당하는 것 처럼 하면됨. 순서 정렬 가능.

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
