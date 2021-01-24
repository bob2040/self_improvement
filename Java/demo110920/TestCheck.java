package cn.itcast.demo.demo110920;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Method;

public class TestCheck {
    public static void main(String[] args) throws IOException {

        Calculator c = new Calculator();

        Class cls = c.getClass();
        int number = 0;
        BufferedWriter bw = new BufferedWriter(new FileWriter("zoom-meeting\\src\\cn\\itcast\\demo\\demo110920\\bug.txt"));

        Method[] methods = cls.getMethods();
        for (Method method : methods) {

            if(method.isAnnotationPresent(Check.class)){

                try {
                    method.invoke(c);
                } catch (Exception e) {

                    number ++;
                    bw.write("An exception occurs in the "+method.getName()+" method.");
                    bw.newLine();
                    bw.write("The name of the exception:" + e.getCause().getClass().getSimpleName());
                    bw.newLine();
                    bw.write("The reason for the exception:" + e.getCause().getMessage());
                    bw.newLine();
                    bw.write("-----------------------------------------");
                    bw.newLine();
                }
            }
        }
        bw.write("There were a total of " + number + " exceptions in this test.");
        bw.flush();
        bw.close();
    }
}
