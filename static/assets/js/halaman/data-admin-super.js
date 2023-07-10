refresh()

function refresh() {
    var formdata = new FormData();
    formdata.append("username_rs", sessionStorage.getItem("username"));


    var requestOptions = {
        method: "POST",
        body: formdata,
        redirect: "follow",
    };
    console.log(sessionStorage.getItem("username"));
    fetch("http://127.0.0.1:8000/api/data-akun-admin", requestOptions)
        .then((response) => response.text())
        .then((result) => {
            var result = JSON.parse(result);
            if (result.admins) {
                var data = result.admins;
                console.log(data);

                $("#table-admin").DataTable({
                    data: data,
                    responsive: true,
                    pageLength: 10,
                    autoWidth: false,
                    scrollX: true,
                    columns: [
                        {
                            title:"ID RS",
                            data: "id_rs",                     
                        },
                        {
                            title:"Nama Lengkap",
                            data: "nama_lengkap",
                        },
                        {
                            title: "Username",
                            data: "username",
                        },
                        {
                            title: "Id Admin",
                            data: "id_admin",
                        },
                        {
                            title: "Waktu Dibuat",
                            data: "waktu_dibuat",
                        },
                        {
                            title: "Action",
                            // data: id_pasien,
                            render: function (data, type, full, meta) {
                                id = full.id_admin
                                element = '<td><a href="/edit-data-akun-admin/'+id+'" class="btn btn-primary ml-2">Edit</a>'
                                element+= '<a href="/delete-data-akun-admin/'+id+'" class="btn btn-danger ml-2">Delete</a></td>'
                                return element
                            },
                            orderable: false,
                          }
                    ],
                });
            }
        })
        .catch((error) => console.log("error", error));
}

