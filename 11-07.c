#include <stdio.h>
#include <stdlib.h>

int ascending(const void* a, const void* b);
int main(){
    int n;
    int i=0;
    int* score;
    float avg;
    scanf("%d", &n);

    score=(int*)malloc(sizeof(int)*n);
    for(i=0; i<n; i++){
        scanf("%d", &score[i]);
    }
    qsort(score, n, sizeof(int), ascending);
    i=0;
    if (n==1)
    avg=score[i];
    else{
        avg=(score[i]+score[i+1])/2.0;
        i+=2;
        while(i!=n){
            avg=(score[i]+avg)/2.0;
            i++;
        }
    }
    printf("%0.6f", avg);

}
int ascneding(const void* a, const void* b){
    if(*(int*)a>*(int*)b)
    return 1;
    else if (*(int*)a<*(int*)b)
    return -1;
    else
    return 0;
}