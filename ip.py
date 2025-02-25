import socket
import requests

def get_local_ip():
    """Get the local IP address of the device."""
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_public_ip():
    """Get the public IP address using an external service."""
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        public_ip = response.json()["ip"]
        return public_ip
    except requests.RequestException:
        return "Could not retrieve public IP"

if __name__ == "__main__":
    print(f"Local IP Address: {get_local_ip()}")
    print(f"Public IP Address: {get_public_ip()}")
