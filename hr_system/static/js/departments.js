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
    var wrapper = document.getElementById('wrapper')
    wrapper.innerHTML = ''
    var listt = document.getElementById('listt')
    listt.innerHTML = ''
    var url = 'http://127.0.0.1:8000/api/departments/'
    fetch(url)
    .then((resp)=> resp.json())
    .then(function(data){
        console.log('Data:', data)
        wrapper.innerHTML +=`<option  value="none" selected disabled>No parent department</option>`
        data.forEach((el) => {
            var item = `<option  value="${el.id}" >${el.department_name}</option >`
            wrapper.innerHTML +=item
            var item1 = `<li  id="${el.id}" class="mb-3 " >
                          <button  class="btn btn-sm  btn-outline-dark pt-0 pb-0 mr-3" onclick="getDepartment(${el.id})">Edit</button>
                          <button class="btn btn-sm  btn-outline-danger pt-0 pb-0 mr-3" onclick="deleteItem(${el.id})">X</button>
                          <strong>  ${el.department_name} </strong>    [Manager: ${el.department_manager }]  [ Under the supervision of: ${el.parent_dep_name }]</li>`
            listt.innerHTML +=item1

         })

    })
}


// post
var form = document.getElementById('form-wrapper')
form.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Form submitted')
    if(id!=null){
        putDepartment(id);
        id = null;
    }
    else
    {
        var url = 'http://127.0.0.1:8000/api/departments/'
        var depname = document.getElementById('depname').value;
        var depmanager = document.getElementById('depmanager').value;

        var selector = document.getElementById('wrapper');
        var depparent = selector[selector.selectedIndex].value;



        fetch( url, {
            method: 'POST',
            headers:{'Content-type' : 'application/json',
                     'X-CSRFToken': csrftoken
            },
            body : JSON.stringify({'department_name': depname,
                                    'department_manager': depmanager,
                                     'parent_dep': depparent})
            }).then(function(response){
                buildList()
                reset()
                })
    }

})


// update
function putDepartment(id){

var url = `http://127.0.0.1:8000/api/departments/${id}/`

    var depname = document.getElementById('depname').value;
    var depmanager = document.getElementById('depmanager').value;

    var selector = document.getElementById('wrapper');
    var depparent = selector[selector.selectedIndex].value;
    fetch( url, {
        method: 'PUT',
        headers:{'Content-type' : 'application/json',
        'X-CSRFToken': csrftoken
        },
        body : JSON.stringify({'department_name': depname,
                                'department_manager': depmanager,
                                 'parent_dep': depparent})
        }).then(function(response){
            buildList()
            reset()
            })
}





// delete
function deleteItem(item){
    console.log('clicked',item)
    var url = `http://127.0.0.1:8000/api/departments/${item}/`


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




// get
var id = null;
function getDepartment(item){
    var url = `http://127.0.0.1:8000/api/departments/${item}/`
        var depname = document.getElementById('depname').value;
        var depmanager = document.getElementById('depmanager').value;
        fetch( url, {
            method: 'GET',
            headers:{'Content-type' : 'application/json',
            'X-CSRFToken': csrftoken
            }
            }).then((resp)=> resp.json())
            .then(function(response){
            console.log(response)
            console.log(response.data)
                reset()
                document.getElementById('depname').value = response.department_name
                document.getElementById('depmanager').value = response.department_manager
                document.getElementById('wrapper').value= response.parent_dep

                id = response.id
                })
    }



function reset(){
 document.getElementById('form-wrapper').reset()

}
