# msc-login
Script to obtain the session token when using the RESTAPI in conjunction with a Cisco ACI Multi-Site Controller


Install requirements

```
pip install -r requirements.txt
```

Import this module into other scripts and pass through the following:

* MultiSite Controller Hostname/IP Address
* MultiSite Username
* MultiSite Password

Usage Example:

```
token = msc.login("mschost.cisco.com", "admin", "cisco123")
```

Example of the generated token being inserted into the header:

```
headers = {
"Content-Type": "application/json",
"cache-control": "no-cache"
"Authorization": "Bearer " + token
}
```
