import requests
from pprint import pprint
from dotenv import load_dotenv
import os
search_module = __import__('04') # 04.py를 모듈화
load_dotenv()

def recommendation(title):
    # '04.py'의 search_movie 함수를 가져옴
    movie_id = search_module.search_movie(title) 
    
    # movie_id가 None이면 None을 리턴
    if not movie_id: 
        return None

    BASE_URL = 'https://api.themoviedb.org/3'
    recom_path = f'/movie/{movie_id}/recommendations'
    params = {
        'api_key': os.getenv('key'), 
        'language': 'ko-KR', 
        'region': 'KR', 
    }    

    response_recom = requests.get(BASE_URL+recom_path, params=params).json()
    
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
