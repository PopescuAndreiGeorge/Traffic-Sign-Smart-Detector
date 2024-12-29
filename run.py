from app import app 
import os

IP = '0.0.0.0'
PORT = 5000

if __name__ == '__main__':
    
    base_path = os.path.dirname(os.path.realpath(__file__))
    cert_path = os.path.join(base_path, 'cert.pem')
    key_path = os.path.join(base_path, 'key.pem')

    # Check the existence of the certificate and key files to enable HTTPS.
    # The HTTPS is mandatory for the camera access in the browser, so without the certificate and key files, 
    # the real-time camera functionality will not work.

    # To generate this SSL certificate and key files, you will need:
    #  1. openssl installed in your system: https://slproweb.com/download/Win64OpenSSL-3_4_0.exe 
    #  2. Run the following command in the terminal:
    #    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

    if os.path.exists(cert_path) and os.path.exists(key_path):
        app.run(host=IP, port=PORT, debug=True, ssl_context=(cert_path, key_path))
    
    else:
        app.run(host=IP, port=PORT, debug=True)
