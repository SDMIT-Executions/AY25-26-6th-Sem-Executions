package Day4;

import java.util.Scanner;

public class TwentySeven {

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

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int n = scanner.nextInt();
		int arr[]=new int[n],sum=0,count=0;
		for(int i =0;i<n;i++)
		{
			arr[i]=scanner.nextInt();
		}	

		for(int i =0;i<n;i++)
		{
			sum=sum+arr[i];
		}
		System.out.println(sum);
		while(count!=1)
		{
		
			sum=sumDigit(sum);
			System.out.println(sum);
			count=countDigit(sum);
		}
	}

}
//76
//654
//456
//2478
//==>3664
//==>19
//==>10
//==>1
