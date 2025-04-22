package Day2;

import java.util.Scanner;

public class Eigth {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int num = scanner.nextInt();
		if(num%3==0 && num%5==0)
			System.out.println("Zoom");
		else if(num%5==0)
			System.out.println("Zap");
	 	else if(num%3==0)
			System.out.println("Zip");

	}

}
