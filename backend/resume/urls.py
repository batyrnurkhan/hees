from django.urls import path
from . import apis

urlpatterns = [
    path('resume/', apis.ResumeCreateListApi.as_view(), name="status"),
     path(
        "resume/<int:resume_id>/",
        apis.ResumeRetrieveUpdateDelete.as_view(),
        name="status_detail",
    ),
]
