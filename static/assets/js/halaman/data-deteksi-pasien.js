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
    fetch("http://127.0.0.1:8000/api/riwayat-laporan-pasien", requestOptions)
        .then((response) => response.text())
        .then((result) => {
            var result = JSON.parse(result);
            if (result.deteksi) {
                var data = result.deteksi;
                console.log(data);

                $("#table-rekaman").DataTable({
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
                                waktu = full.waktu_rekaman
                                // console.log(waktu);
                                element = '<td><a href="/cetak-hasil/'+waktu+'" class="btn btn-primary ml-2">Cetak</a>'
                                return element
                            },
                            orderable: false,
                          },
                    ],
                });
            }
        })
        .catch((error) => console.log("error", error));
}

