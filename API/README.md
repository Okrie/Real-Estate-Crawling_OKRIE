# Real-Estate-Crawling_OKRIE

- 폐기된 도로명 주소 지번으로 변경해주는 API
- 금리의 변동된 현황 전체 크롤링

----------------------
/get_road_name
- 폐기된 도로명 주소 지번으로 변경 크롤링하여 보내주는 API

### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| roadname  |   String | Require |

### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | {"road_name": "서울특별시 강남구 개포동 660-1"} |


/get_inter_rate
- 한국은행에서 특정 년도 부터 현재까지의 년, 월, 금리 변동 크롤링하여 보내주는 API
  
### Param

| Name    | Type          |  Require  |
| ------ | ------------  | ---- |
| .  |   . | . |

### Return

| Type          |  Ex  |
| ------------  | ---- |
| JSON | {"year": "2023", "month": "01월 13일", "rate": "3.50"} |
