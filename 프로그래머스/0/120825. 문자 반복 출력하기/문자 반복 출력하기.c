#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string, int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int count =0;
    char* answer = (char*)malloc(n*strlen(my_string)+1);
    for(int i = 0 ; i<strlen(my_string) ; i++){
        for(int j=1; j<=n; j++){
            answer[count] = my_string[i];
            count++;
        }
    }
    answer[count]='\0';
    return answer;
}