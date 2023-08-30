# Real-Estate-Crawling_OKRIE

프로젝트 내 크롤링이 필요한 부분 API로 제작
- 폐기된 도로명 주소 지번으로 변경해주는 API
- 금리의 변동된 현황 전체 크롤링

----------------------
/get_road_name
- 폐기된 도로명 주소 지번으로 변경

### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| roadname  |   String | Require |

### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | {"road_name": "서울특별시 강남구 개포동 660-1"} |
