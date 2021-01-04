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
 document.getElementById('checkedList').innerHTML=''
 document.getElementById('uncheckedList').innerHTML=''

}




// post
function postRequest(userID){
    infoList(userID);
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

    if(endmoment.isBefore(startmoment)){
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
                buildList()
            })
        }
    }else{
        //subtract from total days
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
                    alert("Oops!   You cannot cancel now. Too late.")
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





// list personal information
function infoList(userID){

    var url = `http://127.0.0.1:8000/api/users/${userID}`
    fetch(url)
    .then((resp)=> resp.json())
    .then(function(response){
    document.getElementById('listt').innerHTML=`
        <li>Date & Time: ${moment()}</li>
        <li class="pb-3 pt-3" id="name"><strong>${response.first_name} ${response.last_name}</strong></li>
        <li class="pb-3" id="jobid">Job position:  </li>
        <li class="pb-3" id="salary">Salary: ${response.salary}</li>
        <li class="pb-3" id="phone">Phone:  ${response.phone_no}</li>
        <li class="pb-3" id="positionLeft">Days left in the current position</li>
        <li class="pb-3" id="premissionLeft">Days left to request permission</li>
        <li class="pb-3" id="futureHoliday">Nearest future holiday</li>`

    })
}


// Moment.js
/*
// current date and time
var  m = moment();
console.log(`toString() => ${m.toString()}`);
console.log(`toISOString()=>${m.toISOString()}`);

// create from iso 8601 string
m=moment("2021-01-03T13:09:00.000-01:00");
console.log(`toString() => ${m.toString()}`);
console.log(`toISOString()=>${m.toISOString()}`);

//parse using a format
m=moment("14/06/2019 4:50PM", "DD/MM/YYYY h:mmA");

console.log(`toString() => ${m.toString()}`);
console.log(`toISOString()=>${m.toISOString()}`);


//getter and setter
const m=moment()
console.log(m.toString());

//getting units
console.log(m.minutes());
console.log(m.hour());
console.log(m.week());
console.log(m.year());
console.log(m.get("quarter"));

//setting units w/ moment.js
m.minutes(65);
m.hour(12);
m.week(20);
m.set("day", 9 )
console.log(m.toString());


//min & max of a particular set of moment objects
// compare two moemnt objects
const a=moment("01-01-2021")
const n=moment("02-02-2021")
console.log(moment.max(moment(), a).toString());
console.log(moment.min(moment(), a).toString());


//manupulate, add subtract
const m = moment();

console.log(`original moment: ${m.toString()}`);
//add or subtract
m.add(4,"hours");
m.add(1,"h").add(12,"m");
m.add({
    "hours":1,
    "minutes":20
})
m.subtract({
    "hours":1,
    "minutes":20
})
//return to the begining of the hour
m.startOf("hour");
m.startOf("year");
m.endOf("day");

console.log(`after manipulation: ${m.toISOString()}`);


//format for display
const m = moment();

//console.log(m.format("[bfcxzrgso] dd mm yyyy"))
m.locale("en-au")
console.log(m.format("L"))



//how long ago was this moment from now
const m=moment("2019-05-13")
console.log(m.fromNow())
console.log(m.from("2019-05-15"))
const a=moment().add(3,"days")
console.log(a.calendar())
const b=moment().add(30,"days")
console.log(b.calendar())

// find the diffeyfformrences between two moment objects
const m=moment()
const m1=moment("2020-05-13")
console.log(m.diff(m1,"weeks"))

const m1=moment("2020-05-13")
const jsonObj={
    momentObj:m1
};
console.log(JSON.stringify(jsonObj));

*/


