package Day3;
import java.util.Scanner;
public class Eighteen {
	
	public static int sumDigit(int num)
	{
	int sum=0,digit;
	while(num!=0)
	{
		digit=num%10;
		sum=sum+digit;
		num=num/10;
	}
		
		return sum;
	}
	
	public static int countDigit(int num)
	{
		int count=0;
		while(num!=0)
		{
			count++;
			num=num/10;
		}
		return count;
	}

	public static boolean chkPrime(int num)
	{
		boolean flag=true;
		for(int i=2;i<=num/2;i++)
		{
			if(num%i==0)
			{
				flag=false;
				break;
			}
		}
		return flag;
	}
	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int num=scanner.nextInt();
		int sum=0,count=0;
//		int sum=sumDigit(num);
//		int count=countDigit(sum);
		while(count!=1)
		{
		
			sum=sumDigit(num);
			count=countDigit(sum);
		}
		
			boolean isPrime=chkPrime(sum);
		
		
		if(isPrime)
		{
			System.out.println("Lucky Number");
		}
		else {
			System.out.println("Not Lucky");
		}

	}

}
