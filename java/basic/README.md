# index
* [Collection의 종류](#collection-종류)
* [final을 사용하는 이유](#final-사용하는-이유)
* [Collection 사용 방법](#collection-사용-방법)
    * [Map 사용 방법](#hashmap-사용-방법)

## Collection 종류
- 컬렉션을 사용하는 이유
    - 다수의 DATA를 다루는데 표준화된 클래스들을 제공해주기 때문에 DataStructure를 직접 구현하지 않고 편하게 사용할 수 있다.
    - 배열과 다르게 객체를 보관하기 위한 공간을 미리 정하지 않아도 되므로, 상황에 따라 객체의 수를 동적으로 정할 수 있다. 이는 프로그램의 공간적 효율성 또한 높여준다. 
- 컬렉션의 종류
    - List Interface
        - ArrayList
        - LinkedList
    - Map Interface
        - key-value 구조
        - HashMap : key를 기준으로 순서 보장 x 
        - LinkedHashMap : key를 기준으로 순서 보장 o
    - Set Interface
        - value에 대해서 중복된 값을 저장하지 않는다
        - HashSet : 순서를 보장하지 않음
        - LinkedHashSet : 순서를 보장
    - Stack & Queue 
        - Stack은 클래스로 직접 new 키워드를 통해 할당
        - Queue 인터페이스는 LinkedList에 new 키워드를 적용하여 사용할 수 있다.

## Collection 사용 방법


### HashMap 사용 방법
```java
// 선언
Map<Object,Object> map = new HashMap<>();

// 중복되는 key를 넣는 경우 최신화된다.
map.put(object, object);

map.get(key);

map.remove(key);

map.clear(key);

// 순회
for(Object key : map.keySet()){
    System.out.println(map.get(key));
}
```

## final 사용하는 이유
- final class : 다른 클래스에서 상속하지 못한다.
- final method : 다른 메소드에서 오버라이딩하지 못한다.
- final variable : 변하지 않는 상수값이 되어 새로 할당할 수 없는 변수가 된다. 그렇기 때문에 초기값이 초기화 값이 필수.

- final argument : 메소드 내에서 변경이 불가능하다. 

## Sting 관련 함수나 개념

- String to Object or Object to String
    ```java
        String str;
        int a = Integer.parseInt(str);
        int b = Long.parseLong(str);

        String numStr = String.valueOf(a);
    ```