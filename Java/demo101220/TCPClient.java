package cn.itcast.demo.demo101220;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.util.Scanner;


public class TCPClient {
    public static void main(String[] args) throws IOException {

        while(true){

            Socket socket = new Socket("127.0.0.1",8888);

            OutputStream os = socket.getOutputStream();

            Scanner sc = new Scanner(System.in);
            System.out.print("Bob:");
            String str = sc.nextLine();
            os.write(("Bob:"+str).getBytes());

            InputStream is = socket.getInputStream();

            byte[] bytes = new byte[1024];
            int len = 0;
            while((len=is.read(bytes))!=-1){
                System.out.println(new String(bytes,0,len));
            }

            socket.close();
        }

    }
}
