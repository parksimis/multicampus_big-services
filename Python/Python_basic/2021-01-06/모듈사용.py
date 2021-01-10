# 모듈사용.py
# 사용할 모듈과 같은 폴더에 저장되어 있는 파일
# 모듈을 사용할 때
# 모듈이 저장되어 있는 공간(폴더)를 경로로 등록해서 사용해야 함.

# 모듈 패스 등록
## file - settings - project interpreter

import new_calc # 모듈명만 import
from new_calc import sub # 특정 함수 import

#print(div(7, 4)) #NameError: name 'div' is not defined
# 모듈명 사용을 안했고, 함수명을 import 하지 않아서 생기는 에러
from new_calc import * # 모듈의 전체 함수 사용
print(div(7, 4)) #모듈의 전체 함수를 불러오기 때문에 사용가능
print(new_calc.add(7, 4)) # 모듈명.함수명()으로 사용
print(sub(7, 4))
print(div(7, 4))