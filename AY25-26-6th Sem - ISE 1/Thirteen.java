package Day3;

import java.util.Scanner;

public class Thirteen {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int num=scanner.nextInt();
        int count=0,num2=num,digit,sum=0;
		while(num!=0)
		{
			count++;
			num=num/10;
		}
		num=num2;
		while(num!=0)
		{
			digit=num%10;
			sum=sum+(int)Math.pow(digit, count);
			num=num/10;
		}
		if(sum==num2)
			System.out.println("amstrong");
		else {
			System.out.println("Not Amstrong");
		}
     
	}

}
