document.getElementById('img_file').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file.type.startsWith('image/')) {
        const img = document.getElementById('img_area');
        img.src = URL.createObjectURL(file);
    } else {
        alert('Please select an image file.');
    }
});
