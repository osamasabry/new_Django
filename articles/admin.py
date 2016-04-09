from django.contrib import admin
from .models import *
from articles.models import User_profile  
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .forms import ArticleForm
# Register your models here.

admin.site.register(Comment)

# from .models import Employee
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton

#-------------------------------------------------------------------
class User_profileInline(admin.StackedInline):
    model = User_profile
    can_delete = False
    verbose_name_plural = 'user_profile'
#-------------------------------------------------------------------
# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (User_profileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#----------------------------------------------------------------
class ArticleAdmin(admin.ModelAdmin):
	list_display = ["art_title","art_content"]
	form = ArticleForm


# admin.site.unregister(Article)
admin.site.register(Article, ArticleAdmin)
#---------------------------------------------------------------------------







#-------------------------------------------------------------------

# from django.contrib import admin
# from .models import *
# # Register your models here.
# admin.site.register(User_profile)
# admin.site.register(Article)
# admin.site.register(keywords)
# admin.site.register(Comment)
# admin.site.register(Banwords)
# admin.site.register(Emotions)



