package cn.itcast.demo.demo082120;

import java.util.Scanner;
/*
Custom Exception class practice:
Please simulate the username registration operation, if the user name already exists,
an exception will be thrown and the following message will be displayed: Dear,this user name has already been registered.
*/
public class DemoRegisterException {
    //create a string array to save registered usernames
    static String[] usernames={"Ian","Rono","Alex"};
    public static void main(String[] args){
        //use Scanner to get the ID you want to register from Keyboard
        Scanner sc=new Scanner(System.in);
        System.out.println("Please input an ID you want to register:");
        String username = sc.next();
        checkUsername(username);
    }
    //define a method to check if the ID you wanted has been registered
    public static void checkUsername(String username) {
        //iterate through the array which you save registered usernames to get each username
        for (String name : usernames) {
            //use the obtained username to compare with the username entered by the user
            if(name.equals(username)){
                //true:if the username already exists,throw RegisterException，inform the user "Dear,this username has already been registered."
                try {
                    throw new RegisterException("Dear,this username has already been registered.");
                } catch (RegisterException e) {
                    e.printStackTrace();
                    return;//end method
                }
            }
        }
        //if the loop is complete and no duplicate username has been found,
        //the user is prompted with "Congratulations,registration was successful!"
        System.out.println("Congratulations,registration was successful!");
    }
}
