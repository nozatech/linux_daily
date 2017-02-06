import java.util.Scanner;

public class CoinFlippingGame {
	public static void main(String[] args){
		CoinGame theCoinGame =new CoinGame("Mark", "Tom");
		String usersAnser;
		do {
			theCoinGame.startGame();
			System.out.println("Play Again?");
			Scanner playGameAgain =new Scanner(System.in);
			userAnswer = playGameAgain.nextLine();
			
		} while((userAnswer.startsWith("y")) || (userAnswer.startsWith("Y")));
	}
}