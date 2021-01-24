package cn.itcast.demo.demo110920;

public class Calculator {

    //addition
    @Check
    public void add(){
        String str = null;
        str.toString();
        System.out.println("1 + 0 =" + (1 + 0));
    }

    //subtraction
    @Check
    public void sub(){
        System.out.println("1 - 0 =" + (1 - 0));
    }

    //multiplication
    @Check
    public void mul(){
        System.out.println("1 * 0 =" + (1 * 0));
    }

    //division
    @Check
    public void div(){
        System.out.println("1 / 0 =" + (1 / 0));
    }

    public void show(){
        System.out.println("No bug...");
    }
}
