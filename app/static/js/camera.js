// Get access to the video and canvas elements

import { serverIp } from './utils.js';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

function isMobileDevice() {
    return /Mobi|Android/i.test(navigator.userAgent);
}

let constraints =
{
    video: {
        facingMode: isMobileDevice() ? { exact: 'environment' } : 'user'
    }
};

// Access the device camera and stream to video element
navigator.mediaDevices.getUserMedia(constraints)
    .then((stream) => {
        video.srcObject = stream;
        video.play();
    })
    .catch((err) => {
        console.error('Error accessing the camera: ', err);
    });

setInterval(() => {
    if (video.readyState === video.HAVE_ENOUGH_DATA) {

        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        canvas.toBlob((blob) => { 
            const formData = new FormData();
            formData.append('image', blob, 'frame.png');

            const endpoint = `https://${serverIp}:5000/sign`;

            fetch(endpoint, { 
                method: 'POST', 
                body: formData
            })
            .then(response => response.json())
            .then(sign => { 
                document.getElementById('signName').textContent     = sign.name;
                document.getElementById('signCategory').textContent = sign.category;
                document.getElementById('signType').textContent     = sign.type;
                document.getElementById('signMeaning').textContent  = sign.meaning;
                document.getElementById('signRules').textContent    = sign.rules;
            })
            .catch((error) => { 
                console.error('Error:', error); 
            });
        }, 'image/png');
    }
}, 1000);  // 1 frames per second
