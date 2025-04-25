package Day3;

import java.util.Scanner;

public class Eleven {

	public static void main(String[] args) {
		Scanner scanner= new Scanner(System.in);
		int num = scanner.nextInt();
		int digit,count=0;
		while(num!=0)
		{
			count++;
			num=num/10;
		}
		System.out.println(count);
	}

}




//package Day3;
//
//import java.util.Scanner;
//
//public class Eleven {
//
//	public static void main(String[] args) {
//		Scanner scanner= new Scanner(System.in);
//		int num = scanner.nextInt();
//		int digit,sum=0;
//		while(num!=0)
//		{
//			digit= num%10;
//			sum=sum+digit;
//			num=num/10;
//		}
//		System.out.println(sum);
//	}
//
//}
