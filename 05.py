import requests
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()

def recommendation(title):
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path_search = '/search/movie'
    params = {
        'api_key': os.getenv('key'), 
        'query': title, 
        'language': 'ko-KR', 
        'region': 'KR', 
    }
    response_search = requests.get(BASE_URL+path_search, params=params).json()
    # print(requests.get(BASE_URL+search_path, params=params).url)
    if response_search.get('total_results') == 0:
        return None


    movie_id = response_search.get('results')[0].get('id')


    # if data1:
    #     result1 = data1[0]['id']
    # else:
    #     return None

    recom_path = f'/movie/{movie_id}/recommendations'
    # URL2 = f'https://api.themoviedb.org/3/?api_key={key}&language=ko-KR&region=KR'

    response_recom = requests.get(BASE_URL+recom_path, params=params).json()
    # print(requests.get(BASE_URL+recom_path, params=params).url)
    
    data = response_recom.get('results')
    
    movie_recommend=[]
    if data:
        for movie in data:
            movie_recommend.append(movie.get('title')) 

    return movie_recommend

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
