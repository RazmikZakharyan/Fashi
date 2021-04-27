from django.contrib import admin
from .models import \
    Product, Category, \
    Color, Collection, \
    Brand, Size, Tag, \
    ProductImage, Departments


class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    prepopulated_fields = {"slug":("title",)}


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at','photo')
    list_display_links = ('id', 'title')
    fields = ('title', 'slug', 'collection','availability', 'price',
              'description', 'size', 'color',
              'category', 'departments', 'brand', 'tags', 'image', 'photo', 'created_at', 'update'
    )
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['photo', 'created_at', 'update']
    save_as = True
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product


@admin.register(ProductImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Departments, BaseAdmin)
admin.site.register(Category, BaseAdmin)
admin.site.register(Color, BaseAdmin)
admin.site.register(Collection, BaseAdmin)
admin.site.register(Brand, BaseAdmin)
admin.site.register(Size, BaseAdmin)
admin.site.register(Tag, BaseAdmin)