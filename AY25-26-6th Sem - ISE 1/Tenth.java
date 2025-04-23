package Day2;

import java.util.Scanner;

public class Tenth {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		char alpha=scanner.next().charAt(0);
//		if(alpha=='a'||alpha=='e'||alpha=='i'||alpha=='o'||alpha=='u')
//         System.out.println("Vowel");
//		else {
//			System.out.println("Consonant");
//		}
		switch(alpha)
		{
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':
			System.out.println("Vowel");
		break;
		default:
			System.out.println("Consonant");
		}
	}

}
