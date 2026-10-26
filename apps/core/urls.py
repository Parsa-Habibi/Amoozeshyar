from django.urls import path

from .views import HomeView, enroll_student, drop_course

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('enroll/', enroll_student, name='enroll_student'),
    path('drop/', drop_course, name='drop_course'),


]

