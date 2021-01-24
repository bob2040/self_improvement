package cn.itcast.demo.demo092920;

import java.io.*;
import java.util.HashMap;

/*
   Practice：
      Sort the contents of the text in a file by serial number(1,2,3,...).
 */
public class DemoTest {
    public static void main(String[] args) throws IOException {
        //create a HashMap collection object,key of HashMap is used to store the serial number of each line of text,value of HashMap is used to store each line of the text
        HashMap<String,String> map = new HashMap<>();
        //create a BufferedReader object,pass FileReader object to constructor of the BufferedReader
        BufferedReader br = new BufferedReader(new FileReader("zoom-meeting\\test.txt"));
        //create a BufferedWriter object,pass FileWriter object to constructor of the BufferedWriter
        BufferedWriter bw = new BufferedWriter(new FileWriter("zoom-meeting\\tested.txt"));
        //use readLine() method of the BufferedReader object to read text line by line
        String line;
        while ((line = br.readLine()) != null){
            //split the read text to get the serial number and the content of each line of the text
            String[] arr = line.split("\\.");
            //put the gotten serial numbers and text content in HashMap collection
            map.put(arr[0],arr[1]);
        }
        //iterate through the HashMap collection to get each key-value pair
        for(String key : map.keySet()){
            String value = map.get(key);
            //splice each key-value pair into a single line of text
            line = key+"."+value;
            //use write() method of the BufferedWriter object to write the spliced text to the file testOut.txt
            bw.write(line);
            bw.newLine();//line feed
        }
        //close stream objects to release system resources
        bw.close();
        br.close();
    }
}
