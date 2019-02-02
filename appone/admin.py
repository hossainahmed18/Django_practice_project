from django.contrib import admin
from .models import UserProfile,article


class UserModel(admin.ModelAdmin):
    list_display = ["__str__"]

    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserModel)


class authorModel(admin.ModelAdmin):
    list_display = ["__str__", "title"]

    class Meta:
        model = article


admin.site.register(article, authorModel)