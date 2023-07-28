from django.contrib import admin
from .models import user,doctor,patient,appointment,invoice,prescription,routinecheckup,questionnairefacility,answer,requestequipment,reporting,feedback,promo
# Register your models here.
admin.site.register(user)
admin.site.register(doctor)
admin.site.register(patient)
admin.site.register(appointment)
admin.site.register(invoice)
admin.site.register(prescription)
admin.site.register(routinecheckup)
admin.site.register(questionnairefacility)
admin.site.register(answer)
admin.site.register(requestequipment)
admin.site.register(reporting)
admin.site.register(feedback)
admin.site.register(promo)


