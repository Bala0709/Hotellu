from django.contrib import admin
'''
# Register your models here.
from hotellu_app.models import AccessRecord, Topic, WebPage
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
'''

from hotellu_app.models import UserProfileInfo#,User

# admin.site.register(User)
admin.site.register(UserProfileInfo)
