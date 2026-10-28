from django.urls import path
from .views import HomeView, person_list, student_list, teacher_list, create_person_with_student

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('persons/', person_list, name='person_list'),
    path('students/', student_list, name='student_list'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('create-student/', create_person_with_student, name='create_student'),
]
