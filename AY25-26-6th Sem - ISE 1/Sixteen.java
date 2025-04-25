package Day3;

import java.util.Scanner;

public class Sixteen {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int num=scanner.nextInt();
		//int flag=0;
		boolean flag=true;
		for(int i =2;i<=num/2;i++)
		{
			if(num%i==0)
			{
				//System.out.println("not a prime");
				flag=false;
				break;
			}
		}
		if(flag)
		System.out.println("Prime number");
		else {
			System.out.println("Not a prime");
		}

	}

}
