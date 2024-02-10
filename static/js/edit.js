let img_blob_data = null;
let base64_for_ai_img = null;

Flmngr.load(
    { apiKey: "kEKofpMi", },
    { onImgPenLoaded: () => { attachOnClickListenerToButton(); }
});

function attachOnClickListenerToButton() {
    let elLoading = document.getElementById("loading");
    elLoading.parentElement.removeChild(elLoading);
    editImage(handlerFork=false);

    document.getElementById('btn-ai-btn').style.zIndex = document.getElementById('btn-ai-btn').style.zIndex + 9;
}
async function sendAIPhotoGenReq() {
    const prompt_data = document.getElementById("prompt_data").value;
    const negative_prompt = document.getElementById("negative_prompt").value;

    if (prompt_data != undefined && prompt_data != null && prompt_data != '') {

        const formData = new FormData();

        formData.append('init_image', img_blob_data);
        formData.append('init_image_mode', "IMAGE_STRENGTH");
        formData.append('image_strength', 0.35);
        formData.append('cfg_scale', 5);
        formData.append('samples', 1);
        formData.append('text_prompts[0][text]', prompt_data)
        formData.append('text_prompts[0][weight]', 1);

        if (negative_prompt != undefined && negative_prompt != null && negative_prompt != '') {
            formData.append('text_prompts[1][text]', negative_prompt)
            formData.append('text_prompts[1][weight]', -1);
        }

        document.getElementById('err_msg').innerText = "Wait! We're processing the image.."
        
        const img_ai_req = await fetch("https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image", {
            mode: 'no-cors',
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Authorization': "Bearer sk-kw3V2MrkzlVD2YmcUNBcVf0noSI9FggUAkCF63tmn1PLFpPA",
            },
            body: formData,
        });



        if (img_ai_req.ok && img_ai_req.status === 200) {
            document.getElementById('err_msg').innerText = "";
            const ai_response = await img_ai_req.json();
            console.log(ai_response);
            base64_for_ai_img = ai_response.artifacts[0].base64;
            ai_img_update_prompt_modal.close();
            editImage(handlerFork=true)

        } else {
            document.getElementById('err_msg').innerText = "Something went wrong";
        }

    }
    else {
            document.getElementById('err_msg').innerText = "Enter a prompt";
    }

}

function aiGenImage(){
    return "data:image/png;base64," + base64_for_ai_img
}

function resizeImageBlob(blob) {
    return new Promise((resolve, reject) => {
        const canvas = document.createElement('canvas');
        canvas.width = 1024;
        canvas.height = 1024;

        const ctx = canvas.getContext('2d');

        const img = new Image();
        img.src = URL.createObjectURL(blob);

        img.onload = () => {
            ctx.drawImage(img, 0, 0, 1024, 1024);

            const resizedBlob = canvas.toBlob(
                (resizedBlob) => {
                    URL.revokeObjectURL(img.src);
                    canvas.width = canvas.height = 0;
                    resolve(resizedBlob);
                },
                blob.type,
                1
            );

        };

        img.onerror = (error) => {
            URL.revokeObjectURL(img.src);
            reject(error);
        };
    });
}

