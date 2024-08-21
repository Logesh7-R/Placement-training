/*
Sum of a row in 2D Array
*/

#include <stdio.h>
int main() {
    int a,b,c=0,r;
    scanf("%d %d",&a,&b);
    int arr[a][b];
    for(int i=0;i<a;i++){
        for(int j=0;j<a;j++){
            scanf("%d",&arr[i][j]);
        }
    }
    scanf("%d",&r);
    for(int i=0;i<a;i++){
        c+=arr[r-1][i];
    }
    printf("%d",c);
    return 0;
}
