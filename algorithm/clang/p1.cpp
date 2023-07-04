#include <iostream>

using namespace std;

int main()
{

    /*
    #입력
    1. 변수  입력 받고 (n,x)
    2. 배열  입력 받고 (동정할당)
    #정렬, 이진탐색
    3.
    */

    //변수 선언
    int n, x;
    int *arr;

    //입력 단계
    cin >> n >> x;
    arr = new int(n);
    for(int i=0; i<n; i++)
        cin >> arr[i];

    for(int i=0; i<n; i++)
        cout << arr[i];
        
    //x 보다 큰 수를 배열에서 찾아야 하자나

    return 0;
}