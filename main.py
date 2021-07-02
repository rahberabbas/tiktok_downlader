import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

# r = requests.get('https://tiktokdownload.online/results', headers=headers)
# print(r.status_code)

r = requests.post('https://tiktokdownload.online/results', headers=headers, data={'id': 'https://www.tiktok.com/@khaby.lame/video/6949115989145537797?sender_device=pc&sender_web_id=6969977128956642817&is_from_webapp=v1&is_copy_url=0'})
print(r.text)