from django.contrib import admin
from home.models import Book
from home.models import Person
#from home.models import Musician
#from home.models import Album
# Register your models here.
#admin.site.register(Book)
#admin.site.register(Person)
#admin.site.register(Musician)
#admin.site.register(Album)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields=('id','name')
   

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields=('id','first_name')
    list_filters=('first_name','last_name')
