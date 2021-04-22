from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from question.models import Subject,Question


admin.site.register(
    Subject,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(Question)
