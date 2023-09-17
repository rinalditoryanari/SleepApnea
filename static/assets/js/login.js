function loginAPI() {
    var formdata = new FormData();
    formdata.append("email", document.getElementById('email').value);
    formdata.append("password", document.getElementById('password').value);

    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/loginAPI", requestOptions)
    .then(response => response.text())
    .then(result => {
        var API = JSON.parse(result)
        sessionStorage.setItem('username',API.username)
        sessionStorage.setItem('email',API.email)
        sessionStorage.setItem('role',API.role)
        window.location.href = API.url
    })
    .catch(error => console.log('error', error));
}