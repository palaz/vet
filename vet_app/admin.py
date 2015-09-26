from django.contrib import admin

# Register your models here.
from vet_app.models import Category, Page


class PageInLine(admin.StackedInline):
    model = Page
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nome', {'fields': ['name']}),
        ('Sezione', {'fields': ['is_vet']}),
    ]
    list_display = ('name', 'is_vet', 'slug')
    inlines = [PageInLine]


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Categoria', {'fields': ['category']}),
        ('Contenuto', {'fields': ['name', 'text']})
    ]
    list_display = ('name', 'category', 'slug')

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)