from django.contrib import admin
from robot_control.models import Category, Question, Response 

#### Category
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category', {'fields': ['name', 'description', 'RFID_id']}),
    ]
    inlines = [QuestionInline]
    list_display = ('name', 'RFID_id')

admin.site.register(Category, CategoryAdmin)

#### Question
class ResponseInline(admin.TabularInline):
    model = Response
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['title', 'explanation', 'category', 'difficulty']}),
    ]
    inlines = [ResponseInline]
    list_display = ('title', 'difficulty', 'category')
    list_filter = ['category', 'difficulty']

admin.site.register(Question, QuestionAdmin)

#### Response
class ResponseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Response', {'fields': ['body', 'true', 'question']}),
    ]
    list_display = ('body', 'true', 'question')
    list_filter = ['question']

admin.site.register(Response, ResponseAdmin)