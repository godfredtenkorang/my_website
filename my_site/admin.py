from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Services)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Youtube, AdminVideo)
admin.site.register(Portfolio)
admin.site.register(Post)