from django.contrib import admin
from courses.models import Course, Category, Chapter, Subcategory, CourseAccess


class CourseMediaInline(admin.TabularInline):
    model = Chapter
    extra = 3


class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseMediaInline]
    readonly_fields = ('date',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Subcategory)
admin.site.register(Category)
admin.site.register(Chapter)
admin.site.register(CourseAccess)

