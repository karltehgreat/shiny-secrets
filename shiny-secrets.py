#!/usr/bin/env python3

import requests
params = {"words": 10, "paragraphs": 1, "format": "json"}
response = requests.get(f"https://api-example.local/", params=params,
 headers={
   "localAPI-Host": "api-example.local",
   "localAPI-Key": "8ugS5gDLVzKDHRez0QwLgKLXX369TJNKegMslrMwAPGHn30kUHajRv2N91L8kvxMwc9mvoATPgsoy7hiBAtkAOb0QIayDlTysSAOwPHb5aACFP5egmYeru7c5pmzLITn"
 }
)
print (type(response.json()))
print(response.json())

-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABDatt+BA9
n06PgkmJ5sZEJ9AAAAGAAAAAEAAAAzAAAAC3NzaC1lZDI1NTE5AAAAIEUJSQ/swQ5m1Jnk
6yRVS3e3q/FIZQ4lgOzb3ADn57DYAAAAoFV6lLP6kCl2HrUUB4piiV96zTwtq3M5smy/Nt
zVicrzw/XXGuPNPdgkBUWkOE+2wnyLuaEg81x0PLnAHofgfsHFpnsMubiPF7rKA2YOOorM
IMYN6DeK3Gk/sCGVO0Ghf9NDLmM5azru/4suds1Hc06yTsoe0tkx7FFwkfMLBr9OQIosbO
yIqQTsaUMUd68Af0fUc+9aAMjK7mclZ756ie0=
-----END OPENSSH PRIVATE KEY-----


8ugS5gDLVzKDHRez0QwLgKLXX369TJNKegMslrMwAPGHn30kUHajRv2N91L8kvxMwc9mvoATPgsoy7hiBAtkAOb0QIayDlTysSAOwPHb5aACFP5egmYeru7c5pmzLITn

