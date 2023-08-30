# 
#   월별금리크롤링.py
#   Flutter_R_Spring Project
#
#   부동산 실시간 예측을 위한 Python API 서버
#
#   save_to_csv
#   받은 정보를 합해 csv로 저장시켜주는 함수
#   year, month, rate 컬럼으로 추가하여 저장
#
#   /get_inter_rate
#   한국은행에서 특정 년도 부터 현재 까지의 금리를 보내줌
#   
#   Created by Okrie on 2023/08/15.

from flask import Flask, request, Response
import requests
from bs4 import BeautifulSoup
import json
import csv

app = Flask(__name__)

#   공백 제거
def fix_whitespace(text):
    return ' '.join(text.split())

#   받은 정보를 합해 csv로 저장시켜주는 함수
#   year, month, rate 컬럼으로 추가하여 저장
def save_to_csv(data):
    with open('금리.csv', 'w', newline='', encoding='utf-8') as csvfile:  # 인코딩을 cp949로 변경
        fieldnames = ['year', 'month', 'rate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow({"year": item['year'], "month": item['month'], "rate": item['rate']})
            


#   한국은행에서 특정 년도 부터 현재 까지의 금리를 크롤링 하여 csv로 저장, json으로 보내줌
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
            save_to_csv(interest_rates)
            return Response(json.dumps(interest_rates, ensure_ascii=False), content_type="application/json"), 200
        else:
            return jsonify({"error": "머고"}), 404

    return jsonify({"error": "서버 에러"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
