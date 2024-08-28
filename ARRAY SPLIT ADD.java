// Write a program to split an array and add the first half after the second half of the array.
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n;
        n=scanner.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=scanner.nextInt();
        }
       for(int i=0;i<n/2;i++){
           for(int j=0;j<n-1;j++){
               a[j]+=a[j+1];
           a[j+1]=a[j]-a[j+1];
           a[j]=a[j]-a[j+1];
           }
       }
        for(int i=0;i<n;i++){
            System.out.print(a[i]+" ");
        }
       
        }
    }



