import requests as req
import argparse as argp
import re
from wafw00f.main import WAFW00F

parser = argp.ArgumentParser()
parser.add_argument("-u")
parser.add_argument("-O",action="store_true")
arg = parser.parse_args()
api_key = "SECURITYTRAILS_API_KEY"

def domain2domain(u):
    repl = ["https://","http://","https:/","http:/","https:","http:",":","/"]
    for i in repl:
       return u.replace(i,"")

def originIP(): 
    ip = domain2domain(arg.u) if arg.u else ""
    if ip == "":
        print("Invalid Domain")
        return
    url = f"https://api.securitytrails.com/v1/history/{ip}/dns/a"
    headers = {"apikey": api_key}
    resp = req.get(url, headers=headers)
    ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b",resp.text)
    for i in set(ips):
        print(i)
    return list(ips)


"""
Waf detection is causing error.

"""

def checkWaf(ips):
    for ip in ips:
        try:
            waf = WAFW00F("http://" + str(ip)).identwaf()
            if waf and len(waf) > 0:
                print(f"{ip} -> {waf[0][0]}")
            else:
                print(f"{ip} -> [!] No WAF detected")
        except KeyboardInterrupt:
            print("User Cancelled Operation")
            return
        except Exception:
            print(f"{ip} -> [!] No WAF detected")

if arg.O and arg.u:
    print("Historical IPs")
    ips = originIP()
    print("Finding WAF")
    checkWaf(ips)
elif arg.u:
    originIP()
else:
    pass