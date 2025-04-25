package Day4;

import java.util.Scanner;

public class Twenty {

	public static void main(String[] args) {
		 Scanner scanner=new Scanner(System.in);
		int a;
		int arr[]=new int[3];
		a=10;
		arr[0]=70;
		arr[1]=80;
		arr[2]=90;
		int b=20;
		int arr2[]= {70,80,90};
		int c;
		int arr3[]=new int[3];
		c=scanner.nextInt();
//		arr3[0]=scanner.nextInt();
//		arr3[1]=scanner.nextInt();
//		arr3[2]=scanner.nextInt();
		for(int i =0;i<3;i++)
		{
			arr[i]=scanner.nextInt();
		}
		for(int i =0;i<3;i++)
		{
			System.out.println(arr[i]);
		}

	}

}
