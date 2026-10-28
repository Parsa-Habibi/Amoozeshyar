from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from .models import Person, Student, Teacher

class HomeView(TemplateView):
    template_name = 'core/home.html'


# ==========================================
# API های مربوط به Person (شخص)
# ==========================================
@api_view(['GET'])
def person_list(request):
    """دریافت لیست تمام اشخاص"""
    persons = Person.objects.all()
    data = [{"id": p.person_id, "first_name": p.first_name, "last_name": p.last_name} for p in persons]
    return Response({"message": "لیست اشخاص", "data": data})


# ==========================================
# API های مربوط به Student (دانشجو) - نیازمندی FUAD06 (جستجو)
# ==========================================
@api_view(['GET'])
def student_list(request):
    """دریافت لیست دانشجویان همراه با قابلیت جستجو"""
    search_query = request.query_params.get('search', None)
    
    if search_query:
        # جستجو بر اساس شماره دانشجویی یا نام شخص
        students = Student.objects.filter(
            student_code__icontains=search_query
        ) | Student.objects.filter(
            person__first_name__icontains=search_query
        )
    else:
        students = Student.objects.all()
        
    data = [{
        "student_code": s.student_code, 
        "name": f"{s.person.first_name} {s.person.last_name}",
        "status": s.status
    } for s in students]
    
    return Response({"message": "لیست دانشجویان", "data": data})


# ==========================================
# API های مربوط به Teacher (استاد)
# ==========================================
@api_view(['GET'])
def teacher_list(request):
    """دریافت لیست اساتید"""
    teachers = Teacher.objects.all()
    data = [{
        "teacher_code": t.teacher_code, 
        "name": f"{t.person.first_name} {t.person.last_name}",
        "department": t.department
    } for t in teachers]
    
    return Response({"message": "لیست اساتید", "data": data})


# ==========================================
# نمونه‌ای از نیازمندی‌های غیرعملیاتی (NFRP01 - تراکنشی بودن)
# ==========================================
@api_view(['POST'])
@transaction.atomic
def create_person_with_student(request):
    """
    ایجاد همزمان شخص و دانشجو به صورت تراکنشی.
    اگر در ساخت دانشجو خطایی رخ دهد، شخص هم ساخته نمی‌شود (Rollback).
    """
    try:
        # ۱. ساخت شخص
        person = Person.objects.create(
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            national_id=request.data.get('national_id')
        )
        
        # ۲. ساخت دانشجو
        student = Student.objects.create(
            person=person,
            student_code=request.data.get('student_code'),
            educational_level=request.data.get('educational_level', 'کارشناسی'),
            field_of_study=request.data.get('field_of_study', 'کامپیوتر'),
            application_date='2024-01-01',
            status='فعال'
        )
        
        return Response({"message": "شخص و دانشجو با موفقیت ساخته شدند"})
        
    except Exception as e:
        # در صورت بروز خطا، به دلیل @transaction.atomic، شخص هم پاک می‌شود
        return Response({"error": str(e)}, status=500)
