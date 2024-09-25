import requests
import sys

# List of common security-related headers
security_headers = [
    'Content-Security-Policy', 
    'Strict-Transport-Security', 
    'X-Content-Type-Options', 
    'X-Frame-Options', 
    'X-XSS-Protection', 
    'Referrer-Policy',
    'Permissions-Policy',
    'Feature-Policy',
    'Public-Key-Pins',
]

def get_security_headers(url):
    try:
        # Send a HEAD request to the URL
        response = requests.head(url, timeout=10)
        
        headers = response.headers
        
        # Filter and display only security headers
        found_headers = {header: headers.get(header) for header in security_headers if header in headers}
        
        if found_headers:
            print(f"Security headers for {url}:")
            for header, value in found_headers.items():
                print(f"{header}: {value}")
        else:
            print(f"No security headers found for {url}.")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Check if URL is passed as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python security_headers.py <URL>")
    sys.exit(1)

# Get the URL from command-line argument
url = sys.argv[1]
get_security_headers(url)
