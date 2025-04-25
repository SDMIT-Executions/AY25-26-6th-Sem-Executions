package Day3;

import java.util.Scanner;


public class Fourteen {

	public static void main(String[] args) {
	   Scanner scanner=new Scanner(System.in);
	   int num =scanner.nextInt(),sum=0;
       for(int i =1;i<=num/2;i++)
       {
    	   if(num%i==0)
    		   sum=sum+i;
       }
       if(sum==num)
       {
    	   System.out.println("Perfect");
       }
       else {
    	   System.out.println("Not Perfect");
       }
	}

}
