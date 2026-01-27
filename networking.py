import socket
import http.client
import ssl

def check_http_service(ip_address, port, use_https=False):
    """
    Checks if a port on a given IP address hosts an HTTP/HTTPS service.
    
    Returns:
        A string indicating the result.
    """
    try:
        # Step 1: Basic port connectivity check
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2) # Set a timeout for the connection attempt
            s.connect((ip_address, port))
            print(f"Port {port} is open. Attempting HTTP check...")

            # Step 2: Verify HTTP service
            if use_https:
                context = ssl.create_default_context()
                conn = http.client.HTTPSConnection(ip_address, port, timeout=2, context=context)
            else:
                conn = http.client.HTTPConnection(ip_address, port, timeout=2)
            
            # Send a GET request to the root path
            conn.request("GET", "/")
            response = conn.getresponse()
            
            # Check for a successful HTTP status code and HTML content
            if 200 <= response.status < 300:
                content_type = response.getheader("Content-Type", "")
                if "text/html" in content_type or "application/json" in content_type or "text/" in content_type:
                    return f"Port {port} has an active HTTP/HTTPS service (Status: {response.status}, Content-Type: {content_type})."
                else:
                    return f"Port {port} is an active HTTP/HTTPS service (Status: {response.status}), but content might not be HTML."
            else:
                return f"Port {port} open, but HTTP request failed with status code: {response.status}."
                
    except socket.error as e:
        return f"Port {port} is closed or unreachable (Socket error: {e})."
    except http.client.HTTPException as e:
        return f"Port {port} open, but an HTTP error occurred: {e}"
    except ssl.SSLError as e:
        return f"Port {port} open, but an SSL error occurred (likely not an HTTPS port): {e}"
    except Exception as e:
        return f"An unexpected error occurred for port {port}: {e}"

# --- Example Usage ---
target_ip = "192.168.1.1"
ports_to_scan = [n for n in range(0, 65537)] # added the n for n thingy myself lol

print(f"Scanning IP: {target_ip}\n")

with open("results.txt", 'w') as file:
    file.write('')

with open("results.txt", 'w') as file:
    for p in ports_to_scan:
        is_https = (p == 443)
        result = check_http_service(target_ip, p, use_https=is_https)
        print(f"* {result}")
        print("-" * 20)
        file.write(result)
        file.write("\n")
