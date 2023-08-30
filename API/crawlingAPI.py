# 
#   CrawlingAPI.py
#   Flutter_R_Spring Project
#
#   부동산 실시간 예측을 위한 Python API 서버
#   /get_road_name
#   폐기된 도로명 주소를 받아 지번 주소로 보내줌
#   
#   /get_inter_rate
#   한국은행에서 특정 년도 부터 현재 까지의 금리를 보내줌
#
#   Created by Okrie on 2023/08/17.

from flask import Flask, request, Response
import requests
from bs4 import BeautifulSoup
import json
import csv

app = Flask(__name__)

def fix_whitespace(text):
    return ' '.join(text.split())


# 폐기된 도로명 주소 지번으로 변경 
@app.route('/get_road_name', methods=['GET'])
def get_road_name():
    search_keyword = request.args.get('roadname')
    if not search_keyword:
        return jsonify({"error": "검색 키워드를 지정하세요."}), 400


    url = f'https://www.juso.go.kr/support/AddressMainSearch.do?firstSort=none&ablYn=Y&aotYn=N&fillterHiddenValue=&searchKeyword={search_keyword}&dsgubuntext=&dscity1text=&dscounty1text=&dsemd1text=&dsri1text=&dssan1text=&dsrd_nm1text=&searchType=HSTRY&ckAblYn=on&dssearchType1=road&dscity1=&dscounty1=&dsrd_nm_idx1=%EA%B0%80_%EB%82%98&dsrd_nm1=&dsma=&dssb=&dstown1=&dsri1=&dsbun1=&dsbun2=&dstown2=&dsbuilding1='
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        road_name_element = soup.select_one('.subejct_2 .roadNameText')
        if road_name_element:
            road_name = road_name_element.get_text(strip=True)
            road_name = fix_whitespace(road_name)  # 띄어쓰기 한 칸으로 고정
            result = {"road_name": road_name}
            return Response(json.dumps(result, ensure_ascii=False), content_type="application/json"), 200
        else:
            return jsonify({"error": "도로명주소를 찾을 수 없습니다."}), 404

    return jsonify({"error": "서버 에러"}), 500


# 금리 크롤링
# 한국은행에서 특정 년도 부터 현재 까지의 금리를 보내줌
@app.route('/get_inter_rate', methods=['GET'])
def get_inter_rate():
    url = f'https://www.bok.or.kr/portal/singl/baseRate/list.do?dataSeCd=01&menuNo=200643'
    
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        interest_rate_rows = soup.select('#content > div.table.tac > table > tbody > tr')
        interest_rates = []
        for row in interest_rate_rows:
            year = row.select_one('td:nth-child(1)').get_text(strip=True)
            month = row.select_one('td:nth-child(2)').get_text(strip=True)
            rate = row.select_one('td:nth-child(3)').get_text(strip=True)

            interest_rates.append({"year": year, "month": month, "rate": rate})

        if interest_rates:
            # save_to_csv(interest_rates)
            return Response(json.dumps(interest_rates, ensure_ascii=False), content_type="application/json"), 200
        else:
            return jsonify({"error": "페이지 에러"}), 404

    return jsonify({"error": "서버 에러"}), 500





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)