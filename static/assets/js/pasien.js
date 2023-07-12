getData()

function getData(){
    if (sessionStorage.getItem('role') != 'pasien') {
        sessionStorage.clear()
        window.location.href = "http://127.0.0.1:8000/auth-login2"
    }
    document.getElementById("username-header").innerHTML = sessionStorage.getItem('username');
}

function logout(){
    sessionStorage.clear()
    alert("Anda Sudah Logout")
    window.location.href = "http://127.0.0.1:8000/auth-login2"
}

function edit(){
    const url = 'http://127.0.0.1:8000/edit-data-akun/' +sessionStorage.getItem('username')
    window.location.href = url
}

