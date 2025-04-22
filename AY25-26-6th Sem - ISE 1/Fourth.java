//5
//12340
//23401
//34012
//40123
//01234
//
//r1=c1,c2,c3,c4,c5
//r2=c1,c2,c3,c4,c5
//r3=c1,c2,c3,c4,c5
//r4=c1,c2,c3,c4,c5
//r5=c1,c2,c3,c4,c5
//
//    st stop alter
//row 1   <=5  +1
//col 1   <=5   +1




package Day2;

import java.util.Scanner;

public class Fourth {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int nrow=scanner.nextInt();
		int count=1;
		for(int row=1;row<=nrow;row++)
		{
			count=row;
			for(int col=1;col<=nrow;col++)
			{
				if(count==nrow)
					count=0;
				System.out.print(count);
				count++;
		}
			System.out.println();
		}
		
	}

}


