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

showDeletedUsers()
function showDeletedUsers(){
    var listt = document.getElementById('listt')
    listt.innerHTML = ''
// list the employees
    var url = 'http://127.0.0.1:8000/api/users/'
    fetch(url)
    .then((resp)=> resp.json())
    .then(function(data){
        console.log('Data:', data)

        data.forEach((el) => {
            if (el.active==false){
                 var item1 = `<li  id="${el.id}" class="mb-3 " >
                          <button  class="btn btn-sm  btn-outline-danger pt-0 pb-0 mr-3" onclick="undoDelete(${el.id})">Undo</button>

                          <strong>  ${el.first_name} ${el.last_name}</strong>    [${el.phone_no} ]  </li>`
                listt.innerHTML +=item1
            }

         })

    })
}


function undoDelete(id){
var url = `http://127.0.0.1:8000/api/users/${id}/`
fetch(url, {
            method : 'PUT',
             headers:{'Content-type' : 'application/json',
                     'X-CSRFToken': csrftoken
            },
            body : JSON.stringify({})
        }).then(function(response){
            showDeletedUsers()
        })

}