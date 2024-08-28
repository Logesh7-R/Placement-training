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
       int b=0;
       for(int i=0;i<n;i++){
           if(n/2==i){
               System.out.print(b+" ");
               b=0;
           }
           b+=a[i];
       }
       System.out.print(b);
        }
    }

