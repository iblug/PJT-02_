import requests
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv('key')

def search_movie(title):
    pass
    # 여기에 코드를 작성합니다.
    
    # BASE_URL = 'https://api.themoviedb.org/3'
    # path = '/search/movie'
    # params = { 
    #     'api_id': key,
    #     # 'language': 'ko-KR',
    #     # 'region': 'KR',
    #     'query' : f'{title}'
    # }
    # response = requests.get(BASE_URL+path, params=params).json()
    
    URL = f'https://api.themoviedb.org/3/search/movie?api_key={key}&language=ko-KR&region=KR&query={title}'
    response = requests.get(URL).json()

    # print(response.url)
    # print(type(title))
    data = response['results']

    result = data[0]['id'] if data else None
    # if data:
    #     result = data[0]['id']
    # else:
    #     return None

    return result

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
