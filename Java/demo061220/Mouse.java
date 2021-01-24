package cn.itcast.demo.demo061220;
//creat a Mouse class to implements USB interface
public class Mouse implements USB {
    @Override
    public void open() {
        System.out.println("Turn on mouse");
    }

    @Override
    public void close() {
        System.out.println("Turn off mouse");
    }

    public void click(){
        System.out.println("Mouse click");
    }
}
