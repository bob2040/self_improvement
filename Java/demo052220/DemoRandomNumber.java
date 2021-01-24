package cn.itcast.demo.demo052220;

import java.util.Random;
import java.util.Scanner;

public class DemoRandomNumber {
    public static void main(String[] args) {
        Random r=new Random();
        int randomNum=r.nextInt(100)+1;
        Scanner sc=new Scanner(System.in);

        while(true){
            System.out.println("Please input a number you guessed:");
            int guessNum=sc.nextInt();
            if (guessNum>randomNum){
                System.out.println("Too big,try again!");
            }else if(guessNum<randomNum){
                System.out.println("Too small,try again!");
            }else {
                System.out.println("Congratulations,bingo!");
                break;
            }
        }
        System.out.println("Game Over!");
    }
}
