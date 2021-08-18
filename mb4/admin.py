
from django.contrib import admin

from .models import Reeks, Opgave, Oefening


class ChoiceInline(admin.TabularInline):
    model = Opgave
    extra = 3

@admin.register(Reeks)
class ReeksAdmin(admin.ModelAdmin):
    fieldsets = [
        ('reeksoverzicht',{'fields': ['titel','foto','uitleg','datum','soort','glob_moeilkhgr','glob_strtijd']})]
    #     ( 'date info', {'fields': ['onderwerp'], 'classes': ['collapse']}),
    # ]
    inlines = [ChoiceInline]
    search_fields = ['titel']
    list_display = ('titel', 'datum','glob_strtijd')

@admin.register(Oefening)
class OefeningAdmin(admin.ModelAdmin):
    search_fields = ['student']
    list_display = ('student','oef_datum')


    # student = models.ForeignKey(User, on_delete=models.CASCADE)
    # opgave = models.ForeignKey(Opgave, on_delete=models.CASCADE)
    # antwoord = models.IntegerField(blank=True)
    # delta = models.IntegerField()
    # oef_datum = models.DateTimeField('datum_gemaakt')

    # def __str__(self):
    #     return self.student + self.opgave

    # class Meta:
    #     verbose_name = ('Oefening')
    #     verbose_name_plural =('Oefeningen')
    #     # ordering = ('datum')




# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     search_fields = ['question_text']
#     list_display = ('question_text', 'pub_date', 'was_published_recently')

# admin.site.register(Question, QuestionAdmin)
