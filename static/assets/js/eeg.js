
function predict() {
    if (document.getElementById("jenis_fisiologis").value == "Otak - EEG") {
    eeg_predict() 
    } else if (document.getElementById("jenis_fisiologis").value == "Jantung - ECG"){
        ecg_predict()
    }
}
function eeg_predict() {
    console.log("test");
    var formdata = new FormData();
    formdata.append("eeg_file", document.getElementById("file_predict").files[0]);
    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };
    console.log("hello");
    fetch("http://127.0.0.1:8000/api/predict-eeg", requestOptions)
    .then(response => response.text())
    .then(result => {
        var API = JSON.parse(result)
        sessionStorage.setItem('predictions',API.predictions)
        sessionStorage.setItem('description',API.description)
        sessionStorage.setItem('percentage',API.percentage)
        document.getElementById("result").value = API.description;
        const prediksi = sessionStorage.getItem(API.predictions)
        const deskripsi = sessionStorage.getItem(API.description)
        const persen = sessionStorage.getItem(API.percentage)        
    })
    .catch(error => console.log('error', error));
}
function ecg_predict() {
    console.log("hai");
    var formdata = new FormData();
    formdata.append("ecg_file", document.getElementById("file_predict").files[0]);
    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };
    console.log("ho");
    fetch("http://127.0.0.1:8000/api/predict-ecg", requestOptions)
    .then(response => response.text())
    .then(result => {
        console.log(result);
        var API = JSON.parse(result)
        sessionStorage.setItem('predictions',API.predictions)
        document.getElementById("result").value = API.predictions;
        const prediksi = sessionStorage.getItem(API.predictions)      
    })
    .catch(error => console.log('error', error));
}
function coba() {

}
