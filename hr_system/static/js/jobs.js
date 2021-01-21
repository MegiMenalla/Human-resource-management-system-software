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


var name;
var role;
buildList()
// list
function buildList(){
    var role = document.getElementById('role') // <select>
    role.innerHTML = ''
    var user = document.getElementById('user')
    user.innerHTML = ''

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
            if(el.active){
                var item1 = `<option>${el.first_name} ${el.last_name}</option>`
                user.innerHTML +=item1
            }
         })

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

