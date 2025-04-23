package Day2;

import java.util.Scanner;

public class Fifth {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		double puramt=scanner.nextDouble(),dis;
		if(puramt>=20000)
		{
			dis=1500;
			}
		else if(puramt>=10000)
		{
			dis=1000;
			}
		else if(puramt>5000)
		{
			dis=100;
		
		}
		else if(puramt>=1000)
		{
			dis =50;
			
		}
		else {
			dis=0;
			
		}
		System.out.println(dis);
		System.out.println(puramt-dis);

	}

}
