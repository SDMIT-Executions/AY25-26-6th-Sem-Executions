package Day4;

import java.util.Scanner;

public class TwentyEight {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int n = scanner.nextInt();
		int arr[]=new int[n],oddsum=0,evensum=0;
		for(int i =0;i<n;i++)
		{
			arr[i]=scanner.nextInt();
		}	

		for(int i =0;i<n;i++)
		{
			if(i%2==0)
				evensum=evensum+arr[i];
			else {
				oddsum=oddsum+arr[i];
			}
			
		}
		System.out.println(oddsum);
		System.out.println(evensum);
	}

}
