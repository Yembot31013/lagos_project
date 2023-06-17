from django.urls import path
from . import views
from . import fetch
from . import add_to_db

urlpatterns = [
    path('', views.teacher_index, name="teacher_index"),
    path('competition/', views.student_page, name="student_page"),
    path('student_create/', views.student_create, name="student_create"),
    path('manage_student/', views.manage_student, name="manage_student"),
    path('import/', add_to_db.import_data, name="verifyPage"),
    path('login/', views.loginpage, name="loginPage"),
    path('register/', views.register, name="registerPage"),
    path('logout/', views.logoutpage, name="logoutPage"),
    path('get_local_government/', fetch.get_zone),
    path('get_district/', fetch.get_district),
    path('get_school/', fetch.get_school),
]
