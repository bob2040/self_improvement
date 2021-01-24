package cn.itcast.demo.demo061220;
//create a Computer class
public class Computer {
    public void powerOn(){
        System.out.println("Turn on computer");
    }
    public void powerOff(){
        System.out.println("Turn off computer");
    }
    //create a use USB device method,the method parameter is USB interface
    public void useDevice(USB usb){
        usb.open();//call usb.open() method to turn on USB device
        if (usb instanceof Mouse){//use instanceof keyword to judge which the usb class belongs to
            Mouse mouse=(Mouse)usb;//if it belongs to Mouse class
            mouse.click();//then call click() method
        }else if (usb instanceof Keyboard){
            Keyboard keyboard=(Keyboard)usb;//if it belongs to Mouse class
            keyboard.type();//then call type() method
        }
        usb.close();//call usb.close() method to turn off USB device
    }
}
