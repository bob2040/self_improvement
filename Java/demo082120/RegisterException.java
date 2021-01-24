package cn.itcast.demo.demo082120;
//customize an Exception class
public class RegisterException extends Exception {
    //insert a Constructor without parameters
    public RegisterException(){
        super();
    }
    //insert another Constructor with exception message parameter
    public RegisterException(String message){
        super(message);
    }
}
