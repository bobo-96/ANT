from django.urls import path

from courses.views import CategoryView, SubCategoryView, SubCategoryWithCoursesView, CourseView, CommentView, \
    CategoryWithSubcategoryView, LessonView, HomeworkView, StudentsHomeworksView, CourseAccessView

urlpatterns = [
    # path('', CourseView.as_view({'get': 'list'})),
    path('course/create', CourseView.as_view({'post': 'create'})),
    path('course/<int:pk>', CourseView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('course/', CourseView.as_view({'get': 'list'})),
    path('courseaccess/create', CourseAccessView.as_view({'post': 'create'})),
    path('courseaccess/<int:pk>', CourseAccessView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('lesson/create', LessonView.as_view({'post': 'create'})),
    path('lessons/', LessonView.as_view({'get': 'list'})),
    path('lesson/<int:pk>', LessonView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('homework/create', HomeworkView.as_view({'post': 'create'})),
    path('homeworks/', HomeworkView.as_view({'get': 'list'})),
    path('homework/<int:pk>', HomeworkView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('studenthomework/create', StudentsHomeworksView.as_view({'post': 'create'})),
    path('studentshomeworks/', StudentsHomeworksView.as_view({'get': 'list'})),
    path('studenthomework/<int:pk>', StudentsHomeworksView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('category/', CategoryView.as_view({'get': 'list'})),
    path('category/<int:pk>', CategoryView.as_view({'get': 'retrieve'})),
    path('category_subcategory/<int:pk>', CategoryWithSubcategoryView.as_view({'get': 'retrieve'})),
    path('subcategory_courses/<int:pk>', SubCategoryWithCoursesView.as_view({'get': 'retrieve'})),
    path('subcategory/', SubCategoryView.as_view({'get': 'list'})),
    path('comment/create', CommentView.as_view({'post': 'create'})),
]