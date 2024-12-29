
export var serverIp = '192.168.113.100';

export async function getServerIp() {
    try {
        fetch(`https://${serverIp}:5000/api/ip`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            serverIp = data.ip;
            console.log("Server IP Address:", serverIp);
        })
        .catch(error => {
            console.error('Error fetching IP address:', error);
        });

    } catch (error) {
        console.error('Error fetching IP address:', error);
    }
}

getServerIp();
