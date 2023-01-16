import requests
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()

def search_movie(title):    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = { 
        'query' : title,
        'api_key': os.getenv('key'),
        'language': 'ko-KR',
        'region': 'KR',
    }
    
    response = requests.get(BASE_URL+path, params=params).json()

    movie_id = response.get('results')[0].get('id') if response.get('results') else None

    return movie_id

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    pprint(search_movie('기생충'))
    # 496243
    pprint(search_movie('그래비티'))
    # 959101
    pprint(search_movie('검색할 수 없는 영화'))
    # None
