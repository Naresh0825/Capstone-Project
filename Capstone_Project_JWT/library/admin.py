from django.contrib import admin
from .models import User,Book,Borrow

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','address','phone','gender']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "isbn", "available_copies")

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "borrow_date", "return_date", "returned")
