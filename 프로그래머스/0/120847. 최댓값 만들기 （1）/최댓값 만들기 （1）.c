#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = 1;
    for (int i=1 ; i<3 ; i++){
        for(int j=0 ; j<numbers_len-1; j++){
            if(numbers[j]>numbers[j+1]){
                int temp = numbers[j+1];
                numbers[j+1]=numbers[j];
                numbers[j]=temp;
            }
        }
        answer *= numbers[numbers_len-i];
    }
    return answer;
}