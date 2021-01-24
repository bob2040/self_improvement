package cn.itcast.demo.demo061220;
//create a USB interface to establish a connection between the computer and the keyboard and mouse
public interface USB {
    public abstract void open();//turn on device
    public abstract void close();//turn off device
}
