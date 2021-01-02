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
var activeItem = null;





buildList()
// list
function buildList(){
    var wrapper = document.getElementById('wrapper') // <select>
    wrapper.innerHTML = ''
    var listt = document.getElementById('listt')
    listt.innerHTML = ''


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



    // list the employees
    var url = 'http://127.0.0.1:8000/api/users/'
    fetch(url)
    .then((resp)=> resp.json())
    .then(function(data){
        console.log('Data:', data)

        data.forEach((el) => {

            var item1 = `<li  id="${el.id}" class="mb-3 " >
                          <button  class="btn btn-sm  btn-outline-dark pt-0 pb-0 mr-3" onclick="getUser(${el.id})">Edit</button>
                          <button class="btn btn-sm  btn-outline-danger pt-0 pb-0 mr-3" onclick="deleteUser(${el.id})">X</button>
                          <strong>  ${el.first_name} ${el.last_name}</strong>    [${el.phone_no} ]  </li>`
            listt.innerHTML +=item1

         })

    })
}





// get
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
                document.getElementById('wrapper').value = response.department_id
                id = response.id
                })
    }



function reset(){
 document.getElementById('form-wrapper').reset()

}


// post
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
        var selector = document.getElementById('wrapper');
        var dep = selector[selector.selectedIndex].value;

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
                'department_id':dep
            })
        }).then(function(response){
            buildList();
            reset();
        })

    }

})


// update
function  putUser(id){
    var url = `http://127.0.0.1:8000/api/users/${id}/`
    var name = document.getElementById('name').value;
    var surname = document.getElementById('surname').value;
    var salary = document.getElementById('salary').value;
    var phone_no = document.getElementById('phone').value;
    var hire_date = document.getElementById('hire_date').value;
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












