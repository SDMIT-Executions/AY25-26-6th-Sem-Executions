package Day3;

import java.util.Scanner;

public class Fifteen {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		   int num =scanner.nextInt();
		   int sqnum=num*num;
		   int count=0,num2=num;
		   while(num!=0) {
			   count++;
			   num=num/10;
		   }
		   if( sqnum%(int)Math.pow(10, count)==num2)
		   {
			   System.out.println("Automorphic");
		   }
		   else 
		   {
			   System.out.println("Not automorphic");
		   }

	}

}
