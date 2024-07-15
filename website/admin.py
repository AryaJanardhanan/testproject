from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)


#method
@admin.register(Userr)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'password')
    list_filter = ('email' ,'name')
    search_fields = ('email', 'name')

#method 2
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    
admin.site.register(Book,BookAdmin)


   
