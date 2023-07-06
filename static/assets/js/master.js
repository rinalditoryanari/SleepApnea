getData()

function getData(){
    if (sessionStorage.getItem('role') != 'master') {
        sessionStorage.clear()
        window.location.href = "http://127.0.0.1:8000/auth-login2"
    }
    document.getElementById("username-header").innerHTML = sessionStorage.getItem('username');
}

function logout(){
    sessionStorage.clear()
    window.location.href = "http://127.0.0.1:8000/auth-login2"
}