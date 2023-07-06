function eeg_predict() {
    var formdata = new FormData();
    formdata.append("eeg_file", document.getElementById("file_predict").files[0]);

    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/api/predict-eeg", requestOptions)
    .then(response => response.text())
    .then(result => {
        var API = JSON.parse(result)
        sessionStorage.setItem('predictions',API.predictions)
        sessionStorage.setItem('description',API.description)
        sessionStorage.setItem('percentage',API.percentage)
        document.getElementById("result").value = API.description;
    })
    .catch(error => console.log('error', error));
}