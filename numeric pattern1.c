/* Write a code for the following pattern:
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
*/

#include <stdio.h>
int main() {
    int a,b,c;
    scanf("%d",&a);
    for(int i=1;i<=a;i++){
            b=i;
               c=a-1;
               printf("%d ",b);
        for(int j=2;j<=i;j++){
               b+=c;
               printf("%d ",b);
               c--;
        }
        printf("\n");
    }
    return 0;
}
