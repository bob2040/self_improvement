package cn.itcast.demo.demo082820;
/*
Exercises for Lambda expressions with parameters and return values.
Requirements.
Given a Calculator interface, the abstract method calc() can be used to sum two int numbers.
Invoke the invokeCalc() method to add up 20 and 30 using the standard Lambda format.
 */
public class DemoCalculator {
    public static void main(String[] args) {

        //Invoke the invokeCalc() method to add up 20 and 30 and output the sum value.
        //After learning about Lambda expressions, here are 3 ways to write code to achieve the same goal.

        //The 1st way,use an anonymous inner class.
        int sum1;
        sum1=invokeCalc(20, 30, new Calculator() {
            @Override
            public int calc(int a, int b) {
                return a+b;
            }
        });
        System.out.println("The 1st way,sum="+sum1);
        System.out.println("------------------");

        //The 2nd way,use standard Lambda expressions format.
        int sum2;
        sum2=invokeCalc(20,30,(int a,int b)->{
            return a+b;
        });
        System.out.println("The 2nd way,sum="+sum2);
        System.out.println("------------------");

        //The 3rd way,use simplified Lambda expressions format.
        int sum3;
        sum3=invokeCalc(20,30,(a,b)-> a+b);
        System.out.println("The 3rd way,sum="+sum3);
        System.out.println("------------------");
    }
    /*
    Define a method with two integers of type int and the Calculator interface as arguments,
    which internally calls the method calc() in the Calculator interface to compute and return the sum of the two integers.
     */
    public static int invokeCalc(int a,int b,Calculator c){
        int sum=c.calc(a,b);
        return sum;
    }
}
