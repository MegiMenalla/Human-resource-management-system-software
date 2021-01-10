# Human-resource-management-system-software

http://127.0.0.1:8000/emp/hr/ --> on the left sidebar, first five links are functional (half functional).

http://127.0.0.1:8000/emp/manage_employees/ --> creates an employee, a User account and assigns a role (adds a record to the user role table)

http://127.0.0.1:8000/emp/manager_page/# --> on the left sidebar, first two links are functional.

#### To create a user: http://127.0.0.1:8000/emp/manage_employees/ 
#### To login: username: email, password: last_name

##### To create a request(as a manager or as an employee) use the coloured column. You can try to add a start date after the enddate or a start hour after the end hour(if both dates are the same), neither case will add the request to the db.

#### To deny or approve a request(both from the manager and hr page): http://127.0.0.1:8000/emp/see_answer_requests/ 

#### If you try to cancel a request that starts less than 48 from now, the record wont be deleted. 

# To login as a human resources employee--> username: 'megi@gmail.com', password: 'Menalla' -->From here you can actually create othe users.
# To login as a manager--> username: 'emma@gmail.com', password: 'Thiemig'
# To login as an employee--> username: 'elvis@gmail.com', password: 'Presley'
