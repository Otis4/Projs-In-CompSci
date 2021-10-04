import java.util.Scanner;

// class to ask for all user inputs
public class MadlibQuestion{
	//method to ask for which madlib is wanted
	public static int madlibAsker(String qstTxt){
		Scanner userNum = new Scanner(System.in);
		int userAns = 0;
		//loop to make sure there are no invalid answers
		while( !(user_Ans == 1 || user_Ans ==2)){
			System.out.print(qstTxt);
			userAns = userNum.nextInt();
		}
		return userAns;
	}
	//method to take use inputs and put them into the list
	public String wordFill(){// needs list item to be able to do anything
		Scanner wordEnter= new Scanner(System.in);
		//String 
	
	   String placeHolder = "yes";
	   return placeHolder;
	}
}