package Day2;

import java.util.Scanner;

public class Sixth {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int amt = scanner.nextInt();
		int no2000=0,no500=0,no200=0,no100=0,no50=0,no2=0,no20=0,no10=0,no1=0,no5=0;
		if(amt>=2000)
		{
			no2000=amt/2000;
			amt = amt-(no2000*2000);
		}
		if(amt>=500)
		{
			no500=amt/500;
			amt=amt-(no500*500);
		}
		if(amt>=200)
		{
			no200=amt/200;
			amt=amt-(no200*200);
		}
		if(amt>=100)
		{
			no100=amt/100;
			amt=amt-(no100*100);
		}
		if(amt>=50)
		{
			no50=amt/50;
			amt=amt-(no50*50);
		}
		if(amt>=20)
		{
			no20=amt/20;
			amt=amt-(no20*20);
		}
		if(amt>=10)
		{
			no10=amt/10;
			amt=amt-(no10*10);
		}
		if(amt>=5)
		{
			no5=amt/5;
			amt=amt-(no5*5);
		}
		if(amt>=2)
		{
			no2=amt/2;
			amt=amt-(no2*2);
		}
		if(amt>=1)
		{
			no1=amt/1;
			amt=amt-(no1*1);
		}
		System.out.println("2000*"+no2000+"="+(no2000*2000));
		System.out.println("500*"+no500+"="+(no500*500));
		System.out.println("200*"+no200+"="+(no200*200));
		System.out.println("100*"+no100+"="+(no100*100));
		System.out.println("50*"+no50+"="+(no50*50));
		System.out.println("20*"+no20+"="+(no20*20));
		System.out.println("10*"+no10+"="+(no10*10));
		System.out.println("5*"+no5+"="+(no5*5));
		System.out.println("2*"+no2+"="+(no2*2));
		System.out.println("1*"+no1+"="+(no1*1));
	    int totalnotes=no2000+no500+no200+no100+no50+no10+no20+no5+no2+no1;
	System.out.println("total notes:"+totalnotes);
	}

}
