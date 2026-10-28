from django.db import models

# ==========================================
class Person(models.Model):

    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    national_id = models.CharField(max_length=10, unique=True, verbose_name="کد ملی")
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="ایمیل")
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True, verbose_name="شماره تماس")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Teacher(models.Model):
    """FUAD01: ثبت استاد جدید - FUAD02: غیرفعال کردن استاد"""
    teacher_id = models.AutoField(primary_key=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name="شخص")
    teacher_code = models.CharField(max_length=20, unique=True, verbose_name="کد استاد")
    department = models.CharField(max_length=100, verbose_name="گروه آموزشی")
    is_active = models.BooleanField(default=True, verbose_name="فعال (غیرفعال کردن بدون حذف فیزیکی)")
    hire_date = models.DateField(null=True, blank=True, verbose_name="تاریخ استخدام")

    def __str__(self):
        return self.teacher_code

class Student(models.Model):
    """FUAD03: ثبت دانشجو - FUAD04: ویرایش - FUAD05: غیرفعال کردن - FUAD06: جستجو"""
    student_id = models.AutoField(primary_key=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name="شخص")
    student_code = models.CharField(max_length=20, unique=True, verbose_name="شماره دانشجویی")
    educational_level = models.CharField(max_length=30, verbose_name="مقطع تحصیلی")
    field_of_study = models.CharField(max_length=100, verbose_name="رشته تحصیلی")
    application_date = models.DateField(verbose_name="تاریخ شروع تحصیل")
    status = models.CharField(max_length=20, verbose_name="وضعیت تحصیلی")
    is_active = models.BooleanField(default=True, verbose_name="فعال (غیرفعال کردن بدون حذف فیزیکی)")

    def __str__(self):
        return self.student_code

# ==========================================
