import dataclasses
import datetime
from users import services as user_service
from typing import TYPE_CHECKING
from . import models as resume_models
from django.shortcuts import get_object_or_404
from rest_framework import exceptions
if TYPE_CHECKING:
    from models import Resume
    from users.models import User

@dataclasses.dataclass
class ResumeDataClass:
    content: str
    date_published: datetime.datetime=None
    user: user_service.UserDataClass = None
    id: int = None

    @classmethod
    def from_instance(cls, resume_model: "Resume") -> "Resume":
        return cls(
            content = resume_model.content,
            date_published = resume_model.date_published,
            id=resume_model.id,
            user = resume_model.user
        )

def create_resume(user, resume: "ResumeDataClass") -> "ResumeDataClass":
    resume_create = resume_models.Resume.objects.create(
        content = resume.content,
        user = user
    )
    return ResumeDataClass.from_instance(resume_model=resume_create)

def get_user_resume(user: "User") -> list["ResumeDataClass"]:
    user_resume = resume_models.Resume.objects.filter(user=user)

    return [
        ResumeDataClass.from_instance(single_status) for single_status in user_resume
    ]

def get_user_resume_detail(resume_id: int) -> "ResumeDataClass":
    resume = get_object_or_404(resume_models.Resume, pk=resume_id)

    return ResumeDataClass.from_instance(resume_model=resume)


def delete_user_resume(user: "User", resume_id: int) -> "ResumeDataClass":
    resume = get_object_or_404(resume_models.Resume, pk=resume_id)
    if user.id != resume.user.id:
        raise exceptions.PermissionDenied("You're not the user fool")
    resume.delete()


def update_user_resume(user: "User", resume_id: int, resume_data: "ResumeDataClass"):
    resume = get_object_or_404(resume_models.Resume, pk=resume_id)
    if user.id != resume.user.id:
        raise exceptions.PermissionDenied("You're not the user fool")

    resume.content = resume_data.content
    resume.save()

    return ResumeDataClass.from_instance(resume_model=resume)