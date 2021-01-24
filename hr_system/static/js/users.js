function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

buildList()
// list
function buildList(){
    var wrapper = document.getElementById('wrapper') // <select>
    wrapper.innerHTML = ''
    var listt = document.getElementById('listt')
    listt.innerHTML = ''
    var rl = document.getElementById('roles')
    rl.innerHTML = ''


    // list the departments
    var urldep = 'http://127.0.0.1:8000/api/departments/'
    fetch(urldep)
    .then((resp)=> resp.json())
    .then(function(data){
        //console.log('Data:', data)
        data.forEach((el) => {
            var item = `<option  value="${el.id}" >${el.department_name}</option >`
            wrapper.innerHTML +=item
         })
    })



    // list the roles
    var urlr = 'http://127.0.0.1:8000/api/roles/'
    fetch(urlr)
    .then((resp)=> resp.json())
    .then(function(data){
        //console.log('Data:', data)
        data.forEach((el) => {
            var itemr = `<option  value="${el.id}" >${el.role}</option >`
            rl.innerHTML +=itemr
         })

    })



    // list the employees
    var url = 'http://127.0.0.1:8000/api/users/'
    fetch(url)
    .then((resp)=> resp.json())
    .then(function(data){
        console.log('Data:', data)

        data.forEach((el) => {
            if (el.active==true){
                 var item1 = `<li  id="${el.id}" class="mb-3 " >
                          <button  class="btn btn-sm  btn-outline-dark pt-0 pb-0 mr-3" onclick="getUser(${el.id})">Edit</button>
                          <button class="btn btn-sm  btn-outline-danger pt-0 pb-0 mr-3" onclick="deleteUser(${el.id})">X</button>
                          <strong>  ${el.first_name} ${el.last_name}</strong></li>`
                listt.innerHTML +=item1
            }
         })
    })
}





// get one user
var id = null;
function getUser(user){
    var url = `http://127.0.0.1:8000/api/users/${user}/`

        fetch( url, {
            method: 'GET',
            headers:{'Content-type' : 'application/json',
            'X-CSRFToken': csrftoken
            }
            }).then((resp)=> resp.json())
            .then(function(response){

            //console.log(response.department_id)
                reset()
                document.getElementById('name').value = response.first_name
                document.getElementById('surname').value = response.last_name
                document.getElementById('salary').value = response.salary
                document.getElementById('phone').value = response.phone_no
                document.getElementById('hire_date').value = response.hire_date
                document.getElementById('email').value = response.email
                document.getElementById('wrapper').value = response.department_id
                id = response.id
                })
    }



function reset(){
 document.getElementById('form-wrapper').reset()

}


// create a user if he/she doesn't already exists
var form = document.getElementById('form-wrapper')
form.addEventListener('submit', function(e){
    e.preventDefault();
    //console.log('submitted')
    if (id!=null){
        putUser(id);
        id=null;
    }
    else{
        var url = `http://127.0.0.1:8000/api/users/`
        var name = document.getElementById('name').value;
        var surname = document.getElementById('surname').value;
        var salary = document.getElementById('salary').value;
        var phone_no = document.getElementById('phone').value;
        var hire_date = document.getElementById('hire_date').value;
        var email = document.getElementById('email').value;
        var selector = document.getElementById('wrapper');
        var dep = selector[selector.selectedIndex].value;
        var selector2 = document.getElementById('roles');
        var role = selector2[selector2.selectedIndex].value;


        // create a record on users table
        fetch(url, {
            method : 'POST',
             headers:{'Content-type' : 'application/json',
                     'X-CSRFToken': csrftoken
            },
            body : JSON.stringify({
                'first_name':name,
                'last_name':surname,
                'salary':salary,
                'phone_no': phone_no,
                'hire_date':hire_date,
                'email':email,
                'department_id':dep
            })
        }).then(function(response){
            buildList();
            reset();
        })

        alert('User was created. Click ok to assign him/her the job position.')
        // create a record on user-roles table
        var url1 = `http://127.0.0.1:8000/api/user_role/`
        fetch(url1, {
            method : 'POST',
             headers:{'Content-type' : 'application/json',
                     'X-CSRFToken': csrftoken
            },
            body : JSON.stringify({
                'role':role
            })
        })

        alert('Click OK to finish!')
        // create a record on user holidays table
        var url1 = `http://127.0.0.1:8000/api/user_holiday/`
        fetch(url1, {
            method : 'POST',
             headers:{'Content-type' : 'application/json',
                     'X-CSRFToken': csrftoken
            },
            body : JSON.stringify({
                'days_left':role
            })
        })

    }

})


// update a user
function  putUser(id){
    var url = `http://127.0.0.1:8000/api/users/${id}/`
    var name = document.getElementById('name').value;
    var surname = document.getElementById('surname').value;
    var salary = document.getElementById('salary').value;
    var phone_no = document.getElementById('phone').value;
    var hire_date = document.getElementById('hire_date').value;
    var email = document.getElementById('email').value;
    var selector = document.getElementById('wrapper');
    var dep = selector[selector.selectedIndex].value;
    fetch(url, {
            method : 'PUT',
             headers:{'Content-type' : 'application/json',
                     'X-CSRFToken': csrftoken
            },
            body : JSON.stringify({
                'first_name':name,
                'last_name':surname,
                'salary':salary,
                'phone_no': phone_no,
                'hire_date':hire_date,
                'email': email,
                'department_id':dep
            })
        }).then(function(response){
            buildList();
            reset();
        })
}


// delete
function deleteUser(id){
    console.log('clicked',id)
    var url = `http://127.0.0.1:8000/api/users/${id}/`


    fetch( url, {
        method: 'DELETE',
        headers:{'Content-type' : 'application/json',
        'X-CSRFToken': csrftoken
        }
        }).then(function(response){
            buildList()
            reset()
            })
}















