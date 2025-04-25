package Day4;

import java.util.Scanner;

public class TwentyFour {

	public static void main(String[] args) {
//		int dep[][][]= {{{70,80,90},{71,81,91}},
//				{{72,82,92},{73,83,93}},{{74,84,94},{75,85,95}}};
		Scanner scanner=new Scanner(System.in);
		int ncls=scanner.nextInt();
		int nstu=scanner.nextInt();
		int nsub=scanner.nextInt();
		int dep[][][]=new int[ncls][nstu][nsub];
		for(int cls=0;cls<ncls;cls++)
		{
			System.out.println("Class:"+cls);
			for(int stu=0;stu<nstu;stu++)
			{
				System.out.println("student"+stu);
				for(int sub=0;sub<nsub;sub++)
				{
					dep[cls][stu][sub]=scanner.nextInt();
				}
			}
		}
		for(int cls=0;cls<ncls;cls++)
		{
			System.out.println("Class:"+cls);
			for(int stu=0;stu<nstu;stu++)
			{
				System.out.println("student"+stu);
				for(int sub=0;sub<nsub;sub++)
				{
					System.out.println(dep[cls][stu][sub]);
					
				}
			}
		}
		
	
	}

}
