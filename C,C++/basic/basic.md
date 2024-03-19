### 함수포인터
- 함수의 이름은 곧 포인터다.
- 함수포인터는 함수의 주소를 저장하여, 함수를 호출할 수 있습니다.
- 사용 이유
    1. 콜백 함수 등록
    2. 다형성 구현
    3. 런타임 다양한 동작 지정
    4. 모듈화와 유지 보수성.
    
```c
// 함수의 기본 형식
return_type (*pointer_name)(parameter_list);

int (*ptr)(int);

int add(int a, int b);
```

```c
//구조체 활용
#include <stdio.h>

typedef struct math{

    int (*add)(int, int);
    int (*subtract)(int, int);
}MathFunctions;

int add(int a, int b){
    return a+b;
}
int subtract(int a, int b){
    return a-b;
}
void math_functions_init(MathFunctions *mf){
    mf->add = add;
    mf->subtract = subtract;
}

int main(){
    MathFunctions math_func;
    math_functions_init(&math_func);
    printf("Add(1,3) : %d\n", math_func.add(1,3));
    printf("Sub(3,1) : %d\n", math_func.subtract(3,1));
}

```

### extern
- 다른 파일의 전역변수에 접근할 때 사용하는 키워드
```c
//test.c
int a = 10

int test(){
....
}

//main.c
extern int a;
prinf("%d", a); //10
```

### exit() vs return
- return : 일반 함수를 반환값과 함께 종료시킨다.
- exit : 프로세스 자체를 종료시킨다. 종료 전 모든 파일에 대한 입출력을 저장한다. main 함수에서의 return은 exit과 기능적으로 거의 유사. 
