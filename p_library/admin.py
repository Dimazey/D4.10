from django.contrib import admin
from p_library.models import Book, Author, PublishingHouse

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_filter = ("title",)
    list_display = ('title', 'author_full_name')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price'  )
    
    pass 

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("full_name",)
    pass

@admin.register(PublishingHouse)
class PublisherAdmin(admin.ModelAdmin):
    pass

