function deletePhotoModalHandler(image_id, img_name) {
    delete_modal.showModal();
    document.getElementById("delete_modal_btn_id_value").value = image_id;
    document.getElementById("itr_text").innerText = img_name;
}


async function deletePhoto() {
    const image_id = document.getElementById("delete_modal_btn_id_value").value;

    if (image_id == undefined || image_id == null || image_id == '') return;

    const _img_elem = document.getElementById('F_' + image_id);

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const delete_req = await fetch("/delete/" + image_id + "/", {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        }
    })

    if (delete_req.ok && delete_req.status == 200) {
        const res = await delete_req.json();
        const RT = JSON.parse(res);
        if (RT.msg === 'success') {
            document.getElementById("delete_modal_btn_id_value").value = '';
            delete_modal.close();
            _img_elem.parentElement.removeChild(_img_elem);
            return;

        }
    }

    document.getElementById("err_msg").innerText = "Something went wrong";


}
