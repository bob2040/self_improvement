package cn.itcast.demo.demo052920;

import java.util.Scanner;

/*
练习题：
键盘输入一个字符串，并且统计字符串中各个不同种类字符出现的次数。
字符串里面字符的种类有：大写字母，小写字母，数字，其他符号。
 */
public class DemoStringCount {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("请输入你想要的字符串：");
        String str=sc.next();

        int countUpper=0;
        int countLower=0;
        int countNumber=0;
        int countOther=0;

        char[] ch=str.toCharArray();
        for (int i = 0; i < ch.length; i++) {
            if ('A'<=ch[i]&&ch[i]<='Z') {
                countUpper++;
            }else if('a'<=ch[i]&&ch[i]<='z'){
                countLower++;
            }else if('0'<=ch[i]&&ch[i]<='9'){
                countNumber++;
            }else{
                countOther++;
            }
        }

        System.out.println("大写字母数量："+countUpper);
        System.out.println("小写字母数量："+countLower);
        System.out.println("数字数量："+countNumber);
        System.out.println("其他字符数量："+countOther);
    }
}
