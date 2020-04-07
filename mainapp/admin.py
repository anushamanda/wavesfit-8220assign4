from django.contrib import admin
from .models import Branche, Trainer, Event, Enrollment

class BrancheAdmin(admin.ModelAdmin):
    list_display =('branch_name', 'street', 'phone', 'email',)
    list_display_links = ('branch_name', 'street')
    list_filter=('branch_name', 'street')

class TrainerAdmin(admin.ModelAdmin):
    list_display =('trainer_name', 'phone', 'email',)

class EventAdmin(admin.ModelAdmin):
    list_display =('event_name', 'date','class_duration', 'seats', 'is_published')
    list_editable = ('is_published',)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display =('event', 'name', 'phone', 'email')


admin.site.register(Branche, BrancheAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)






