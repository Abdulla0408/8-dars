from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import LoginForm, RegisterForm, Profile_Edit_Form, StudentEditForm, ResetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import AdminRequiredMixin
from .models import Student, Team, User
from django.db.models import Q


# ----------------------------------------------------------------------------------------------------------------------
# CRUD
def add_users(request):
    return render(request, 'create.html')


def add_users_save(request):
    if request.method == 'POST':
        save = request.POST
        student = Student()
        student.first_name = save['first_name']
        student.last_name = save['last_name']
        student.email = save['email']
        student.location = save['location']
        student.phone = save['phone']
        student.save()
        return redirect('/')
    return render(request, 'create.html')


def user_update(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        save = request.POST
        student.first_name = save['first_name']
        student.last_name = save['last_name']
        student.email = save['email']
        student.location = save['location']
        student.phone = save['phone']
        student.save()

        return redirect('/')
    return render(request, 'update.html', context={'student': student})


def delete_user(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('/')


# ----------------------------------------------------------------------------------------------------------------------
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


class RegisterView(AdminRequiredMixin, View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user.user_role == 'student':
                new_student = Student()
                new_student.user = user
                new_student.save()
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            return redirect('/')

        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html')


class Edit(LoginRequiredMixin, View):
    def get(self, request):
        form = Profile_Edit_Form(instance=request.user)
        return render(request, 'users/edit_profile.html', context={'form': form})

    def post(self, request):
        form = Profile_Edit_Form(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')

        form = Profile_Edit_Form(instance=request.user)
        return render(request, 'users/edit_profile.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class GroupsView(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, 'users/groups.html', {'teams': teams})


class StudentListView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            students = Student.objects.filter(
                Q(user__username__icontains=search_query) |
                Q(team__name__icontains=search_query) |  # Assuming `team` model has a `name` field
                Q(user__first_name__icontains=search_query) |
                Q(user__last_name__icontains=search_query)
            )
        else:
            students = Student.objects.all()
        return render(request, 'users/students.html', {'students': students})

class StudentByTeamView(AdminRequiredMixin,View):
    def get(self, request, id):
        team = get_object_or_404(Team, id=id)
        students = team.students.all()
        return render(request, 'users/groups.html', {'students': students})


class EditStudentView(AdminRequiredMixin, View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentEditForm(instance=student)
        return render(request, 'users/edit_student.html', {'form': form})

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users:students')
        else:
            return render(request, 'users/edit_student.html', {'form': form})


class DeleteStudentView(AdminRequiredMixin, View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        user = get_object_or_404(User, username=student.user.username)
        student.delete()
        user.delete()
        return redirect('users:students')


class ResetPasswordView(LoginRequiredMixin, View):
    def get(self, request):
        form = ResetPasswordForm()
        return render(request, 'users/reset_password.html', {'form': form})