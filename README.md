# Real-Estate-Crawling_OKRIE

Python Flask로 Flutter로 제작한 매매, 전세가 예측 어플리케이션에서 요청하는 서버 제작    
프로젝트 내 크롤링이 필요한 부분 API로 제작

            
<a href="https://drive.google.com/file/d/1DpbfSfgAn9wvw47s7ArMIJdveqDGZ9Yb/view?usp=sharing">![cover](https://github.com/Okrie/Real-Estate-Spring_OKRIE/blob/main/Real%20Estate_Spring.png)</a>     

---

### 기능 설명
![image](https://github.com/Okrie/Real-Estate-Crawling_OKRIE/assets/24921229/266c675d-e262-451e-a7e7-ea8fc66830db)

- 폐기된 도로명 주소 지번으로 변경해주는 API
- 금리의 변동된 현황 전체 크롤링
  
---
---
    
#### 기술 스택
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=git,github,vscode,python" />
  </a>
    <img src="https://cdn.icon-icons.com/icons2/512/PNG/512/prog-flask_icon-icons.com_50797.png" height="53" title="Flask">
    <img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/slack_tile_logo_icon_168820.png" height="53" title="Slack">
    <img src="https://cdn.icon-icons.com/icons2/3913/PNG/512/miro_logo_icon_248450.png" height="53" title="Miro">
    <img src="https://cdn.icon-icons.com/icons2/3221/PNG/512/docs_editor_suite_docs_google_icon_196688.png" height="53" title="Google Docs">
</p>

---
---


### 기능 상세 설명

/get_road_name
- 폐기된 도로명 주소 지번으로 변경

#### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| roadname  |   String | Require |

#### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | {"road_name": "서울특별시 강남구 개포동 660-1"} |
    
/get_inter_rate
- 금리의 변동된 현황 전체 크롤링

#### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
|   |    |  |

#### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | [{"year": "2023", "month": "01월 13일", "rate": "3.50"}, {"year": ...}] |
