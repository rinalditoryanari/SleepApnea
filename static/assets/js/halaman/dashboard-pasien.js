refresh()

function refresh() {
    var formdata = new FormData();
    formdata.append("username_rs", sessionStorage.getItem("username"));

    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/api/dashboard-pasien", requestOptions)
    .then(response => response.text())
    .then(result => {
        console.log(result)
        var API = JSON.parse(result)
        console.log(API)

        // document.getElementById("total_pasien").innerHTML = API.pasiens;
        document.getElementById("total_rekaman").innerHTML = API.rekamans;
        document.getElementById("total_rekaman_today").innerHTML = API.rekamans_today;
        document.getElementById("id-pasien").innerHTML = API.pasiens[0].id_pasien;
        document.getElementById("nama-pasien").innerHTML = API.pasiens[0].nama_lengkap;
        document.getElementById("username-pasien").innerHTML = API.pasiens[0].username;
        // document.getElementById("email-pasien").innerHTML = API.pasiens[0].email;
        document.getElementById("rs-pasien").innerHTML = API.pasiens[0].rs;
        // document.getElementById("role-pasien").innerHTML = API.pasiens;

    })
    .catch(error => console.log('error', error));
}