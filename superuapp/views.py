from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from superuapp.models import Profile
from superuapp.serializers import ProfileAPiSerilizer
# Create your views here.


class ProfileApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileAPiSerilizer

    def get(self, request, id=None):
        '''
        get method is used to fetch the Profile object using id or fetch entire Profile object
        '''
        if id:
            try:
                profile_obj = Profile.objects.get(id=id)
            except Profile.DoesNotExist:
                return Response({'msg': "Id is incorrect. Please entered correct profile id", 'status code': 400}, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(profile_obj)
            return Response({'data': serializer.data, 'status code': 200}, status=status.HTTP_200_OK)

        profile_obj = Profile.objects.all()
        serializer = self.serializer_class(profile_obj, many=True)
        return Response({'data': serializer.data, 'status code': 200}, status=status.HTTP_200_OK)

    def post(self, request):
        '''
        post method is used to create new profile object
        '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 'user': str(request.user)
            # 'auth': str(request.auth)
            return Response({'msg': "Successfully create profile ", 'data': serializer.data, 'status':201}, status=status.HTTP_201_CREATED)
        return Response({'msg':"Failed to create SuperU Profile", 'data':serializer.errors, 'status code': 400}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id=None):
        '''
        patch method is used to update the Profile
        '''
        try:
            profile_obj = Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            return Response({'msg': "Id is incorrect. Please entered correct profile id", 'status code': 400}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(profile_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Successfully update SuperU profile ", 'data': serializer.data, 'status':201}, status=status.HTTP_201_CREATED)
        return Response({'msg':"Failed to update SuperU Profile", 'data':serializer.errors, 'status code': 400}, status=status.HTTP_400_BAD_REQUEST)

