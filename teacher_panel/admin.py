from django.contrib import admin
from .models import Teacher

# Register your models here.
class Teacher_ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'verified', 'school', 'verified_at', 'joined_at')
    search_fields = ('name', 'user', 'school')
    date_hierarchy = 'verified_at'
    list_filter = ('verified', 'school', 'local_government', 'district')
    
    fieldsets = (
        (None, {
            "fields": (
                'name', 'local_government', 'district', 'school'
            ),
        }),
        ('Personal Info', {
            "fields": (
                'gender', 'date_of_birth', 'longitude', 'latitude'
            ),
        }),
        ('Verification', {
            "fields": (
                'access_code', 'verified_at', 'verified', 'profile_pics'
            ),
        }),
    )
    

admin.site.register(Teacher)
