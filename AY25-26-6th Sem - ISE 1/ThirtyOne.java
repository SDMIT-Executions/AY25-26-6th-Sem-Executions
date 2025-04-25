package Day4;

import java.util.Scanner;

public class ThirtyOne {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int n = scanner.nextInt();
		int arr[]=new int[n];
		for(int i =0;i<n;i++)
		{
			arr[i]=scanner.nextInt();
		}
		int max=arr[0],smax=arr[0];
		for(int i =0;i<n;i++)
		{
			if(max<arr[i])
			{
				smax=max;
				max=arr[i];
			}
			else if(max>arr[i]&&smax<arr[i])
			{
				smax=arr[i];
			}
		}
	System.out.println(smax);

	}

}
