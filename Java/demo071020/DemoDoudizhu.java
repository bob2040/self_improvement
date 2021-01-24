package cn.itcast.demo.demo071020;

import java.util.ArrayList;
import java.util.Collections;

/*
This is a demo to simulate the process of dealing cards in the card game Fight the Landlord.
1.Prepare cards
2.Shuffle cards
3.Deal cards
4.Read cards
 */
public class DemoDoudizhu {
    public static void main(String[] args) {
        //1.Prepare cards
        //create an ArrayList object，generic is String
        ArrayList<String> poker=new ArrayList<>();
        //define 2 arrays，one is used for the cards colors,the other is used for the cards numbers
        String[] colors={"♠","♥","♣","♦"};
        String[] numbers={"2","A","K","Q","J","10","9","8","7","6","5","4","3"};
        //put red Joker and black Joker into collection first
        poker.add("red_Joker");
        poker.add("black_Joker");
        //cyclically and nestedly traverse arrays to assemble 52 cards
        for(String color:colors){//enhanced for loop
            for(String number:numbers){
                poker.add(color+number);//put the assembled cards into the poker collection
            }
        }

        //2.Shuffle cards
        //use shuffle() method of Collections
        Collections.shuffle(poker);

        //3.Deal cards
        //define 4 Collection objects,use them to store 3 players' cards and three leftover wild cards separately
        ArrayList<String> player1=new ArrayList<>();
        ArrayList<String> player2=new ArrayList<>();
        ArrayList<String> player3=new ArrayList<>();
        ArrayList<String> diPai=new ArrayList<>();
        //traverse poker Collection to get each card
        //use index of poker to mod 3(i%3) to deal cards to the 3 players
        for (int i = 0; i <poker.size() ; i++) {
            //get each cards
            String s = poker.get(i);
            //deal cards
            if(i>=51){
                //three leftover wild cards
                diPai.add(s);
            }else if(i%3==0){
                //deal cards to player1
                player1.add(s);
            }else if(i%3==1){
                //deal cards to player2
                player2.add(s);
            }else if(i%3==2){
                //deal cards to player3
                player3.add(s);
            }
        }

        //4.Read cards
        System.out.println("Player1："+player1);
        System.out.println("Player2："+player2);
        System.out.println("Player3："+player3);
        System.out.println("diPai："+diPai);

    }
}
