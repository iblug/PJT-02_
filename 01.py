import requests
from dotenv import load_dotenv
import os
load_dotenv()

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': os.getenv('key'),
        'language': 'ko-KR',
        'region': 'KR'
    }

    response = requests.get(BASE_URL+path, params=params).json()
    data = response['results']
    return len(data)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
