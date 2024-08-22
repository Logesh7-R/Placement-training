/* Reverse a string */

#include <stdio.h>
int main() {
   char a[20];
   scanf("%[^\n]s",a);
   int c=0,d=0;
   for(int i=0;a[i]!='\0';i++){
       c++;
   }
   c--;
   for (int i=0;i<((c+1)/2);i++){
       char b=a[i];
       a[i]=a[c-i];
       a[c-i]=b;
   }
   printf("%s",a);
    return 0;
}
