import re

class StringExtractor:
    def __init__(self):
        self.patterns = [
       "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "urls": r"https?://[^\s]+",
        "phone_numbers": r"\+?[0-9\s-]{7,15}",
        "ipv4": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        "ipv6": r"\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b|(?:[0-9a-fA-F]{1,4}:){1,7}:|::(?:[0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4}",
        "malicious_domains": r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",  
        "suspicious_commands": r"\b(cmd|powershell|wget|curl|Invoke-).*", 
        "malware_tools": r"\b(metasploit|Cobalt Strike|Mimikatz|DarkComet|NanoCore|RAT|Kaiten|PhishTool|Emotet|TrickBot|Agent Tesla|NetWire|Powershell Empire)\b"
        ]
    
    def extract_strings(self, file_path):
        extracted_strings = []
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                strings = content.decode(errors='ignore')
                for pattern in self.patterns:
                    found = re.findall(pattern, strings)
                    extracted_strings.extend(found)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
        
        return extracted_strings
