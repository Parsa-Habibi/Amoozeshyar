from django.db import models
from django.contrib.auth.models import AbstractUser


# شخص (جایگزین User پیش‌فرض جنگو)
class Person(AbstractUser):
    pass


# استاد
class Teacher(Person):
    pass


# دانشجو
class Student(Person):
    pass


# درس
class Lesson(models.Model):
    pass


# ترم
class Term(models.Model):
    pass


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

    tuition_receipt_key = models.AutoField(
        primary_key=True,
        db_column="TuitionReceiptKey"
    )
    receipt_serial_code = models.CharField(
        max_length=50,
        unique=True,
        db_column="ReceiptSerialCode"
    )
    receipt_payment_link = models.ForeignKey(
        "core.Payment",
        on_delete=models.PROTECT,
        related_name="tuition_receipts",
        db_column="ReceiptPaymentLinkId"
    )
    receipt_issued_on = models.DateTimeField(
        auto_now_add=True,
        db_column="ReceiptIssuedOn"
    )
    receipt_document_uri = models.CharField(
        max_length=500,
        blank=True,
        db_column="ReceiptDocumentUri"
    )

    class Meta:
        db_table = "TuitionReceipt"

    def __str__(self):
        return self.receipt_serial_code





# درخواست بازپرداخت وجه
class RefundRequest(models.Model):
    REFUND_STATUS_CHOICES = [
        ("pending", "در انتظار بررسی"),
        ("approved", "تأیید شده"),
        ("rejected", "رد شده"),
        ("paid", "بازپرداخت انجام شده"),
    ]

    refund_case_key = models.AutoField(
        primary_key=True,
        db_column="RefundCaseKey"
    )
    refund_payment_link = models.ForeignKey(
        "core.Payment",
        on_delete=models.PROTECT,
        related_name="refund_requests",
        db_column="RefundPaymentLinkId"
    )
    refund_value_requested = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        db_column="RefundValueRequested"
    )
    refund_justification_text = models.TextField(
        db_column="RefundJustificationText"
    )
    refund_review_state = models.CharField(
        max_length=20,
        choices=REFUND_STATUS_CHOICES,
        default="pending",
        db_column="RefundReviewState"
    )

    class Meta:
        db_table = "RefundRequest"

    def __str__(self):
        return f"درخواست بازپرداخت {self.refund_case_key}"





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
    REQUEST_KIND_CHOICES = [
        ("installment", "تقسیط بدهی"),
        ("withdrawal", "انصراف از تحصیل"),
    ]

    REQUEST_STATUS_CHOICES = [
        ("pending", "در انتظار بررسی"),
        ("approved", "تأیید شده"),
        ("rejected", "رد شده"),
    ]

    student_service_case_key = models.AutoField(
        primary_key=True,
        db_column="StudentServiceCaseKey"
    )
    service_requester = models.ForeignKey(
        "core.Student",
        on_delete=models.PROTECT,
        related_name="service_requests",
        db_column="ServiceRequesterLinkId"
    )
    service_request_kind = models.CharField(
        max_length=20,
        choices=REQUEST_KIND_CHOICES,
        db_column="ServiceRequestKind"
    )
    service_request_data = models.TextField(
        blank=True,
        db_column="ServiceRequestData"
    )
    service_decision_state = models.CharField(
        max_length=20,
        choices=REQUEST_STATUS_CHOICES,
        default="pending",
        db_column="ServiceDecisionState"
    )

    class Meta:
        db_table = "StudentServiceRequest"

    def __str__(self):
        return (
            f"درخواست {self.student_service_case_key} - "
            f"{self.get_service_request_kind_display()}"
        )



# درخواست بورسیه
class ScholarshipApplication(models.Model):
    pass


# جلسات مشاوره
class CounselingAppointment(models.Model):
    pass


# پروپوزال
class Proposal(models.Model):
    pass

