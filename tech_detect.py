import subprocess

def run_tech_detect(domain):
    """
    Runs WhatWeb to detect web technologies used by the target domain.

    Args:
        domain (str): The domain name or IP address to scan.

    Returns:
        str: The WhatWeb scan output or an error message.
    """
    try:
        result = subprocess.check_output(
            ["whatweb", domain],
            stderr=subprocess.STDOUT,
            timeout=10
        )
        return result.decode().strip()
    except subprocess.TimeoutExpired:
        return "[!] Technology detection timed out."
    except subprocess.CalledProcessError as e:
        return f"[!] WhatWeb error:\n{e.output.decode().strip()}"
    except Exception as e:
        return f"[!] Tech detection failed: {str(e)}"
