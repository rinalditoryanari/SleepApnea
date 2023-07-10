function cekid_pasien() {
    var formdata = new FormData();
    formdata.append("id_pasien", document.getElementById('id_pasien').value);

    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/cekIDPasien", requestOptions)
    .then(response => response.text())
    .then(result => {
        console.log(result);
        var API = JSON.parse(result)
        sessionStorage.setItem('nama_lengkap',API.nama_lengkap)
        document.getElementById("nama_lengkap").value = API.nama_lengkap;
        document.getElementById("id_pasien1").value = document.getElementById('id_pasien').value

        // document.getElementById("nama_lengkap").value = API.nama_lengkap;
        // document.getElementById("nama_lengkap").hidden = false 
        // const nama_lengkap = sessionStorage.getItem(API.nama_lengkap)
    })
    .catch(error => console.log('error', error));
}

function ceknama_pasien() {
    var formdata = new FormData();
    formdata.append("nama", document.getElementById('nama').value);

    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/cekNamaPasien", requestOptions)
    .then(response => response.text())
    .then(result => {
        console.log(result);
        console.log("test");
        var API = JSON.parse(result)
        sessionStorage.setItem('id_pasien',API.id_pasien)
        document.getElementById("nama_lengkap").value = document.getElementById('nama').value;
        document.getElementById("id_pasien1").value = API.id_pasien;

        // document.getElementById("nama_lengkap").value = API.nama_lengkap;
        // document.getElementById("nama_lengkap").hidden = false 
        // const nama_lengkap = sessionStorage.getItem(API.nama_lengkap)
    })
    .catch(error => console.log('error', error));
}