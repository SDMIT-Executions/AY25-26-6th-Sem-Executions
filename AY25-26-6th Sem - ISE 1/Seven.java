package Day2;

import java.util.Scanner;

public class Seven {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int avil5=scanner.nextInt();
		int avil1=scanner.nextInt();
		int amt=scanner.nextInt();
		int no5=0,no1=0;
		if(amt>=5)
		{
			no5=amt/5;
			if(no5>avil5)
				no5=avil5;
			amt=amt-(no5*5);
		}
		if(amt>=1)
		{
			no1=amt/1;
			if(no1>avil1)
				no1=avil1;
			amt=amt-(no1*1);
		}
		if(amt==0)
		{
			System.out.println(no5);
			System.out.println(no1);
		}
		else {
			System.out.println("-1");
		}

	}

}
