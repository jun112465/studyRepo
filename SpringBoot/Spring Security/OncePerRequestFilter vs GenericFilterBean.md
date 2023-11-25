# GenericFilterBean
- Filter를 확장하여 Spring에서 제공하는 filter.
- 기존 Filter에서 얻어올 수 없는 정보였던 Spring의 설정 정보를 가져올 수 있게 확장된 추상 클래스
- 해당 filter는 서블릿마다 호출이 된다.
    - 서블릿은 사용자의 요청을 받으면 서블릿을 생성해 메모리에 저장해두고, 같은 클라이언트의 요청을 받으면 생성해둔 서블릿 객체를 재활용하여 요청을 처리한다.
- 문제는 의도치 않은 경우에 Filter가 두번씩 적용되는 경우가 있을 수 있다.
    - ![image](https://velog.velcdn.com/images/jmjmjmz732002/post/dee34cf5-0d55-4267-9f78-ef32b20383c1/image.png)
    - Spring Security에서 인증과 인가 또한 Filter로 구현되어 있다.
    - 예를 들어, 그림과 같이 API 0에서 요청을 처리하고 API 1로 redirect 시킨다고 가정하자.
    - 클라이언트는 한번의 요청을 한 것 뿐이지만 흐름상 요청을 두번 한 것과 같이 된다. 쓸데없는 자원만 낭비하는 셈이다.
- 이러한 문제를 해결하기 위해 OncePerRequestFilter가 등장했다.

# OncePerRequestFilter
- 모든 서블릿에서 일관된 요청을 처리하기 위해 만들어진 필터이다.
- 이 추상 클래스를 구현한 필터는 사용자의 요청당 단 한번만 실행되는 필터를 만들 수 있다.
- OncePerRequestFilter를 상속하여 구현한 경우 doFilter 대신 doFilterInternal 메서드를 구현하면 된다.
