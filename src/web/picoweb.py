
"""
picoweb - WiFi connectivity and web interface module for remote car control
FIXED VERSION with non-blocking socket
"""
import network
import socket
import time

# Module state variables
wlan = None
server_socket = None
is_connected = False
ip_address = None
AUTOREFRESH = 2 # seconds

# Configuration
SSID = 'ITEK1st'
PASSWORD = 'itekf25v' 
PORT = 80



def init_wifi(ssid=None, password=None):
    """
    Initialize and connect to WiFi
    Returns: True if connected, False otherwise
    """
    global wlan, is_connected, ip_address, SSID, PASSWORD

    if ssid:
        SSID = ssid
    if password:
        PASSWORD = password

    print('[WiFi] Initializing...')
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print(f'[WiFi] Connecting to {SSID}...')
        wlan.connect(SSID, PASSWORD)

        # Wait for connection (10 second timeout)
        max_wait = 10
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            print('[WiFi] Waiting for connection...')
            time.sleep(1)

    # Check connection status
    if wlan.status() != 3:
        print('[WiFi] Connection failed!')
        is_connected = False
        return False
    else:
        is_connected = True
        status = wlan.ifconfig()
        ip_address = status[0]
        print(f'[WiFi] Connected! IP: {ip_address}')
        return True

def get_ip_address():
    """Returns the current IP address or None if not connected"""
    return ip_address

def is_wifi_connected():
    """Check if WiFi is currently connected"""
    return is_connected and wlan and wlan.isconnected()

def start_server():
    """
    Start the web server socket
    Call this once during initialization
    """
    global server_socket

    if not is_wifi_connected():
        print('[Web Server] Cannot start - not connected to WiFi')
        return False

    try:
        addr = socket.getaddrinfo('0.0.0.0', PORT)[0][-1]
        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(addr)
        server_socket.listen(1)  # FIXED: Added parameter
        server_socket.setblocking(False)  # CRITICAL FIX: Non-blocking mode

        print(f'[Web Server] Listening on {ip_address}:{PORT}')
        print(f'[Web Server] Access at: http://{ip_address}')
        return True
    except Exception as e:
        print(f'[Web Server] Failed to start: {e}')
        return False


def get_server_status():
    """
    Returns a dictionary with server status information
    Useful for debugging
    """
    return {
        'wifi_connected': is_wifi_connected(),
        'ip_address': ip_address,
        'server_running': server_socket is not None,
    }

def stop_server():
    """Stop the web server and close socket"""
    global server_socket

    if server_socket:
        server_socket.close()
        server_socket = None
        print('[Web Server] Stopped')

def disconnect_wifi():
    """Disconnect from WiFi"""
    global wlan, is_connected, ip_address

    if wlan:
        wlan.disconnect()
        wlan.active(False)
        is_connected = False
        ip_address = None
        print('[WiFi] Disconnected')

