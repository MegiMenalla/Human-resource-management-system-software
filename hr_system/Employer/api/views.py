import datetime
from rest_framework import viewsets, permissions, generics, status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *


# list create for Departments
class DepartmentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


# get, update delete one specific department
class DepartmentRetrieveDeletePut(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


# list create for Holiday dates
class HolidayListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = OfficalHolidays.objects.all()
    serializer_class = HolidaySerializer


# get, update delete one specific holiday
class HolidayRetrieveDeletePut(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = OfficalHolidays.objects.all()
    serializer_class = HolidaySerializer


# list create for days left
class UserHolidayListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserHoliday.objects.all()
    serializer_class = UserHolidaySerializer

    def create(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated]
        serializer = UserHolidaySerializer(data=request.data)
        if serializer.is_valid():
            x = serializer.data.get('days_left')  # actually get the role
            r = Role.objects.get(id=x)
            y = Users.objects.last()
            us_days = UserHoliday(us=y, days_left=r.max_allowance_no)
            us_days.save()
            return Response(UserHolidaySerializer(us_days).data, status=status.HTTP_200_OK)


# get, update delete days left
class UserHolidayRetrieveDeletePut(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserHoliday.objects.all()
    serializer_class = UserHolidaySerializer


# list create for employees
class UsersListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            fname = serializer.data.get('first_name')
            lname = serializer.data.get('last_name')
            sal = serializer.data.get('salary')
            phone = serializer.data.get('phone_no')
            hire_date = serializer.data.get('hire_date')
            email = serializer.data.get('email')
            dep = serializer.data.get('department_id')
            dep = Departments.objects.get(id=dep)

            user_acc = User(username=email)
            user_acc.set_password(lname)
            user_acc.save()
            user1 = Users(first_name=fname, last_name=lname,
                          salary=sal, phone_no=phone, hire_date=hire_date,
                          department_id=dep, email=email, user=user_acc)
            user1.id = user_acc.id
            user1.save()

            return Response(UserSerializer(user1).data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# get, update delete one specific employee
class UsersRetrieveDeletePutView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    # activate user
    def put(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = self.get_object()
            user.active = True
            user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response(UserSerializer.data, status=status.HTTP_400_BAD_REQUEST)

    # apply soft delete
    def delete(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_object()
            user.active = False
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# list requests that are not checked yet
class RequestList(generics.ListAPIView):
    queryset = AllowanceRequest.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):

        queryset = AllowanceRequest.objects.all()
        serializer = RequestSerializer(queryset, many=True)
        me = request.user.id
        dep = Users.objects.get(id=me)
        dep = dep.department_id.id
        # check the users role
        role = UserRole.objects.filter(user=me)
        ids = [i.role.id for i in role]
        id = min(ids)
        requesters = []
        # if user is HR --> he will see only managers requests
        if id == 1:
            managers = UserRole.objects.filter(role=2)
            for i in managers:
                requesters.append(i.user.id)
                requesters = [i for i in requesters if i != me]

        # if user is manager he'll see only its emps requests
        elif id == 2:
            employees = UserRole.objects.filter(role=3)
            empr = [i.user.id for i in employees]
            emp = Users.objects.filter(id__in=empr, department_id=dep)
            requesters = [e.id for e in emp if e.id != me]

        allreq = AllowanceRequest.objects.filter(user_id__in=requesters)
        # print(allreq)
        serializer = RequestSerializer(allreq, many=True)
        return Response(serializer.data)


# list create requests
class RequestListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AllowanceRequest.objects.all()
    serializer_class = RequestSerializer


# get, update delete one specific request
class RequestRetrieveDeletePutView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AllowanceRequest.objects.all()
    serializer_class = RequestSerializer

    def put(self, request, *args, **kwargs):
        serializer = RequestSerializer(data=request.data)

        if serializer.is_valid():
            checked = serializer.data.get('checked')
            approval_flag = serializer.data.get('approval_flag')
            description = serializer.data.get('description')
            req = self.get_object()

            # check for overlapping requests
            this_users_req = AllowanceRequest.objects.filter(user_id=req.user_id.id, approval_flag=True)
            for i in this_users_req:
                if i.start_date != i.end_date:
                    if i.start_date <= req.start_date <= i.end_date or i.start_date <= req.end_date <= i.end_date:
                        approval_flag = False
                        description = 'Overlapping request!'
                else:
                    if i.start_hour <= req.start_hour <= i.end_hour or i.start_hour <= req.end_hour <= i.end_hour:
                        approval_flag = False
                        description = 'Overlapping requests!'

            # check if offic holiday and subtract
            if approval_flag:
                who = req.user_id.id
                userleft = UserHoliday.objects.get(us=who)
                left = userleft.days_left
                start_date = req.start_date
                end_date = req.end_date
                tmp = 0
                # check for holidays
                allholidays = OfficalHolidays.objects.all()
                for i in allholidays:
                    if i.active_flag:
                        if start_date < i.day <= end_date:
                            tmp += 1

                dif_h = None
                if start_date == end_date:
                    start_hour = req.start_hour
                    end_hour = req.end_hour
                    dif_h = end_hour.hour - start_hour.hour
                dif = end_date - start_date

                # check if enough days left
                if (left - dif.days) < 0:
                    approval_flag = False
                    description = 'Not enough days left!'
                else:
                    if dif_h is None:
                        dif = dif.days
                        left = left - dif
                        left += tmp
                    else:
                        left = left * 24
                        left = left - dif_h
                        left = left / 24
                        left += tmp
                    userleft.days_left = left
                    userleft.save()

            appr = Users.objects.get(id=request.user.id)
            req.approver = appr
            req.checked = checked
            req.approval_flag = approval_flag
            req.description = description
            req.save()
            return Response(RequestSerializer(req).data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            req = self.get_object()
            # add back the subtracted days if th request was approved
            if req.checked:
                if req.approval_flag:
                    who = req.user_id.id
                    userholidays = UserHoliday.objects.get(us=who)
                    left = userholidays.days_left
                    start_date = req.start_date
                    end_date = req.end_date
                    tmp = 0
                    # check for holidays
                    allholidays = OfficalHolidays.objects.all()
                    for i in allholidays:
                        if i.active_flag:
                            if start_date < i.day <= end_date:
                                tmp += 1

                    dif_h = None
                    if start_date == end_date:
                        start_hour = req.start_hour
                        end_hour = req.end_hour
                        dif_h = end_hour.hour - start_hour.hour
                    dif = end_date - start_date
                    if dif_h is None:
                        dif = dif.days
                        left = left + dif
                        left -= tmp
                    else:
                        left = left * 24
                        left = left + dif_h
                        left = left / 24
                        left -= tmp
                    userholidays.days_left = left
                    userholidays.save()

            req.delete()
            print('deleted')
            return self.destroy(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# list create roles
class RoleListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# get, update delete one specific role
class RoleRetrieveDeletePutView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# list create user-role-relationship
class UserRoleListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            current_time = datetime.date.today()
            r = serializer.data.get('role')
            s = datetime.date.today()
            u = Users.objects.all().last()
            life = Role.objects.get(id=r)
            l = datetime.date(current_time.year + life.lifespan, 1, 1)
            r = Role.objects.get(id=r)
            user_role = UserRole(user=u, role=r, start_date=s, end_date=l)
            user_role.save()

            return Response(UserRoleSerializer(user_role).data, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# get, update delete one specific role
class UserRoleViewRetrieveDeletePutView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [IsAuthenticated]
