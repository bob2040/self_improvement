package cn.itcast.demo.demo061220;
/*
Practice:
This is a practice related to computer USB ports,define a USB interface,it has a basic on/off function,
the mouse and keyboard should be connected to the computer via the USB port,and open and close operations.

This practice will focus on the basic use of interfaces,
up and down transformations of objects,
and using interfaces as parameters for methods.
 */
public class DemoMain {
    public static void main(String[] args) {
        //create a computer object
        Computer computer=new Computer();
        computer.powerOn();

        USB usbMouse=new Mouse();//this is a polymorphism statement
        //call useDevice method
        computer.useDevice(usbMouse);

        //create a USB keyboard object
        Keyboard keyboard=new Keyboard();
        computer.useDevice(keyboard);

        computer.powerOff();
    }

}
