from django.contrib import admin
from blog.models import Category, Post
from account.models import MyUser


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','author','date','time']

    ordering = ('-date','-time')
    list_per_page = 10
    search_field = ('title')
        

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = MyUser.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

# Register your models here.
admin.site.register(Category)
admin.site.register(Post, PostAdmin)

