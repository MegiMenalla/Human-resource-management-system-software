# Human-resource-management-system-software

### Relational db: 

https://drive.google.com/file/d/1poR8iux6fUGAGfSnLDORtFzWMaIR7eex/view?usp=sharing

-----

### Prerequisites:

After creating a superuser(assign him a valid email address), user the admin panel to:
  1. Create 3 roles on the Role table in this specific order: id-1: Human resources,id-2: Manager,id-3: Employee
  2. Create a department 
  3. Create a record on the Users table
  4. Assign a role to this user on UserRole table
  
-----

#### Each one of the 3 possible roles, Human Resources/Manager/Employee, has its own interface.

To login use this link: http://127.0.0.1:8000/emp/logini/

If the user you want to log in with is superuser:

    Username & password are the same as the superusers username and password.
    
If the user you want to log in with is created from the Manage Employees form in the human resources page:

    Username: 'your email address' 
    
    Password: 'your last name'
    
-----

Maximum number of times you can add the wrong password is 3.

In this case, you will be sent a random 10 digits code in your email address. Use that code as your password to log in and than change it in  the 'change password' page.

This proccess can also be done from the HR's page where the HR, knowing your email, can send you a link which will direct you to reseting your password.

-----

### After login:

#### If the user is from human resources:
##### The left side links:

  1. Manage departments: http://127.0.0.1:8000/emp/manage_departments/  ---> creates, reads, updates, deletes, exports as excel department records.
  
  2. Manage employees: http://127.0.0.1:8000/emp/manage_employees/  ---> creates, reads, updates, deletes, exports as excel Users records.
  
  2.1 Deleted user: http://127.0.0.1:8000/emp/deleted_users/ ---> reads  the deleted users and offers a way to undo the deletion.
  
  3. Manage Holidays: http://127.0.0.1:8000/emp/manage_holidays/ ---> creates, reads, updates, deletes Offical Holidays records.
  
  4. Manage job position: http://127.0.0.1:8000/emp/manage_jobs/ ---> create add a role to an existing user.
  
  5.Requests from managers: http://127.0.0.1:8000/emp/see_answer_requests/ ---> views requests in two sectors: 'checked' requests which have been approved or denied and 'for         approval' requests which are to be checkeb by a human resources employee eventually. These are only requests that are made by manager users.
  
    If the request dates overlap with another approved request of this same user, the request will be automatically denied and associated with a predeclared reason.
  
    If the user has not enough days left, the request will be automatically denied and associated with a predeclared reason.
  
  6.Change a users password : http://127.0.0.1:8000/emp/reset_password/ ---> by entering a users email, the HR sends him a link to reset his/her password.
  
  7. Change password: http://127.0.0.1:8000/emp/change_password/
 
All the buttons in th middle export reports in excel format.

------

#### If the user is a manager:

##### The left side links:

  1. Manage departments: http://127.0.0.1:8000/emp/manage_departments/  ---> creates, reads, updates, deletes, exports as excel department records.
  
  2. Employee requests: http://127.0.0.1:8000/emp/see_answer_requests/ ---> views requests in two sectors: 'checked' requests which have been approved or denied and 'for           approval' requests which are to be checked by a human resources employee eventually. These are requests from users of the same department as the manager.
  
  If the request dates overlap with another approved request of this same user, the request will be automatically denied and associated with a predeclared reason.
  
  If the user has not enough days left, the request will be automatically denied and associated with a predeclared reason.
  
#### The middle section contains two tables of the logged in users requests. 

* The requests that have been checked and approved can only be deleted more than 48 hours earlier that the start date.

* The requests that have not yet been checked can be canceled at any time.

#### The right side contains a form to create a request

* To  create an hourly request set the start and end date as the same date.

* If the request contains : 

        - a start date before an end date
        - a start date smaller than todays date
        - a start hour after the end hour (if start date== end date)
        
  the request will not be created.
  
 
-------

#### If the user is an employee:

##### The left side links:

 * General information about the employee.
  
#### The middle section contains two tables of the logged in users requests. 

* The requests that have been checked and approved can only be deleted more than 48 hours earlier that the start date.

* The requests that have not yet been checked can be canceled at any time.

#### The right side contains a form to create a request

* To  create an hourly request set the start and end date as the same date.

* If the request contains : 
        - a start date before an end date
        - a start date smaller than todays date
        - a start hour after the end hour (if start date== end date)
  the request will not be created.
 

