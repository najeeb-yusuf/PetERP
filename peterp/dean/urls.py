from django.urls import include,path
from . import views

app_name = 'dean'

urlpatterns = [
    path("",views.index,name='index'),
    path("logout/",views.logout_user,name='logout'),
    path("profile/",views.profile,name='profile'),
    path("semester_schedule/",views.semester_schedule,name='semester_schedule'),
    path("section_records/<int:section_id>",views.section_records,name='section_records'),
    path("course_overview/",views.course_overview,name='course_overview'),
    path("sections/",views.sections,name='sections'),
    path("courses/",views.courses,name='courses'),
    path("overrides/",views.overrides,name='overrides'),
    path("overloads/",views.overloads,name='overloads'),
    path("allocate_grades/",views.allocate_grades,name='allocate_grades'),
    path("change_grade/<int:enrollment_id>/<str:new_grade>",views.change_grade,name='change_grade'),
    path("grade_history/",views.grade_history,name='grade_history'),
    path("override_action/<int:override_id>/<str:new_state>",views.override_action,name='override_action'),
    path("overload_action/<int:overload_id>/<str:new_state>",views.overload_action,name='overload_action'),
    path("assign_faculty",views.assign_faculty,name='assign_faculty'),
    path("assign/<int:section_id>/<str:faculty_id>",views.assign,name='assign'),
]