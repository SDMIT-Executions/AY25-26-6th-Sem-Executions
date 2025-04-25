package Day4;

import java.util.Scanner;

public class TwentySix {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int n = scanner.nextInt();
		int arr[]=new int[n],min;
		for(int i =0;i<n;i++)
		{
			arr[i]=scanner.nextInt();
		}
		min=arr[0];
		for(int i =0;i<n;i++)
		{
			if(min>arr[i])
				min=arr[i];
		}
		System.out.println(min);

	}

}


//package Day4;
//
//import java.util.Scanner;
//
//public class TwentySix {
//
//	public static void main(String[] args) {
//		Scanner scanner=new Scanner(System.in);
//		int n = scanner.nextInt();
//		int arr[]=new int[n],max;
//		for(int i =0;i<n;i++)
//		{
//			arr[i]=scanner.nextInt();
//		}
//		max=arr[0];
//		for(int i =0;i<n;i++)
//		{
//			if(max<arr[i])
//				max=arr[i];
//		}
//		System.out.println(max);
//
//	}
//
//}
