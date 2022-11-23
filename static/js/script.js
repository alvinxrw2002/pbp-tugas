// Fungsi untuk me-refresh todolist melalui AJAX GET terhadap seluruh
// data dan menampilannya dalam bentuk cards
function refreshTodolist() {
    $.ajax({
        type: "GET",
        url: '/todolist/json',
        datatype: "json",
        success: function (datas) {
            var cardView = ""
            for (var i = 0; i < datas.length; i++) {
                var data = datas[i].fields
                var idData = datas[i].pk
                var statusPenyelesaian = data.is_finished ? "✅" : "❌"
                cardView += `
                        <div id="${idData}" class="col-sm-4">
                            <div id="hvr-sweep-to-right" class="card text-center" style="margin: 15px 0;">
                                <div class="card-header">
                                    Status penyelesaian: ${statusPenyelesaian}
                                </div>
                                <div class="card-body">
                                    <h5 class="card-title">${data.title}</h5>
                                    <p class="card-text">${data.description}</p>
                                    <button class="btn btn-info btn-sm" onclick="ubahStatus(${idData})">Ubah Status</button>
                                    <button class="btn btn-warning btn-sm" onclick="hapusData(${idData})">Hapus</button>
                                </div>
                                <div class="card-footer text-muted">
                                    ${data.date}
                                </div>
                            </div>
                        </div>`}
            cardView += "</div>"
            $('#tampilan-cards').html(cardView)
        },
    });;
}

// Menambahkan task baru ke server
function tambahinData() {
    var judulTask = $("#judul-task").val();
    var deskripsiTask = $("#deskripsi-task").val();
    document.querySelector('#form-tambah-task').reset()
    $.ajax({
        type: "POST",
        url: "/todolist/add",
        data: {
            'judul': judulTask,
            'deskripsi': deskripsiTask,
        },
        success: function () {
            tambahinHTML();
        }
    });
}

// Menampilkan seluruh data ynag sudah ditambahkan dengan
// data baru ke pengguna
function tambahinHTML() {
    $.ajax({
        type: "GET",
        url: '/todolist/json',
        datatype: "json",
        success: function (all) {
            var datas = all[all.length - 1];
            var data = datas.fields
            var idData = datas.pk
            var statusPenyelesaian = data.is_finished ? "✅" : "❌"
            var cardView = `
                        <div id="${idData}" class="col-sm-4">
                            <div id="hvr-sweep-to-right" class="card text-center" style="margin: 15px 0;">
                                <div class="card-header">
                                    Status penyelesaian: ${statusPenyelesaian}
                                </div>
                                <div class="card-body">
                                    <h5 class="card-title">${data.title}</h5>
                                    <p class="card-text">${data.description}</p>
                                    <button class="btn btn-info btn-sm" onclick="ubahStatus(${idData})">Ubah Status</button>
                                    <button class="btn btn-warning btn-sm" onclick="hapusData(${idData})">Hapus</button>
                                </div>
                                <div class="card-footer text-muted">
                                    ${data.date}
                                </div>
                            </div>
                        </div>`
            $('#tampilan-cards').append(cardView)
        },
    });;
}

function ubahStatus(idData) {
    $.ajax({
        url: `/todolist/update/${idData}`,
        success: function () {
            var targetElement = document.getElementById(`${idData}`).firstElementChild.firstElementChild;
            var status = targetElement.innerHTML;
            var penyelesaian = status.substring(0, 58);
            penyelesaian += status.charAt(58) === "✅" ? "❌" : "✅";
            penyelesaian += status.substring(59, 92);
            targetElement.innerHTML = penyelesaian;
        }
    });
}

// Hapus data di server dan tampilan pengguna
function hapusData(idData) {
    $.ajax({
        url: `/todolist/delete/${idData}`,
        success: function () {
            $(`#${idData}`).remove()
        }
    });
}
    
$(document).ready(function () {
    refreshTodolist();
})