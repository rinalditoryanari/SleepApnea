getData()

function getData(){
    if (sessionStorage.getItem('role') != 'admin') {
        sessionStorage.clear()
        window.location.href = "http://127.0.0.1:8000/auth-login2"
    }
    document.getElementById("username-header").innerHTML = sessionStorage.getItem('username');
}

function logout(){
    sessionStorage.clear()
    window.location.href = "http://127.0.0.1:8000/auth-login2"
}

function validateDateTime() {
    
  
    // Submit or process the valid datetime
    // ...
  }

document.
    getElementById("waktu_rekaman").
    addEventListener("input",function() {
        const input = document.getElementById('waktu_rekaman');
        const selectedDateTime = new Date(input.value);
        const currentDateTime = new Date();
        if (selectedDateTime >= currentDateTime) {
            alert('Pastikan Anda Menginput Waktu Deteksi Dengan Benar.');
            input.value = ''; // Clear the input value
            return;
        }
    })

document.
    getElementById("jenis_fisiologis").
    addEventListener("input",function() {
        const previousInput = document.getElementById('jenis_fisiologis');
        const fileInput = document.getElementById('file_predict');
        previousInput.addEventListener('change', function() {
            console.log(previousInput.value);
            fileInput.removeAttribute('disabled');
        });
        
    })


document.
    getElementById('file_predict')
    .addEventListener('change', function() {
    // Get the selected file
    const selectedFile = document.getElementById('file_predict').files[0];
  
    switch (document.getElementById('jenis_fisiologis').value) {
        case "Otak - EEG":
            extension = '.txt'
            break;

        case "Jantung - ECG":
            extension = '.zip'
            break;
    
        default:
            extension = ''
            break;
    }

    // Check if the file has the desired extension
    if (selectedFile.name.endsWith(extension)) {
        kata = document.getElementById("file_predict").value;
        console.log(kata);
        lastIndex = kata.lastIndexOf('\\');
        // Extract the file name by slicing the string from the last backslash index + 1
        const fileName = kata.slice(lastIndex + 1);
    
        // kata = kata.split('/').slice(-1)[0]
        document.getElementById("label").innerHTML = fileName
    } else {
        // File does not have the desired extension
        alert('Invalid file extension. Please select a '+ extension +' file.');
        // Clear the input field
        document.getElementById('file_predict').files[0] = '';
        
    }
});

