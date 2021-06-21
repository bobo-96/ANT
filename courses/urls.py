from django.urls import path

from courses.views import CategoryView, SubCategoryView, SubCategoryWithCoursesView, CourseView, CommentView

urlpatterns = [
    # path('', CourseView.as_view({'get': 'list'})),
    path('course/create', CourseView.as_view({'post': 'create'})),
    path('course/<int:pk>', CourseView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('course/', CourseView.as_view({'get': 'list'})),
    path('category/', CategoryView.as_view({'get': 'list'})),
    path('subcategory_courses/', SubCategoryWithCoursesView.as_view({'get': 'list'})),
    path('subcategory/', SubCategoryView.as_view({'get': 'list'})),
    path('comment/create', CommentView.as_view({'post': 'create'})),
]