from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import CustomUserForm
from teacher_panel.models import Teacher, Student
from general.models import Zone, District, School
from datetime import datetime
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login/')
def teacher_index(request):
    students = Student.objects.filter(user_id = request.user.id).first()
    teachers = Teacher.objects.filter(user_id = request.user.id).first()
    if not students and not teachers:
        context = {
            "title": "Warning!!!",
            "description": "Sorry You can't access this page",
            "icon": ""
        }
        return render(request, 'general/verify.html', context)
    if not teachers:
        return redirect('student_page')
    context = {
        "teacher": teachers
    }
    return render(request, 'teacher/dashboard.html', context)

@login_required(login_url='/login/')
def student_page(request):
    students = Student.objects.filter(user_id = request.user.id)
    teachers = Teacher.objects.filter(user_id = request.user.id)
    if not students and not teachers:
        context = {
            "title": "Warning!!!",
            "description": "Sorry You can't access this page",
            "icon": ""
        }
        return render(request, 'general/verify.html', context)
    if not students:
        return redirect('teacher_index')
    return render(request, 'student/dashboard.html')

@login_required(login_url='/login/')
def manage_student(request):
    return render(request, 'teacher/manageStudent.html')

@login_required(login_url='/login/')
def student_create(request):
    teachers = Teacher.objects.filter(user_id = request.user.id)

    if not teachers:
        context = {
            "title": "Warning!!!",
            "description": "Sorry You can't access this page",
            "icon": ""
        }
        return render(request, 'general/verify.html', context)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        gender = request.POST.get('sex')
        avatar = request.FILES.get('picture')
        date_string = request.POST.get('dob')
        date_of_birth = datetime.strptime(date_string, '%Y-%m-%d').date()

        teacher = teachers.first()
        student = Student(teacher_id = teacher.id, full_name = full_name, email = email, gender=gender, avatar=avatar, date_of_birth=date_of_birth)
        student.save()
        messages.success(request, f'successfully registered {full_name}')
        return redirect('/')

    return render(request, 'general/student_register.html')

def register(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return redirect('/')
    redirect_link = request.GET.get("next", None)
    if redirect_link is not None:
        request.session["redirect_link"] = redirect_link
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        full_name = request.POST.get('full_name')
        picture = request.FILES.get('picture')
        zone = request.POST.get('zone')
        district = request.POST.get('district')
        level = request.POST.get('level')
        school = request.POST.get('school')
        email = request.POST.get('email')
        teacher_obj = User.objects.filter(email = email)
        if teacher_obj:
            messages.success(
                request, 'An account with this email already existed')
            return redirect('registerPage')
        elif form.is_valid():
            user = form.save()
            zone_obj = Zone.objects.filter(name = zone).first()
            district_obj = District.objects.filter(name = district, zone = zone_obj).first()
            school_obj = School.objects.filter(name = school, zone = zone_obj, district = district_obj, school_level=level).first()
            teacher_obj = Teacher(user_id = user.id, school_id = school_obj.id, zone_id = zone_obj.id, district_id = district_obj.id)
            teacher_obj.name = full_name
            teacher_obj.profile_pics = picture
            teacher_obj.school_level = level
            teacher_obj.save()
            messages.success(
                request, 'registered successfully! login to continue')

            return redirect('/login/')
    context = {'form': form}
    return render(request, 'general/account/register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return redirect('/')
    else:
        if request.session.get("redirect_link"):
            redirect_link = request.session.get("redirect_link")
        else:
            redirect_link = request.GET.get("next", None)
            if redirect_link is not None:
                request.session["redirect_link"] = redirect_link
                redirect_link = request.session.get("redirect_link")
            else:
                redirect_link = "/"

        if request.method == 'POST':
            name = request.POST.get('username', None)
            passwd = request.POST.get('passwd', None)
            if name is not None and passwd is not None:
                user = authenticate(request, username=name, password=passwd)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in sucessfully')
                    return redirect(redirect_link)
                else:
                    messages.error(request, 'Invalid username or password')
                    return redirect('/login/')
        return render(request, 'general/account/login.html')


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'logged out successfully')
    return redirect('/')