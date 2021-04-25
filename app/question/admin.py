from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django.forms import CheckboxSelectMultiple
from django.db import models


from question.models import Subject,Question
from question.models import Test
from more_admin_filters import MultiSelectDropdownFilter

class SubjectAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_questions_count', 'related_questions_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Subject.objects.add_related_count(
            qs,
            Question,
            'subject',
            'questions_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Subject.objects.add_related_count(qs,
                                                Question,
                                                'subject',
                                                'questions_count',
                                                cumulative=False)
        return qs

    def related_questions_count(self, instance):
        return instance.questions_count

    related_questions_count.short_description = 'Related Questions (for this specific Subject)'

    def related_questions_cumulative_count(self, instance):
        return instance.questions_cumulative_count

    related_questions_cumulative_count.short_description = 'Related Questions (in tree)'



admin.site.register(
    Subject,
    SubjectAdmin,
)

class TestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField : {'widget':CheckboxSelectMultiple}
    }
    filter_horizontal = ('questions',)


admin.site.register(Question)
admin.site.register(Test,TestAdmin)
