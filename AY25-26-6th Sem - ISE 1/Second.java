package Day2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Second {

	public static void main(String[] args)throws IOException{
		InputStreamReader ins =new InputStreamReader(System.in);
		BufferedReader br=new BufferedReader(ins);
		String name = br.readLine();
		System.out.println(name);
		int id=Integer.parseInt(br.readLine());
		System.out.println(id);
char gender = (char)br.read();
		System.out.println(gender);
		
		
		
	}

}
