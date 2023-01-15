import requests
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv('key')

def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    URL1 = f'https://api.themoviedb.org/3/search/movie?api_key={key}&query={title}&language=ko-KR&region=KR'

    respons1 = requests.get(URL1).json()
    data1 = respons1['results']

    if data1:
        result1 = data1[0]['id']
    else:
        return None

    URL2 = f'https://api.themoviedb.org/3/movie/{result1}/credits?api_key={key}&language=ko-KR&region=KR'

    response2 = requests.get(URL2).json()
    result2={
        'cast' : [i['name'] for i in response2['cast'] if i['cast_id'] < 10],
        'crew' : [j['name'] for j in response2['crew'] if j['department'] == 'Directing']
    }
    
    return result2

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
