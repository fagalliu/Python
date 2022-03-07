import requests
import browser_cookie3
import os
from urllib.parse import urlparse
import pandas as pd
from requests.exceptions import TooManyRedirects


DOMAIN = 'www.narcity.com'
URL = 'https://www.narcity.com/core/community/redirects/?limit=25&offset={}'
COOKIES_PATH = os.path.join(os.path.expandvars("%userprofile%"), "AppData\\Local\\Google\\Chrome\\User Data\\"
                                                                 "Profile 1\\Network\\Cookies")
COOKIES = browser_cookie3.chrome(domain_name=DOMAIN, cookie_file=COOKIES_PATH)


def _make_get_request(url):
    return requests.get(url)


def _get_request_with_cookies(url):
    response = requests.get(url, cookies=COOKIES)

    return response


def _get_all_redirect(url_offset):
    response = _get_request_with_cookies(url_offset)
    print(response)
    response = response.json()
    if response:
        for re in response:
            old_equal_slug = compare(re['old_url'], re['new_url'])
            if old_equal_slug:
                _exception_in_get_request(re['new_url'], re['old_url'])
        return True
    else:
        return False


def compare(old, new):
    parsed_url = urlparse(new)
    if parsed_url.netloc in (None, '', 'www.narcity.com', 'narcity.com'):
        return parsed_url.path.strip('/') == old
    else:
        return False


def export_to_csv(new, old):
    data = dict()
    new_url = []
    old_ulr = []
    new_url.append(new)
    old_ulr.append(old)

    data['new_url'] = new_url
    data['old_ulr'] = old_ulr

    df = pd.DataFrame(data, columns=['new_url', 'old_ulr'])
    df.to_csv(r'Redirect_urls.csv', mode='a', index=False, header=False)


def _exception_in_get_request(new_url, old_url):
    if not new_url.startswith('https://www.narcity.com'):
        new_url = "https://www.narcity.com{}".format(new_url)

    try:
        _make_get_request(new_url)
    except TooManyRedirects:
        print("- TooManyRedirects found")
        export_to_csv(new_url, old_url)


def main():
    i = 0
    while True:
        print("\n", i)
        url_offset = URL.format(i)
        if _get_all_redirect(url_offset):
            i += 25
        else:
            break


if __name__ == '__main__':
    main()
