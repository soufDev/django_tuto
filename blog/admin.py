from django.contrib import admin
from .models import Category, Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'category')
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title', ), }
    fieldsets = (
        ('General', {
            'classes': ['collapse'],
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('Article Content', {
            'description': 'The content accept html tags, use them wisely !',
            'fields': ('content', )
        })
    )

    def content_preview(self, article):
        """Return the first 40 chars of the content of the article,
        if it has more than 40 chars,
        it's necessary to add points of suspension """
        text = article.content[0:40]
        if len(article.content) > 40:
            return '%s...' % text
        else:
            return text

    content_preview.short_description = 'Content Preview'

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
