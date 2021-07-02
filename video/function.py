import requests
from urllib.parse import parse_qsl, urlparse
import time

def withwater_download(urls):
    time.sleep(5)
    HEADERS = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'video',
        'Referer': 'https://www.tiktok.com/',
        'Accept-Language': 'en-US,en;q=0.9,bs;q=0.8,sr;q=0.7,hr;q=0.6',
        'sec-gpc': '1',
        'Range': 'bytes=0-',
    }

    cookies = {
        'tt_webid': '6969977128956642817',
        'tt_webid_v2': '6969977128956642817'
    }

    response = requests.get(urls, cookies=cookies, headers=HEADERS)
    irt = response.text.split('"playAddr":"')[1].split('"')[0].replace(r'\u0026', '&')
    video_url = irt
    url = urlparse(video_url)

    params = tuple(parse_qsl(url.query))
    request = requests.Request(method='GET',
                                url='{}://{}{}'.format(url.scheme,
                                                        url.netloc, url.path),
                                cookies=cookies,
                                headers=HEADERS,
                                params=params)
    prepared_request = request.prepare()
    session = requests.Session()
    response = session.send(request=prepared_request)
    response.raise_for_status()
    return response