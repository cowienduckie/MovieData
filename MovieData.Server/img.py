import requests
import json
import requests # request img from web
import shutil # save img locally

def getImg(id):
    response_API = requests.get('https://imdb-api.com/en/API/Posters/k_bkxdtr14/'+str(id))
    #print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    if len(parse_json['posters']):
        url = parse_json['posters'][0]['link']


        file_name = '../MovieData.Client/wwwroot/images/'+str(id)+'.jpg'
        res = requests.get(url, stream = True)

        if res.status_code == 200:
            with open(file_name,'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',file_name)
        else:
            print('Image Couldn\'t be retrieved')
        return url

