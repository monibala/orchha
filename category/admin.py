from django.contrib import admin

# Register your models here.
from django.contrib import admin
from category.models import Brands, Category, SubCategory, SubSubCategory
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SubSubCategory)
admin.site.register(Brands)