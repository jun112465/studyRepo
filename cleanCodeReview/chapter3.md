

# CHAPTER3 - 함수

1. [작게 만들어라](#작게-만들어라!)
2. [한 가지만 해라!](#한-가지만-해라!)
3. [함수 당 추상화 수준은 하나로](#함수-당-추상화-수준은-하나로)


## 작게 만들어라!
- 함수의 길이는 더 작을수록 좋다
- ex)
  ~~~java
  public static String renderPageWithSetupsAndTeardowns(
    PageData pageData, boolean isSuite) throws Exception{
    if(isTestPage(pageData))
      includeSetupAndTeardownPages(pageData, isSuite);
    return pageData.getHtml();
  }
  ~~~
- 블록과 들여쓰기
  - is/else, while 문 등에 들어가는 블록은 한 줄 혹은 두 줄이어야 한다.
    
## 한 가지만 해라!
- 함수가 ***한 가지***만 하는지 판단하는 방법
  - 단순히 다른 표현이 아니라 의미있는 이름으로 다른 함수를 추출할 수 있다면 그 함수는 여러 작업을 하는 것이다
## 함수 당 추상화 수준은 하나로
- 함수 내 모든 문장의 추상화 수준이 동일해야 한다. 

## switch 문
## 서술적인 이름을 사용하라!
## 함수 인수
## 부수 효과를 일으키지 마라!
## 명령과 조회를 분리하라!
## 오류 코드보다 예외를 사용하라!
## 반복하지 마라!
## 구조적 프로그래밍
## 함수를 어떻게 짜죠?
## 결론

