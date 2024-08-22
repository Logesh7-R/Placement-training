/*
Matrix multiplication:

Array 01:

1 2 3
4 5 6
7 8 9

Array 02:

1 2 3
4 5 6
7 8 9

Output:

30 36 42
66 81 96
102 126 150
*/
#include <stdio.h>
int main() {
int r1,c1,r2,c2;
scanf("%d %d %d %d",&r1,&c1,&r2,&c2);
if(c1!=r2){
    printf("enter valid matrix row and column");
}
else{
    int arr1[r1][c1],arr2[r2][c2],arr3[c1][r2];
    for(int i=0;i<r1;i++){
        for(int j=0;j<c1;j++){
            scanf("%d",&arr1[i][j]);
        }
    }
    for(int i=0;i<r2;i++){
        for(int j=0;j<c2;j++){
            scanf("%d",&arr2[i][j]);
        }
    }
     for(int i=0;i<c1;i++){
        for(int j=0;j<r2;j++){
            arr3[i][j]=0;
            for(int k=0;k<c1;k++){
            arr3[i][j]+=arr1[i][k]*arr2[k][j];    
            }
            printf("%d ",arr3[i][j]);
        }
        printf("\n");
    }
}
   return 0;
}

