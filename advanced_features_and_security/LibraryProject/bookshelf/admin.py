from .models import Book
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,CustomUser 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, User, CustomUserManager

# Import the User model
#CustomUser
class CustomUserAdmin(BaseUserAdmin):
    model= CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active','date_of_birth']
    fieldsets = BaseUserAdmin.fieldsets + (
        (None,{'fields':('date_of_birth','profile_photo')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None,{'fields':('date_of_birth','profile_photo')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Extra', {'fields': ('bio', 'profile_picture', 'followers')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(User, UserAdmin)
admin.ModelAdmin
list_filter = ('author', 'publication_year')
search_fields = ('title', 'author')
admin.site.register(Book)



# Register your models here.



