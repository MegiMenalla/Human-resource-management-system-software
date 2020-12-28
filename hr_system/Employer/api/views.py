from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from .serializers import *
from rest_framework.generics import *


class DepartmentView(generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


class CreateDepartmentView(APIView):
    serializer_class = CreateDepartmentSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            department_name = serializer.data.get('department_name')
            department_manager = serializer.data.get('department_manager')
            parent_dep = serializer.data.get('parent_dep')
            if parent_dep is not None and Departments.objects.get(department_name=parent_dep).exists():
                parent = Departments.objects.get(department_name=parent_dep)
            else:
                parent = None

            queryset = Departments.objects.filter(department_name=department_name)
            if queryset.exists():
                dep = queryset[0]
                dep.department_name = department_name
                dep.department_manager = department_manager
                dep.parent_dep = parent
                dep.save()

                return Response(CreateDepartmentSerializer(dep).data, status=status.HTTP_200_OK)
            else:
                if parent_dep is None:
                    dep = Departments(department_name=department_name,
                                      department_manager=department_manager)
                else:
                    dep = Departments(department_name=department_name,
                                      department_manager=department_manager,
                                      parent_dep=parent)
                dep.save()
                return Response(CreateDepartmentSerializer(dep).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


'''
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




class DepartmentsGenericAPI(generics.GenericAPIView
                            , mixins.ListModelMixin
                            , mixins.RetrieveModelMixin
                            , mixins.CreateModelMixin
                            , mixins.UpdateModelMixin
                            , mixins.DestroyModelMixin):
    serializer_class = DepartmentSerializer
    queryset = Departments.objects.all()
    lookup_field = 'id_department'
    lookup_url_kwarg = 'pk'
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

'''
