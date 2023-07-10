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
    fetch("http://127.0.0.1:8000/api/riwayat-laporan", requestOptions)
        .then((response) => response.text())
        .then((result) => {
            var result = JSON.parse(result);
            if (result.deteksi) {
                var data = result.deteksi;
                console.log(data);

                $("#table-deteksi").DataTable({
                    data: data,
                    responsive: true,
                    pageLength: 10,
                    autoWidth: false,
                    scrollX: true,
                    columns: [
                        {
                            title:"ID Pasien",
                            data: "id_pasien",                     
                        },
                        {
                            title:"Nama Lengkap",
                            data: "nama_lengkap",
                        },
                        {
                            title: "Usia",
                            data: "usia",
                        },
                        {
                            title: "Jenis Fisiologis",
                            data: "jenis_sinyal",
                        },
                        {
                            title: "Waktu Deteksi",
                            data: "waktu_rekaman",
                        },
                        {
                            title: "Hasil Deteksi",
                            data: "hasil_rekaman",
                        },
                        {
                            title: "Action",
                            // data: id_pasien,
                            render: function (data, type, full, meta) {
                                id = full.id_pasien
                                element = '<td><a href="/edit-data-akun-pasien-admin/'+id+'" class="btn btn-primary ml-2">Edit</a>'
                                element+= '<a href="/delete-data-akun-pasien-admin/'+id+'" class="btn btn-danger ml-2">Delete</a></td>'
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

