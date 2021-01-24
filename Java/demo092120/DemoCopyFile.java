package cn.itcast.demo.demo092120;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

/*
use io byte stream knowledge to copy 1.jpg from C drive to D drive
 */
public class DemoCopyFile {
    public static void main(String[] args) throws IOException {
        long s = System.currentTimeMillis();

        //1.create a FileInputStream object,set the path you want to read in its Constructor
        FileInputStream fis = new FileInputStream("day15-code\\1.jpg");
        //2.create a FileOutputStream object,set the destination you want to write in its Constructor
        FileOutputStream fos = new FileOutputStream("zoom-meeting\\src\\cn\\itcast\\demo\\demo092120\\1.jpg");

        //the first way,read/write one byte per time
        //3.use read() method of FileInputStream object to read file
        /*int len = 0;
        while((len=fis.read())!=-1){
            //4.use write() method of FileOutputStream object to write from what it read one byte to the destination file
            fos.write(len);
        }*/

        //the second way,create a byte array as a buffer to read/write 1KB per time
        byte[] bytes = new byte[1024];
        int len = 0;//number of valid bytes per read
        //3.use read() method of FileInputStream object to read file
        while((len = fis.read(bytes))!=-1){
            //4.use write() method of FileOutputStream object to write from what it read 1KB to the destination file
            fos.write(bytes,0,len);
        }

        //5.release system resources
        fos.close();
        fis.close();
        long e = System.currentTimeMillis();
        System.out.println("Total time to copy files：" + ( e - s ) + "ms.");//record how long it takes to complete the copy
    }
}
