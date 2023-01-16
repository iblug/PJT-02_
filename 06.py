import requests
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()

def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    search_path = '/search/movie'
    params = {
        'api_key': os.getenv('key'), 
        'query': title, 
        'language': 'ko-KR', 
        'region': 'KR', 
    }
    response_search = requests.get(BASE_URL+search_path, params=params).json()
    if response_search.get('total_results') == 0:
        return None

    movie_id = response_search.get('results')[0].get('id')

    path_credits = f'/movie/{movie_id}/credits'

    response_credits = requests.get(BASE_URL+path_credits, params = params).json()
    # print(requests.get(BASE_URL+path_credits, params = params).url)
    result_credits={
        'cast' : [cast['name'] for cast in response_credits.get('cast') if cast.get('cast_id') < 10],
        'crew' : [crew['name'] for crew in response_credits.get('crew') if crew.get('department') == 'Directing']
    }
    
    return result_credits

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
