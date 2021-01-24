# Human-resource-management-system-software

### Relational db: 
https://drive.google.com/file/d/1poR8iux6fUGAGfSnLDORtFzWMaIR7eex/view?usp=sharing

-----

###Prerequisites:

After creating a superuser(assign him a valid email address), user the admin panel to:
  1. Create 3 roles on the Role table in this specific order: id-1: Human resources,id-2: Manager,id-3: Employee
  2. Create a department 
  3. Create a record on the Users table
  
-----
####Each one of the 3 possible roles, Human Resources/Manager/Employee, has its own interface.

To login use this link: http://127.0.0.1:8000/emp/logini/

If the user you want to log in with is superuser:
    Username & password are the same as the superusers username and password.
    
If the user you want to log in with is created from the Manage Employees form in the human resources page:
    Username: 'your email address' 
    Password: 'your last name'
-----
Maximum number of times you can add the wrong password is 3.
In this case, you will be sent a random 10 digits code in your email address. Use that code as your password to log in and than change it in  the 'change password' page.
This proccess can also be done from the HR's page where th hr, knowing your email, can send you a link which will direct you to reseting your password.

-----

http://127.0.0.1:8000/emp/hr/ --> on the left sidebar, first five links are functional (half functional).

http://127.0.0.1:8000/emp/manage_employees/ --> creates an employee, a User account and assigns a role (adds a record to the user role table)

http://127.0.0.1:8000/emp/manager_page/# --> on the left sidebar, first two links are functional.

#### To create a user: http://127.0.0.1:8000/emp/manage_employees/ 
#### To login: username: email, password: last_name

##### To create a request(as a manager or as an employee) use the coloured column. You can try to add a start date after the enddate or a start hour after the end hour(if both dates are the same), neither case will add the request to the db.

#### To deny or approve a request(both from the manager and hr page): http://127.0.0.1:8000/emp/see_answer_requests/ 

#### If you try to cancel a request that starts less than 48 from now, the record wont be deleted. 

### To login as a human resources employee--> username: 'megi@gmail.com', password: 'Menalla' -->From here you can actually create othe users.
### To login as a manager--> username: 'emma@gmail.com', password: 'Thiemig'
### To login as an employee--> username: 'elvis@gmail.com', password: 'Presley'
