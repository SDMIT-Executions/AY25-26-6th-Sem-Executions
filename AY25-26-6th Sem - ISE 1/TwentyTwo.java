package Day4;

import java.util.Arrays;
import java.util.Scanner;

public class TwentyTwo {

	public static void main(String[] args) {
		//int marks[]={70,80,90};
		Scanner scanner=new Scanner(System.in);
		int nsub=scanner.nextInt();
		int marks[]=new int[nsub];
		for(int sub=0;sub<nsub;sub++)
		{
			marks[sub]=scanner.nextInt();
		}
		System.out.println(Arrays.toString(marks));
		
		

	}

}
