from django.contrib import admin
from .models import Article,Category,Comment_to_article,Comment_to_me,User_profile

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment_to_article)
admin.site.register(Comment_to_me)
admin.site.register(User_profile)