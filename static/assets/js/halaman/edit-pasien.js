refresh()

function refresh() {
    var formdata = new FormData();
    formdata.append("username_rs", sessionStorage.getItem("username"));

    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/api/edit-data-akun", requestOptions)
    .then(response => response.text())
    .then(result => {
        console.log(result)
        var API = JSON.parse(result)
        console.log(API)
        // document.getElementById("total_pasien").innerHTML = API.pasiens;
        document.getElementById("id").value = API.pasiens[0].id_pasien;
        document.getElementById("rs").value = API.pasiens[0].rs;
        document.getElementById("id_rs").value = API.pasiens[0].id_rs;
        document.getElementById("username").value = API.pasiens[0].username;
        document.getElementById("username_lama").value = API.pasiens[0].username;
        document.getElementById("name").value = API.pasiens[0].nama_lengkap;
        document.getElementById("nama_lengkap").value = API.pasiens[0].nama_lengkap;
        document.getElementById("no_telp").value = API.pasiens[0].no_telp;
        document.getElementById("alamat").value = API.pasiens[0].alamat;
        document.getElementById("email").value = API.users[0].email;
        document.getElementById("password").value = API.users[0].password;

    })
    .catch(error => console.log('error', error));
}