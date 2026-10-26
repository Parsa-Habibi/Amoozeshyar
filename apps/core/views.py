from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/home.html'


from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, CourseOffering, Enrollment

@api_view(['POST'])
@transaction.atomic
def enroll_student(request):
    try:
        student_id = request.data.get('student_id')
        offering_id = request.data.get('offering_id')
        
        student = Student.objects.get(student_id=student_id)
        offering = CourseOffering.objects.get(offering_id=offering_id)
        
        if offering.remaining_capacity <= 0:
            return Response({"error": "ظرفیت کلاس تکمیل است"}, status=400)
            
        enrollment = Enrollment.objects.create(
            student=student,
            offering=offering,
            enrollment_status='تاییدشده'
        )
        
        offering.remaining_capacity -= 1
        offering.save()
        
        return Response({"message": "انتخاب واحد با موفقیت انجام شد"})
        
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
@transaction.atomic
def drop_course(request):
    try:
        enrollment_id = request.data.get('enrollment_id')
        enrollment = Enrollment.objects.get(enrollment_id=enrollment_id)
        
        enrollment.enrollment_status = 'لغوشده'
        enrollment.save()
        
        offering = enrollment.offering
        offering.remaining_capacity += 1
        offering.save()
        
        return Response({"message": "درس با موفقیت حذف شد"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
