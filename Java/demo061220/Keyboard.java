package cn.itcast.demo.demo061220;
//creat a Keyboard class to implements USB interface
public class Keyboard implements USB {
    @Override
    public void open() {
        System.out.println("Turn on keyboard");
    }

    @Override
    public void close() {
        System.out.println("Turn off keyboard");
    }
    public void type(){
        System.out.println("Keyboard input");
    }
}
