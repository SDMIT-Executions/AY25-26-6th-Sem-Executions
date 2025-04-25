package Day4;
import java.util.Arrays;
import java.util.Scanner;

public class TwentyNine {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int n = scanner.nextInt();
		int arr[]=new int[n];
		int arr2[]=new int[n],temp;
		for(int i =0;i<n;i++)
		{
			arr[i]=scanner.nextInt();
			arr2[i]=arr[i];
		}	
		for(int i=0;i<n-1;i++)
		{
			for(int j=i+1;j<=n-1;j++)
			{
				if(arr2[i]<arr2[j])
				{
					temp=arr2[i];
					arr2[i]=arr2[j];
					arr2[j]=temp;
				}
			}
		}
		for(int i =0;i<n;i++)
		{
			for(int j =0;j<n;j++)
			{
				if(arr[i]==arr2[j])
				{
					arr[i]=j+1;
				}
			}
		}
        System.out.println(Arrays.toString(arr));
       // System.out.println(Arrays.toString(arr2));
        
	}

}

//9 8 4 5  > 9 8 5 4
//1 2 4 3




