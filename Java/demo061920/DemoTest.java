package cn.itcast.demo.demo061920;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

/*
Practice:
Please use a date-time related API to calculate how many days a person has been born.
 */
public class DemoTest {
    public static void main(String[] args) throws ParseException {
        //use next() method of Scanner class to get birthday
        Scanner sc=new Scanner(System.in);
        System.out.println("Please input the birthday(Format is：yyyy-MM-dd):");
        String birthdayDateString = sc.next();

        SimpleDateFormat sdf=new SimpleDateFormat("yyyy-MM-dd");
        //use parse() method of DateFormat class to parse a date of birth in string format to a date of birth in Date format
        Date birthdayDate = sdf.parse(birthdayDateString);
        long birthdayDateTime = birthdayDate.getTime();//Convert date in Date format to milliseconds .
        //get current date,and convert it to milliseconds.
//        Date date=new Date();//way one
//        long todayTime=date.getTime();//way one
//        long todayTime=System.currentTimeMillis();//way two
        long todayTime=new Date().getTime();//way three
        //use the millisecond value of the current date minus the millisecond value of the date of birth.
        long diff=todayTime-birthdayDateTime;
        //convert the milliseconds value to days（ms/1000/60/60/24）
        long totalDays=diff/1000/60/60/24;
        System.out.println("The person has been born for："+totalDays+" days!");
    }
}
