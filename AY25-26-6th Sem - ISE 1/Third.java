package Day2;

import java.util.Scanner;

public class Third {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num =scanner.nextInt();
		if(num>0)
		{
		System.out.println("Positive");
		}
		else if (num==0) {
			System.out.println("Neutral");
		}
		else {
			System.out.println("Negative");
		}
	}

}
