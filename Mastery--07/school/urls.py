from django.urls import path
from school.views import all_stu, single_stu
urlpatterns = [
    path('stu/', all_stu, name='all_data' ),
    path('sin/', single_stu, name='single_data' ),
]
