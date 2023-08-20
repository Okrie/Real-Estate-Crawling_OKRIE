from flask import Flask, request, Response
import requests
from bs4 import BeautifulSoup
import json
import csv

app = Flask(__name__)

def fix_whitespace(text):
    return ' '.join(text.split())

def save_to_csv(data):
    with open('결과_도로명주소.csv', 'w', newline='', encoding='cp949') as csvfile:  # 인코딩을 cp949로 변경
        fieldnames = ['new_address', 'road']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for road_name in data:
            writer.writerow({'new_address': road_name})
            


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


@app.route('/get_road_names', methods=['GET'])
def get_road_names():
    print("진행중")
    road_names = []
    with open('강남구_시군구_도로명.csv', 'r', encoding='cp949') as csvfile:  # 인코딩을 cp949로 변경
        reader = csv.DictReader(csvfile, fieldnames=['x'])
        next(reader)
        for row in reader:
            road_name = fix_whitespace(row['x'])
            road_names.append(road_name)

    if not road_names:
        return jsonify({"error": "도로명주소 목록이 비어있습니다."}), 404

    results = []
    for road_name in road_names:
        url = f'https://www.juso.go.kr/support/AddressMainSearch.do?firstSort=none&ablYn=Y&aotYn=N&fillterHiddenValue=&searchKeyword={road_name}&dsgubuntext=&dscity1text=&dscounty1text=&dsemd1text=&dsri1text=&dssan1text=&dsrd_nm1text=&searchType=HSTRY&ckAblYn=on&dssearchType1=road&dscity1=&dscounty1=&dsrd_nm_idx1=%EA%B0%80_%EB%82%98&dsrd_nm1=&dsma=&dssb=&dstown1=&dsri1=&dsbun1=&dsbun2=&dstown2=&dsbuilding1='

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            road_name_element = soup.select_one('.subejct_2 .roadNameText')
            if road_name_element:
                found_road_name = fix_whitespace(road_name_element.get_text(strip=True))
                results.append(found_road_name)
                results.append(road_name)
                # print(results)

    if results:
        save_to_csv(results)
        return Response(json.dumps(results, ensure_ascii=False), content_type="application/json"), 200
    else:
        return jsonify({"error": "검색된 도로명주소가 없습니다."}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
