refresh()

function refresh() {
    var formdata = new FormData();
    formdata.append("username_rs", sessionStorage.getItem("username"));

    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/api/dashboard-super", requestOptions)
    .then(response => response.text())
    .then(result => {
        console.log(result)
        var API = JSON.parse(result)
        console.log(API)

        document.getElementById("total_admin").innerHTML = API.admins;
        document.getElementById("total_pasien").innerHTML = API.pasiens;
        document.getElementById("id-super").innerHTML = API.supers[0].id_nurse;
        document.getElementById("nama-super").innerHTML = API.supers[0].nama_lengkap;
        document.getElementById("username-super").innerHTML = API.supers[0].username;
        // document.getElementById("email-super").innerHTML = API.supers[0].email;
        document.getElementById("rs-super").innerHTML = API.supers[0].rs;
        // document.getElementById("role-super").innerHTML = API.supers;


    })
    .catch(error => console.log('error', error));
}
