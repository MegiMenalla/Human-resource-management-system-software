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




var name;
var role;
buildList()
// list
function buildList(){
    var role = document.getElementById('role') // <select>
    role.innerHTML = ''
    var user = document.getElementById('user')
    user.innerHTML = ''
    var list = document.getElementById('list')
    list.innerHTML = ''



    // list the roles
    var urlr = 'http://127.0.0.1:8000/api/roles/'
    fetch(urlr)
    .then((resp)=> resp.json())
    .then(function(data){
        //console.log('Data:', data)
        data.forEach((el) => {
            var itemr = `<option  value="${el.id}" >${el.role}</option>`
            role.innerHTML +=itemr
         })

    })



    // list the employees
    var url1 = 'http://127.0.0.1:8000/api/users/'
    fetch(url1)
    .then((resp)=> resp.json())
    .then(function(data){
        console.log('Data:', data)

        data.forEach((el) => {

            var item1 = `<option>${el.first_name} ${el.last_name}</option>`
            user.innerHTML +=item1

         })

    })



    // list the user-role
    var url2 = `http://127.0.0.1:8000/api/user_role/`

    list.innerHTML +=`<tr>
                    <th>User</th>
                    <th>Job position</th>
                    </tr>`

    fetch(url2)
    .then((resp)=> resp.json())
    .then(function(data){
        console.log('Data:', data)
        var i=0, j=0;
        users = [];
        roles = [];
        data.forEach((el) => {
            if (users.includes(el.user)==false){
            users.push(el.user);
            i++;
            }
            if (roles.includes(el.role)==false){
            roles.push(el.role);
            j++;
            }
            list.innerHTML +=`<tr><td class="${el.user}"></td><td class="${el.role}"></td><tr>`
         })
         data.forEach((el) => {
         getUser(el.user,i)
         getRole(el.role,j)
         })
    })

}





// get one user name
var name=null;
function getUser(user,i){
    var url = `http://127.0.0.1:8000/api/users/${user}/`
        fetch( url, {
            method: 'GET',
            headers:{'Content-type' : 'application/json',
            'X-CSRFToken': csrftoken
            }
            }).then((resp)=> resp.json())
            .then(function(response){
            //console.log(response.department_id)
                name = response.first_name.concat('  ')
                name = name.concat(response.last_name)
                for (j = 0; j < i; j++)
                if (document.getElementsByClassName(user)[j]!=null)
                    document.getElementsByClassName(user)[j].innerHTML = name

                })
    }



// get one role name
var role1=null;
function getRole(role,i){
    var url = `http://127.0.0.1:8000/api/roles/${role}/`
        fetch( url, {
            method: 'GET',
            headers:{'Content-type' : 'application/json',
            'X-CSRFToken': csrftoken
            }
            }).then((resp)=> resp.json())
            .then(function(response){
            //console.log(response.department_id)
                role1 = response.role

                for (j = 0; j < i; j++)
                    if (document.getElementsByClassName(role)[j]!=null)
                        document.getElementsByClassName(role)[j].innerHTML = role1;

                })
    }



// post
function postRole(){
    var form = document.getElementById('form-wrapper')
    var url = `http://127.0.0.1:8000/api/user_role/`
    form.innerHTML='';
    var start = document.getElementById('start').value;
    var selector = document.getElementById('user');
    var user = selector[selector.selectedIndex].value;
    var selector1 = document.getElementById('role');
    var role = selector1[selector1.selectedIndex].value;

    fetch( url, {
        method: 'POST',
        headers:{'Content-type' : 'application/json',
        'X-CSRFToken': csrftoken
        },
        body : JSON.stringify({
                                'user': role,
                                 'role': role,
                                 'start_date':start })
        }).then(function(response){
            buildList()

            })



}

