from django.urls import path
from .views import (LoginView, RegisterView, ProfileView,
                    Edit, user_update, delete_user,
                    add_users_save, add_users, LogoutView, GroupsView,
                    StudentListView, EditStudentView, DeleteStudentView,
                    StudentByTeamView, ResetPasswordView)

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit_profile/', Edit.as_view(), name='edit_profile'),
    path('teams/', GroupsView.as_view(), name='groups'),
    path('students/', StudentListView.as_view(), name='students'),
    path('student_by_team/<int:id>/', StudentByTeamView.as_view(), name='student_by_team'),
    path('edit_student/<int:id>/', EditStudentView.as_view(), name='edit_student'),
    path('delete_student/<int:id>/', DeleteStudentView.as_view(), name='delete_student'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),


    # ----------------------------------------------------------------
    # start CRUD urls
    path('update/<int:id>/', user_update, name='update'),
    path('delete/<int:id>/', delete_user, name='delete'),
    path('create_save/', add_users_save, name='create_save'),
    path('create/', add_users, name='create'),
    # end CRUD urls
    #----------------------------------------------------------------
]