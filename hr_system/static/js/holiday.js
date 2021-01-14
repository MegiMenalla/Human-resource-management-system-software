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

    var listt = document.getElementById('listt')
    listt.innerHTML = ''
    var url = `http://127.0.0.1:8000/api/holidays/`
    fetch(url)
    .then((resp)=> resp.json())
    .then(function(data){
        console.log('Data:', data)

        data.forEach((el) => {
            var item1 = `<li  id="${el.id}" class="mb-3 " >
                          <button type="submit" class="btn btn-sm  btn-outline-danger pt-0 pb-0 mr-3" onclick="getHoliday(${el.id})">Edit</button>
                          <button type="submit" class="btn btn-sm  btn-outline-danger pt-0 pb-0 mr-3" onclick="deleteHoliday(${el.id})">X</button>
                          <strong>  ${el.holiday_name} </strong> on ${el.day }</li>`
            listt.innerHTML +=item1

         })

    })
}


// post
var form = document.getElementById('form-wrapper')
form.addEventListener('submit', function(e){
    e.preventDefault()

    if(id!=null){

        putHoliday(id);
        id = null;
    }
    else
    {
        var url = 'http://127.0.0.1:8000/api/holidays/'

        var name = document.getElementById('holname').value;
        var day = document.getElementById('day').value;
        var lastactive = document.getElementById('lastactive').value;
        var active_flag = document.getElementById('active_flag').value;
        var x = document.getElementById("active_flag").checked;
        console.log(x)
        if (x)
            active_flag=true;
        else
            active_flag=false;


        fetch( url, {
            method: 'POST',
            headers:{'Content-type' : 'application/json',
            'X-CSRFToken': csrftoken
            },
            body : JSON.stringify({'holiday_name': name,
                                    'active_flag': active_flag,
                                     'day': day,
                                     'last_active':lastactive})
            }).then(function(response){
                buildList()
                reset()
                })
    }

})


// update
function putHoliday(id){

var url = `http://127.0.0.1:8000/api/holidays/${id}/`

    var name = document.getElementById('holname').value;
    var day = document.getElementById('day').value;
    var lastactive = document.getElementById('lastactive').value;
    var active_flag = document.getElementById('active_flag').value;
    var x = document.getElementById("active_flag").checked;
        console.log(x)
        if (x)

            active_flag=true;
        else
            active_flag=false;
    if (x)
        active_flag=true;
    else
        active_flag=false;
    fetch( url, {
        method: 'PUT',
        headers:{'Content-type' : 'application/json',
        'X-CSRFToken': csrftoken
        },
        body : JSON.stringify({'holiday_name': name,
                                'active_flag': active_flag,
                                 'day': day,
                                 'last_active':lastactive})
        }).then(function(response){
            buildList()
            reset()
            })
}





// delete
function deleteHoliday(item){
    console.log('clicked',item)
    var url = `http://127.0.0.1:8000/api/holidays/${item}/`


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
function getHoliday(item){
    var url = `http://127.0.0.1:8000/api/holidays/${item}/`
    var name = document.getElementById('holname').value;
    var day = document.getElementById('day').value;
    var lastactive = document.getElementById('lastactive').value;
    var active_flag = document.getElementById('active_flag').value;



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
                document.getElementById('holname').value= response.holiday_name
                document.getElementById('day').value = response.day
                document.getElementById('lastactive').value = response.last_active
                 if (response.active_flag==true)
                   document.getElementById("active_flag").checked=true;
                else
                    document.getElementById("active_flag").checked=false;


                id = response.id
                })
    }



function reset(){
 document.getElementById('form-wrapper').reset()

}
