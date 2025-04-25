package Day3;

import java.util.Scanner;

public class Twelve {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int num=scanner.nextInt();
		int digit,rev=0,num2=num;
		while(num!=0)
		{
			digit=num%10;
			rev=rev*10+digit;
			num=num/10;
			
		}
		System.out.println(rev);
		if(num2==rev)//using copied num2 because num is 0
			System.out.println("Palindrome");
		else {
			System.out.println("Not a palindrome");
		}

	}

}










//package Day3;
//
//import java.util.Scanner;
//
//public class Twelve {
//
//	public static void main(String[] args) {
//		Scanner scanner=new Scanner(System.in);
//		int num=scanner.nextInt();
//		int digit,rev=0;
//		while(num!=0)
//		{
//			digit=num%10;
//			rev=rev*10+digit;
//			num=num/10;
//			
//		}
//		System.out.println(rev);
//
//	}
//
//}
