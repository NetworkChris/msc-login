#! /usr/bin/env python

"""
This script completes the login process for the Cisco Multi-Site Controller
and returns the token required for future API calls
"""

def login(msc_hostname, msc_username, msc_password):

    import requests
    import urllib3
    import json

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    msc_credentials = {
        "username": msc_username,
        "password": msc_password
        }

    msc_headers = {
        "Content-Type": "application/json",
        "cache-control": "no-cache"
        }

    msc_api_base = "https://{msc}/api/v1"
    msc_auth_url = msc_api_base + "/auth/login"
    msc_url = msc_auth_url.format(msc=msc_hostname)
    msc_body = json.dumps(msc_credentials, indent=4)

    msc_login = requests.request(
        "POST",
        msc_url,
        headers=msc_headers,
        data=msc_body,
        verify=False)

    msc_response = json.loads(msc_login.text)
    msc_token = msc_response["token"]

    return msc_token

if __name__ =='__main__':
    login()
