document.getElementById('fileInput').addEventListener('change', function(event) {
    var preview = document.getElementById('preview');
    preview.innerHTML = ''; // Clear any existing preview

    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function(e) {
        var img = document.createElement('img');
        img.src = e.target.result;
        preview.appendChild(img);
        document.getElementById('uploadContainer').style.display = 'none';
        document.getElementById('reopenButton').style.display = 'block';
        document.getElementById('signInformation').style.display = 'block';
    }

    reader.readAsDataURL(file);
});

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // TODO: Upload the image to the server
    alert('Image uploaded!');
});

document.getElementById('reopenButton').addEventListener('click', function() {
    document.getElementById('fileInput').click(); // Trigger click on file input
    document.getElementById('uploadContainer').style.display = 'block';
    document.getElementById('preview').innerHTML = '';
    document.getElementById('reopenButton').style.display = 'none';
    document.getElementById('signInformation').style.display = 'none';
});
