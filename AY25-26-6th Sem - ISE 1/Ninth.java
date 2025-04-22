package Day2;

import java.util.Scanner;

public class Ninth {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		int num=scanner.nextInt();
		int num2=scanner.nextInt();
		if(num==num2)
			System.out.println(num+num2);
		else {
			System.out.println(2*(num+num2));
		}

	}

}
