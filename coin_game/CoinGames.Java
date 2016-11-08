public class CoinGame {
	Player[] players = new Player[2];
	Coin theCoin = new Coin();
	CoinGame(String player1Name, String payer2Name){
		players[0] = new Player(player1Name);
		players[0] = new Player(player1Name);
	}
	public void startGame(){
		int randIndex = (Math.random() < 0.5)?0:1;
		String playersPick = players[randindex].getRandCoinOption();
		
		int opponentIndex = (randIndex == 0)?1:0;
		players[opponentsIndex].setCoinOption(playersPick);
		
		String winningFlip = theCOin.getCoinOption();
		
		players[0].didPlayerWin(winningFlip);
		players[1].didPlayerWin(winningFlip);
	}
}