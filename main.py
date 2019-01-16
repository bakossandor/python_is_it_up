import requests


def isup(site):
    r = requests.get(f"https://{site}")
    return f"The {site} is up" if r.status_code == 200 else f"The {site} is not up"