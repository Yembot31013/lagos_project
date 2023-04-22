from django.contrib import admin
from .models import Competition, District, Zone, School

# Register your models here.
class DistrictInline(admin.StackedInline):
    model = District


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam_status', 'exam_duration', 'starting_at')
    search_fields = ('name', 'description')
    list_filter = ('exam_status', 'can_join_with_link')
    date_hierarchy = 'starting_at'
    fieldsets = (
        (None, {
            "fields": (
                'name', 'description'
            ),
        }),
        ('Timing', {
            "fields": (
                'exam_duration', 'starting_at', 'ending_at'
            ),
        }),
        ('Joining & Rules', {
            "fields": (
                'custom_link_slug', 'can_join_with_link', 'number_of_allowed_attempt', 'joining_password', 'request_password_when_using_link'
            ),
        }),
    )
    

class Local_GovernmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fieldsets = (
        (None, {
            "fields": (
                'name',
            ),
        }),
    )
    

    inlines = [DistrictInline]


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'zone', 'district', 'school_level')
    search_fields = ('name', 'zone__name', 'district__name', 'school_level')
    list_filter = ('zone', 'school_level', 'district')
    


admin.site.register(School, SchoolAdmin)
# admin.site.register(Competition, CompetitionAdmin)
# admin.site.register(Local_Government, Local_GovernmentAdmin)
admin.site.register(Competition)
admin.site.register(Zone)
admin.site.register(District)

