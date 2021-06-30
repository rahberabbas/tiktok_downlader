import requests
import json

def downloader(link):
    print(link)
    # newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    source = "https://freevideosdowloader.tk/services/downloader_api.php"
    resp = requests.post(source, data={"url": link}, verify=True).text
    print(resp)
    links_list = json.loads(resp)["VideoResult"][0]["VideoUrl"]
    print(links_list)

downloader(link='https://www.tiktok.com/@amg_65s_bro/video/6970634217176714502')