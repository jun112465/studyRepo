#include <vector>
#include <iostream>
#include <cstring>

using namespace std;

class Polynomial{
    
private:
    // 정리된 배열
    // index : 지수
    // value : 계수
    int ef[401] = {0};
    // 숫자 순서대로 입력받은 배열
    int pn[20] = {0};
public:
    Polynomial() {}

    // 연산자 재정의 
    Polynomial operator*(Polynomial& other){
        Polynomial tmp;

        for(int i=1; i<21; i++){
            for(int j=1; j<21; j++){
                tmp.ef[i*j] += ef[i]*other.ef[j];
            }
        }

        return tmp;
    }

    // 문자열 읽어서 채우기
    void read(){
        string input;
        getline(cin, input);

        // 공백 기준으로 정수 변환하여 pn 만들기
        char *token = strtok(&input[0], " ");
        for(int i=0; token!=nullptr; i++){
            pn[i] = stoi(token);
            token = strtok(nullptr, " ");
        }

        // pn을 기반으로 ef 만들기
        for(int i=0; i<10 && pn[i]; i+=2){
            ef[pn[i+1]] = pn[i];
        }
    }

    // 대충 출력
    void print(){
        for(int i=0; i<20; i++){
            cout << i << ":" << ef[i] << endl;
        }
    }
};

int main(){

    Polynomial A;
    A.read();

    Polynomial B;
    B.read();

    Polynomial C = A*B;
    C.print();

    return 0;
}