package Day4;

import java.util.Arrays;
import java.util.Scanner;

public class TwentyThree {

	public static void main(String[] args) {
		//int cls[][]= {{70,80,90},{71,81,91}};
		Scanner scanner=new Scanner(System.in);
		int nstu=scanner.nextInt();
		int nsub=scanner.nextInt();
		int cls[][]=new int[nstu][nsub];
		for(int stu=0;stu<nstu;stu++)
		{
			System.out.println("Student:"+stu);
			for(int sub=0;sub<nsub;sub++)
			{
				cls[stu][sub]=scanner.nextInt();
			}
		}
		for(int stu=0;stu<nstu;stu++)
		{
			System.out.println("Student:"+stu);
			for(int sub=0;sub<nsub;sub++)
			{
				System.out.println(cls[stu][sub]);
				
			}
		}
   //System.out.println(Arrays.toString(cls));
	}

}
