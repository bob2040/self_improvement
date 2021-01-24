package cn.itcast.demo.demo072420;

import java.util.HashMap;
import java.util.Scanner;
import java.util.Set;

/*
Practice:
    Counts the number of times each character appears in a string.(Please use HashMap)
 */
public class DemoMapTest {
    public static void main(String[] args) {
        //1.use Scanner to get user input string
        Scanner sc=new Scanner(System.in);
        System.out.println("Please input a string:");
        String str = sc.next();
        //2.create a HasMap object,Key is the character in the string,Value is the number of the characters
        HashMap<Character,Integer> map=new HashMap<>();
        //3.iterate through the string to get each character
        for (char key : str.toCharArray()) {
            //4.use the gotten characters to judge if the key exists or not in the the HashMap collection.
            if(map.containsKey(key)){
                //if the key exists
                Integer value = map.get(key);
                value++;
                map.put(key,value);
            }else {
                //if the key doesn't exist
                map.put(key,1);
            }
        }
        //5.iterate through the HashMap collection and print the result
        Set<Character> set = map.keySet();
        for (Character key : set) {
            Integer value = map.get(key);
            System.out.println(key+"="+value);
        }
    }
}
