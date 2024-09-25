# SecHeaderFinding
This Python script checks for security headers from a provided URL. It sends a HEAD request to the URL and extracts common security-related headers like Content-Security-Policy, Strict-Transport-Security, X-Content-Type-Options, and others. The script is designed to be executed from the command line, with the URL passed as an argument.

# *Key Features:*
*Command-Line Argument Input: Accepts a URL as a command-line argument, making it easy to use in terminal or script automation.

*Security Headers Detection: Identifies and extracts common security-related headers such as:

Content-Security-Policy
Strict-Transport-Security
X-Content-Type-Options
X-Frame-Options
X-XSS-Protection
Referrer-Policy
Permissions-Policy
*Efficient Request Method: Uses a HEAD request to only fetch headers, reducing bandwidth and increasing speed since the body of the page is not downloaded.

*Error Handling: Includes exception handling to manage cases such as request timeouts or invalid URLs, ensuring the script doesn’t crash unexpectedly.

*Simple Output: Outputs the found security headers in a clear and readable format, helping users quickly assess a website’s security configuration.

*Modular Design: The get_security_headers function can easily be reused or modified for more advanced functionality if needed.

# *Usage
Run the script and pass the URL as a command-line argument:

python security_headers.py https://example.com
