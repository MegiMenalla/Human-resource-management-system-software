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
var name='';
function reset(){
 document.getElementById('form-wrapper').reset()
 document.getElementById('checkedList').innerHTML=''
 document.getElementById('uncheckedList').innerHTML=''

}


var id = getID()
console.log(id);

// post
function postRequest(userID){

    var form = document.getElementById('form-wrapper');

    var url = `http://127.0.0.1:8000/api/requests/`

    var startd = document.getElementById('startd').value;
    var endd = document.getElementById('endd').value;
    var starth = document.getElementById('starth').value;
    var endh = document.getElementById('endh').value;
    var approval_flag = false;
    var checked = false;
    var desc = 'No description';

    var startmoment= moment(startd)
    var endmoment= moment(endd)

    var starthour = moment(starth,"hh:mm")
    var endhour = moment(endh,"hh:mm")

    //alert(starthour.isBefore(endhour))
    if (startmoment.isBefore(moment())){
        alert('Your input is invalid. Please make sure your start date is after today!')
        return;
    }
    else if(endmoment.isBefore(startmoment)){
        alert('Your input is invalid. Please make sure your start date is before your end date!')
        return;
    }else if(startmoment.isSame(endmoment)){
        if(endhour.isBefore(starthour)){
            alert('Your input is invalid. Please make sure your start hour is before your end hour!')
            return;
        }
        else{
            //subtract from total hour
            fetch(url, {
                method : 'POST',
                 headers:{'Content-type' : 'application/json',
                         'X-CSRFToken': csrftoken
                },
                body : JSON.stringify({
                    'user_id': userID,
                    'approver': null,
                    'start_date':startd,
                    'end_date':endd,
                    'start_hour':starth,
                    'end_hour':endh,
                    'approval_flag':approval_flag,
                    'checked': checked,
                    'description':desc,

                })
            }).then(function(response){
                reset();
                buildList()
            })
        }
    }else{

        fetch(url, {
            method : 'POST',
             headers:{'Content-type' : 'application/json',
                     'X-CSRFToken': csrftoken
            },
            body : JSON.stringify({
                'user_id': userID,
                'approver': null,
                'start_date':startd,
                'end_date':endd,
                'start_hour':starth,
                'end_hour':endh,
                'approval_flag':approval_flag,
                'checked': checked,
                'description':desc,

            })
        }).then(function(response){
            reset();
            buildList()
        })

    }
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
                    <th>Reason</th>
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


        var i=0;
        tmp = [];

        data.forEach((el) => {
        // check if its this userrss request
        if (el.user_id==id){
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
                                    <td style="width: 25%;">${el.description}</td>
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
        }

       })

    })
}


// delete my request
// delete
function deleteRequest(req_id){
    //console.log('clicked',req_id)
    var url = `http://127.0.0.1:8000/api/requests/${req_id}/`
    // get the request  to be deleted
    fetch( url, {
            method: 'GET',
            headers:{'Content-type' : 'application/json',
            'X-CSRFToken': csrftoken
            }
            }).then((resp)=> resp.json())
            .then(function(response){
            // if the request is checked than you cant cancel less then 48 hours before the startdate
            if (response.checked){
                // check if the canceling is being done  48 hours before the start date
                sd = response.start_date
                sh = response.start_hour
                a =sd.concat(sh)

                sdm = moment(a, "YYYY-MM-DDhh:mm")
                sdm.subtract(48,"hours");
                if(moment().isAfter(sdm)){
                    alert("Oops! You cannot cancel now. Too late.")
                    return;
                }else{
                    fetch( url, {
                    method: 'DELETE',
                    headers:{'Content-type' : 'application/json',
                    'X-CSRFToken': csrftoken
                    }
                    }).then(function(response){
                        reset()
                        buildList()
                        })
                }
            }
            else{
                fetch( url, {
                method: 'DELETE',
                headers:{'Content-type' : 'application/json',
                'X-CSRFToken': csrftoken
                }
                }).then(function(response){
                    reset()
                    buildList()
                    })
            }
            })

}






