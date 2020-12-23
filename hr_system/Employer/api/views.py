from django.shortcuts import render
from rest_framework import viewsets, permissions
from ..models import *
from .serializers import *


class DepartmentView(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserRoleView(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer


class OfficalHolidaysView(viewsets.ModelViewSet):
    queryset = OfficalHolidays.objects.all()
    serializer_class = OfficialHolidaysSerializer


class AllowanceRequestView(viewsets.ModelViewSet):
    queryset = AllowanceRequest.objects.all()
    serializer_class = RequestSerializer


class ProfilView(viewsets.ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer


'''

def test(request):
    return HttpResponse('hi')


class DepartmentsGenericAPI(generics.GenericAPIView
    , mixins.ListModelMixin
    , mixins.RetrieveModelMixin
    , mixins.CreateModelMixin
    , mixins.UpdateModelMixin
    , mixins.DestroyModelMixin):
    serializer_class = DepartmentSerializer
    queryset = Departments.objects.all()
    lookup_field = 'pk'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class DepartmentAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dep = Departments.objects.all()
        serializer = DepartmentSerializer(dep, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Departments.objects.get(id_department=id)
        except Departments.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        dep = self.get_object(id)
        serializer = DepartmentSerializer(dep)
        return Response(serializer.data)

    def put(self, request, id):
        dep = self.get_object(id)
        serializer = DepartmentSerializer(dep, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        dep = self.get_object(id)
        dep.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
