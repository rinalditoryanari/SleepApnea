refresh()

function refresh() {
    var formdata = new FormData();
    formdata.append("username_rs", sessionStorage.getItem("username"));

    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/api/dashboard-admin", requestOptions)
    .then(response => response.text())
    .then(result => {
        console.log(result)
        var API = JSON.parse(result)
        console.log(API)

        document.getElementById("total_pasien").innerHTML = API.pasiens;
        document.getElementById("total_rekaman").innerHTML = API.rekamans;
        document.getElementById("total_rekaman_today").innerHTML = API.rekamans_today;
        document.getElementById("id-admin").innerHTML = API.admins[0].id_admin;
        document.getElementById("nama-admin").innerHTML = API.admins[0].nama_lengkap;
        document.getElementById("username-admin").innerHTML = API.admins[0].username;
        // document.getElementById("email-admin").innerHTML = API.admins[0].email;
        document.getElementById("rs-admin").innerHTML = API.admins[0].rs;
        // document.getElementById("role-admin").innerHTML = API.admins;


    })
    .catch(error => console.log('error', error));
}
