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
var name=null;
//var id = getID();




buildListRequests()

// build the tables for checked and unchecked requests


function buildListRequests(){
    var uncheckedList = document.getElementById('for_approval')
    var checkedList = document.getElementById('checked_requests')
    var url = `http://127.0.0.1:8000/api/requests-to-be-checked/`
    fetch(url)
    .then((resp)=> resp.json())
    .then(function(response){

        checked = `<tr>
                    <th>Emplyee</th>
                    <th>From</th>
                    <th></th>
                    <th>To</th>
                    <th></th>
                    <th>Status</th>
                    <th>Reason:</th>
                </tr>`
        checkedList.innerHTML +=checked

        unchecked = `<tr>
                    <th>Emplyee</th>
                    <th>From</th>
                    <th></th>
                    <th>To</th>
                    <th></th>
                    <th></th>
                    <th></th>
                    <th>Reason:</th>
                </tr>`
        uncheckedList.innerHTML +=unchecked

        var i=0;
        response.forEach((el) => {

        console.log(el.user_id)
            i++;
            // get the username for display purpose
            getUser(el.user_id,i)

            if (el.checked){
                  if(el.approval_flag)
                    var sts = `<h6 class="text-success">Approved</h6>`
                    else
                    var sts = `<h6 class="text-danger">Denied</h6>`

                    var checked = `<tr>
                                        <td class="${el.user_id}"></td>
                                        <td>${el.start_date}</td>
                                        <td>${el.start_hour}</td>
                                        <td>${el.end_date}</td>
                                        <td>${el.end_hour}</td>
                                        <td>${sts}</td>
                                        <td style="width: 25%;">${el.description}</td>
                                    </tr>`
                    checkedList.innerHTML +=checked
            }
            else{
                var unchecked = `<tr>
                                    <td class="${el.user_id}"></td>
                                    <td>${el.start_date}</td>
                                    <td>${el.start_hour}</td>
                                    <td>${el.end_date}</td>
                                    <td>${el.end_hour}</td>
                                    <td><a class="btn btn-sm btn-success" onClick='approve(${el.id})'>Approve</a></td>
                                    <td><a class="btn btn-sm btn-danger" onClick='deny(${el.id})'>Deny</a></td>
                                    <td>
                                        <textarea id="${el.id}" rows="2" cols="50"></textarea>
                                    </td>
                                </tr>`
                uncheckedList.innerHTML +=unchecked
            }

       })
    })
}




// update // approve a request and give a reason why
function  approve(id){
    var desc = document.getElementById(id).value;
    var url = `http://127.0.0.1:8000/api/requests/${id}/`

    fetch(url, {
            method : 'PUT',
             headers:{'Content-type' : 'application/json',
                     'X-CSRFToken': csrftoken
            },
            body : JSON.stringify({
                'checked':true,
                'approval_flag':true,
                'description':desc
            })
        }).then(function(response){
            reset()
            buildListRequests()
        })
}

// update
// deny a request and give a reason why
function  deny(id){
  var desc = document.getElementById(id).value;
    var url = `http://127.0.0.1:8000/api/requests/${id}/`

    fetch(url, {
            method : 'PUT',
             headers:{'Content-type' : 'application/json',
                     'X-CSRFToken': csrftoken
            },
            body : JSON.stringify({
                'checked':true,
                 'approval_flag':false,
                'description':desc
            })
        }).then(function(response){
            reset()
            buildListRequests()
        })
}

function reset(){
 document.getElementById('for_approval').innerHTML=''
 document.getElementById('checked_requests').innerHTML=''
}

// get one user name

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
                        document.getElementsByClassName(user)[j].innerHTML = name;

                })
    }