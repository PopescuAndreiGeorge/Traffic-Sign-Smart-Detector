import { serverIp } from './utils.js';

document.getElementById('fileInput').addEventListener('change', function (event) {
    var preview = document.getElementById('preview');
    preview.innerHTML = ''; // Clear any existing preview

    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function (e) {
        var img = document.createElement('img');
        img.src = e.target.result;
        preview.appendChild(img);
    }

    reader.readAsDataURL(file);
});

document.getElementById('uploadForm').addEventListener('submit', function (event) {
    event.preventDefault();

    var xhr = new XMLHttpRequest();
    var formData = new FormData();

    xhr.open('POST', `https://${serverIp}:5000/sign`, true);
    formData.append('image', document.getElementById('fileInput').files[0]);

    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.getElementById('signName').textContent = response.name;
            document.getElementById('signDescription').textContent = response.meaning;

            document.getElementById('uploadContainer').style.display = 'none';
            document.getElementById('signInformation').style.display = 'block';
            document.getElementById('reuploadBtn').style.display = 'block';
        } else if (xhr.status === 400) {
            showAlert('Oops! That doesn\'t look like a valid image file. Please try again with a different file.');
        }
        else {
            console.error('Error:', xhr.statusText);
        }
    };

    xhr.send(formData);
});

document.getElementById('reuploadBtn').addEventListener('click', function () {
    document.getElementById('fileInput').click(); // Trigger click on file input
    document.getElementById('uploadContainer').style.display = 'block';
    document.getElementById('preview').innerHTML = '';
    document.getElementById('reuploadBtn').style.display = 'none';
    document.getElementById('signInformation').style.display = 'none';
});

document.getElementById('cameraBtn').addEventListener('click', function () {

    document.getElementById('uploadContainer').style.display = 'none';
    document.getElementById('preview').innerHTML = '';
    document.getElementById('reuploadBtn').style.display = 'none';

    window.location.href = '/camera';
});

function showAlert(message) {
    document.getElementById('alertMessage').textContent = message;
    document.getElementById('customAlert').style.display = 'block';
}

function closeAlert() {
    document.getElementById('customAlert').style.display = 'none';
}
