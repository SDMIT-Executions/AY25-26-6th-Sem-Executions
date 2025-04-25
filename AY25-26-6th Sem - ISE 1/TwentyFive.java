package Day4;
import java.util.Arrays;
import java.util.Scanner;

public class TwentyFive {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int n = scanner.nextInt();
		int arr[]=new int[n],temp;
		for(int i =0;i<n;i++)
		{
			arr[i]=scanner.nextInt();
		}
		for(int i =0;i<n-1;i++)
		{
			for(int j = i+1;j<=n-1;j++)
			{
				if(arr[i]>arr[j])
				{
				  temp=arr[i];
				  arr[i]=arr[j];
				  arr[j]=temp;
				}
			}
		}
		System.out.println(Arrays.toString(arr));

	}

}
