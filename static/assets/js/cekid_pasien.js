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
        document.getElementById("nama_lengkap").innerHTML = API.nama_lengkap;
        document.getElementById("nama_lengkap").hidden = false 
    })
    .catch(error => console.log('error', error));
}