package cn.itcast.demo.demo091420;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

/*
practice after class:
use FileOutputStream class to write "Java is very interesting!!!" to a .txt file.
 */
public class DemoOutputStream {
    public static void main(String[] args) throws IOException {

        //1.create a FileOutputStream object,pass the destination of the data you want to write in the constructor method of FileOutputStream class
        FileOutputStream fos=new FileOutputStream("zoom-meeting\\bb.txt");

        //2.invoke write() method of the FileOutputStream object,write the data to the file
        fos.write(74);//J
        fos.write(97);//a
        fos.write(118);//v
        fos.write(97);//a
        fos.write(32);//
        fos.write(105);//i
        fos.write(115);//s
        fos.write(32);//
        fos.write(118);//v
        fos.write(101);//e
        fos.write(114);//r
        fos.write(121);//y
        fos.write(32);//
        fos.write(105);//i
        fos.write(110);//n
        fos.write(116);//t
        fos.write(101);//e
        fos.write(114);//r
        fos.write(101);//e
        fos.write(115);//s
        fos.write(116);//t
        fos.write(105);//i
        fos.write(110);//n
        fos.write(103);//g
        fos.write(33);//!
        fos.write(33);//!
        fos.write(33);//!

        //3.invoke close() method to release system resources
        fos.close();

        //File f=new File("zoom-meeting\\bb.txt");
        //f.delete();
    }
}
