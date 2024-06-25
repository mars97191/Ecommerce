from django.contrib import admin

from .models import Category, Product, ProductType, AttributeValue, Attribute, ProductImage, ProductReview, Wishlist


# Инлайн категорий
class ChildCategoryInline(admin.TabularInline):
    model = Category
    fk_name = "parent"
    extra = 1


# Инлайн типа продукта
class ChildTypeInline(admin.TabularInline):
    model = ProductType
    fk_name = "parent"
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue


@admin.register(Attribute)
class AttributeValueAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ChildCategoryInline]
    list_display = ('id', 'name', 'parent_name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')

    def parent_name(self, obj):
        return obj.parent.name if obj.parent else None


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [ChildTypeInline, ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'category', 'stock_status', 'is_active')
    list_filter = ("stock_status", 'category', 'is_active')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, AttributeValueInline]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "rating", "review")


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user", "product")
