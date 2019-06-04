# msc-login
[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/NetworkChris/msc-login)

Script to obtain the session token when using the RESTAPI in conjunction with a Cisco ACI Multi-Site Controller


Install requirements

```
pip install -r requirements.txt
```

Import this module into other scripts and pass through the following:

* Multi-Site Controller Hostname/IP Address
* Multi-Site Username
* Multi-Site Password

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
