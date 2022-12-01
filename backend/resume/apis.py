from rest_framework import views
from rest_framework import response
from users import authentication
from rest_framework import permissions
from . import serializer as resume_serializer
from . import services
from rest_framework import status as rest_status
class ResumeCreateListApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = resume_serializer.ResumeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        serializer.instance = services.create_resume(user = request.user, resume=data)
        return response.Response(data=serializer.data)

    def get(self, request):
        resume_collection = services.get_user_resume(user=request.user)
        serializer = resume_serializer.ResumeSerializer(resume_collection, many=True)
        return response.Response(data=serializer.data)

class ResumeRetrieveUpdateDelete(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, resume_id):
        resume = services.get_user_resume_detail(resume_id=resume_id)
        serializer = resume_serializer.ResumeSerializer(resume)
        return response.Response(data=serializer.data)

    def delete(self, request, resume_id):
        services.delete_user_resume(user=request.user, resume_id=resume_id)
        return response.Response(resume=rest_status.HTTP_204_NO_CONTENT)

    def put(self, request, resume_id):
        serializer = resume_serializer.ResumeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resume = serializer.validated_data
        serializer.instance = services.update_user_resume(
            user=request.user, resume_id=resume_id, resume_data=resume
        )

        return response.Response(data=serializer.data)