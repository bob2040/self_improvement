package cn.itcast.demo.demo101220;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;


public class TCPServer {
    public static void main(String[] args) throws IOException {

        ServerSocket server = new ServerSocket(8888);
        while(true){

            Socket socket = server.accept();

            InputStream is = socket.getInputStream();

            byte[] bytes = new byte[1024];
            int len = is.read(bytes);
            System.out.println(new String(bytes,0,len));


            OutputStream os = socket.getOutputStream();

            Scanner sc = new Scanner(System.in);
            System.out.print("Server:");
            String str = sc.nextLine();
            os.write(("Server:"+str).getBytes());

            socket.close();
        }
        //server.close();
    }
}
