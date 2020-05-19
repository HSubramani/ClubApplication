from django.contrib import admin
from .models import *
# Register your models here.
class AdminMemberView(admin.ModelAdmin):
    list_display=['username','password','name','regno','type','tackle']
class AdminTempMemberView(admin.ModelAdmin):
    list_display=['username','password','name','regno']
class AdminView(admin.ModelAdmin):
    list_display=['username','password']
class AdminTackleMemberView(admin.ModelAdmin):
    list_display=['username','regno','file']
class AdminFeedbackView(admin.ModelAdmin):
    list_display=['username','type','text','id','name']
class AdminTopscoresView(admin.ModelAdmin):
    list_display=["username","regno","score"]
class AdminMessageView(admin.ModelAdmin):
    list_display=["name","message"]
class AdminEventView(admin.ModelAdmin):
    list_display=["username","regno","slot","teamID","eventName"]
class AdminEvenCreatorView(admin.ModelAdmin):
    list_display=["eventName","description","team"]
class AdminFileView(admin.ModelAdmin):
    list_display=["name","file"]
admin.site.register(FileCSV,AdminFileView)
admin.site.register(Member,AdminMemberView)
admin.site.register(TempMember,AdminTempMemberView)
admin.site.register(Admin,AdminView)
admin.site.register(EventMember,AdminEventView)
admin.site.register(EventCreator,AdminEvenCreatorView)
admin.site.register(TackleMember,AdminTackleMemberView)
admin.site.register(Feedback,AdminFeedbackView)
admin.site.register(Message,AdminMessageView)
admin.site.register(Topscores,AdminTopscoresView)
