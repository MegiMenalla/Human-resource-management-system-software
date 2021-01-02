
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

function reset(){
 document.getElementById('form-wrapper').reset()

}




// post
function postRequest(userID){
id=userID;
    var form = document.getElementById('form-wrapper')

    console.log('submitted')

    var url = `http://127.0.0.1:8000/api/requests/`

    var startd = document.getElementById('startd').value;
    var endd = document.getElementById('endd').value;
    var starth = document.getElementById('starth').value;
    var endh = document.getElementById('endh').value;
    var approval_flag = false;
    var checked = false;
    var desc = 'No description';


    fetch(url, {
        method : 'POST',
         headers:{'Content-type' : 'application/json',
                 'X-CSRFToken': csrftoken
        },
        body : JSON.stringify({
            'user_id': userID,
            'start_date':startd,
            'end_date':endd,
            'start_hour':starth,
            'end_hour':endh,
            'approval_flag':approval_flag,
            'checked': checked,
            'description':desc
        })
    }).then(function(response){
        reset();
        //console.log(response.user_id)
    })
}



// list employees requests

buildList()

function buildList(){

    var checkedList = document.getElementById('checkedList')

    var uncheckedList = document.getElementById('uncheckedList')

    var url = `http://127.0.0.1:8000/api/requests/`
    fetch(url)
    .then((resp)=> resp.json())
    .then(function(data){
       // console.log('Data:', data)

        checked = `<tr>
                    <th>From</th>
                    <th></th>
                    <th>To</th>
                    <th></th>
                    <th>Status</th>
                </tr>`
        checkedList.innerHTML +=checked
        unchecked = `<tr>
                    <th>From</th>
                    <th></th>
                    <th>To</th>
                    <th></th>
                </tr>`
        uncheckedList.innerHTML +=unchecked



        data.forEach((el) => {
        if (el.checked){
              if(el.approval_flag)
                var sts = `<h6 class="text-success">Approved</h6>
                <td><button class="btn btn-sm btn-outline-danger" onClick="deleteRequest(${el.id})" >X</button></td>`
                else
                var sts = `<h6 class="text-danger">Denied</h6>`

                var checked = `<tr>
                                    <td>${el.start_date}</td>
                                    <td>${el.start_hour}</td>
                                    <td>${el.end_date}</td>
                                    <td>${el.end_hour}</td>
                                    <td>${sts}</td>
                                </tr>`

                checkedList.innerHTML +=checked
        }
        else{

            var unchecked = `<tr>
                                <td>${el.start_date}</td>
                                <td>${el.start_hour}</td>
                                <td>${el.end_date}</td>
                                <td>${el.end_hour}</td>
                                <td><button class="btn btn-sm btn-outline-danger" onClick="deleteRequest(${el.id})" >Cancel Request</button></td>
                            </tr>`

            uncheckedList.innerHTML +=unchecked
        }
       })

    })
}


// delete my request
// delete
function deleteRequest(req_id){
    //console.log('clicked',req_id)
    var url = `http://127.0.0.1:8000/api/requests/${req_id}/`


    fetch( url, {
        method: 'DELETE',
        headers:{'Content-type' : 'application/json',
        'X-CSRFToken': csrftoken
        }
        }).then(function(response){
            document.getElementById('checkedList').innerHTML=''
            document.getElementById('uncheckedList').innerHTML=''
            buildList()
            })
}


infoList(1)
// list personal information
function infoList(userID){
    var url = `http://127.0.0.1:8000/api/users/${userID}`
    fetch(url)
    .then((resp)=> resp.json())
    .then(function(response){
        document.getElementById('name').innerHTML += response.first_name
        document.getElementById('name').innerHTML += ' '
        document.getElementById('name').innerHTML += response.last_name
        document.getElementById('salary').innerHTML += ': '
        document.getElementById('salary').innerHTML += response.salary
        document.getElementById('phone').innerHTML += ': '
        document.getElementById('phone').innerHTML += response.phone_no

    })
}



// get one specific request
var id=1;
function checkRequest(){
    var url = `http://127.0.0.1:8000/api/requests/${id}/`
    console.log(id)
        fetch( url, {
            method: 'GET',
            headers:{'Content-type' : 'application/json',
            'X-CSRFToken': csrftoken
            }
            }).then((resp)=> resp.json())
            .then(function(response){
                if(response.approval_flag){

                    //to be continued
                    
                }
                })
    }

checkRequest()