
import re

def validate_ip(ip):
    pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    ips = ip.split(":")
    return ips[0] if re.match(pattern, ips[0]) else None

print(validate_ip("10.22.253.130:34120:X20"))