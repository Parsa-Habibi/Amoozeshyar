from django.db import models
from django.contrib.auth.models import AbstractUser


# شخص (جایگزین User پیش‌فرض جنگو)
class Person(AbstractUser):
    gender = models.CharField(
        max_length=1,
        choices=[
            ("F", "Female"),
            ("M", "Male"),
        ],
    )
    address = models.TextField()
    email = models.EmailField(unique=True)
    father_name = models.CharField(max_length=100)
    birth_place = models.CharField(max_length=100)


# استاد
class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, related_name="teacher"
    )
    teacher_code = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey("Department", on_delete=models.PROTECT)
    academic_rank = models.CharField(max_length=100)
    hire_date = models.DateField()


# دانشجو
class Student(models.Model):
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, related_name="student"
    )
    admission_type = models.CharField(max_length=100)
    previous_term_gpa = models.DecimalField(max_digits=4, decimal_places=2)
    total_gpa = models.DecimalField(max_digits=4, decimal_places=2)
    passed_units = models.IntegerField()
    tuition_debt = models.DecimalField(max_digits=12, decimal_places=2)


# درس
class Lesson(models.Model):

    pass


# ترم
class Term(models.Model):
    id = models.BigAutoField(primary_key=True)
    term_code = models.CharField(max_length=20, unique=True)
    semester = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    registration_start = models.DateTimeField()
    registration_end = models.DateTimeField()
    add_drop_start = models.DateTimeField()
    add_drop_end = models.DateTimeField()
    emergency_drop_start = models.DateTimeField()
    emergency_drop_end = models.DateTimeField()
    is_active = models.BooleanField(default=False)


# پرداخت
class Payment(models.Model):
    pass


# امتحان
class Exam(models.Model):
    pass


# گروه کلاسی
class LessonGroups(models.Model):
    pass


# مجوزهای پارکینگ
class ParkingPasses(models.Model):
    pass


# نقش
class Role(models.Model):
    pass


# حساب کاربری
class UserAccount(models.Model):
    pass


# دانشکده
class Faculty(models.Model):
    pass


# گروه آموزشی
class Department(models.Model):
    pass


# رشته
class Field(models.Model):
    pass


# پیش‌نیاز/هم‌نیاز
class Prerequisite(models.Model):
    pass


# کلاس/مکان
class Classroom(models.Model):
    pass


# اعضای گروه کلاسی
class LessonGroupMember(models.Model):
    pass


# ارائه درس در ترم
class CourseOffering(models.Model):
    pass


# انتخاب واحد
class Enrollment(models.Model):
    pass


# نمره
class Grade(models.Model):
    pass


# اعتراض به نمره
class GradeAppeal(models.Model):
    pass


# حضور و غیاب
class Attendance(models.Model):
    pass


# تیکت
class Ticket(models.Model):
    pass


# دسته بندی تیکت ها
class TicketCategory(models.Model):
    pass


# برگزاری کلاس مجازی
class OnlineClass(models.Model):
    pass


# رسید شهریه
class TuitionReceipt(models.Model):
    pass


# درخواست بازپرداخت وجه
class RefundRequest(models.Model):
    pass


# اعلان
class Notification(models.Model):
    pass


# نظرسنجی از معلم
class TeacherSurvey(models.Model):
    pass


# کارآموزی
class Internship(models.Model):
    pass


# امانت کتابخانه
class LibraryLoan(models.Model):
    pass


# رویداد
class Event(models.Model):
    pass


# خوابگاه
class Dormitory(models.Model):
    pass


# کتاب
class Book(models.Model):
    pass


# درخواست خدمات دانشجویی
class StudentServiceRequest(models.Model):
    pass


# درخواست بورسیه
class ScholarshipApplication(models.Model):
    pass


# جلسات مشاوره
class CounselingAppointment(models.Model):
    pass


# پروپوزال
class Proposal(models.Model):
    pass
