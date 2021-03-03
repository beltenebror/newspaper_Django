from django.contrib import admin
from . import models


class CommentInline(admin.StackedInline):  # new
    model = models.Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):      # new
    inlines = [
        CommentInline,
    ]


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
