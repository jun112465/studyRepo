package socket.practice.tcp;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

public class TcpServer extends Thread{
    final static int SERVER_PORT = 1225;
    final static String MESSAGE_TO_SERVER = "Hello, Client";

    public static void main(String[] args) {

        ServerSocket serverSocket = null;

        try {
            serverSocket = new ServerSocket(SERVER_PORT);


        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            while (true) {
                System.out.println("socket 연결 대기");
                Socket socket = serverSocket.accept();
                System.out.println("host : "+socket.getInetAddress()+" | 통신 연결 성공");

                /**	Server에서 보낸 값을 받기 위한 통로 */
                BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                /**	Server에서 Client로 보내기 위한 통로 */
                OutputStream os = socket.getOutputStream();

                System.out.println("using BufferedReader");
                /*
                * br.readline()으로 문자열을 읽기 위해선 마지막에 개행문자가 있어야 한다. 안그러면 무한루프에 빠지게 된다.
                *  */
                System.out.println(br.readLine());
                System.out.println("end");


                os.write( MESSAGE_TO_SERVER.getBytes() );
                os.flush();

//                is.close();
                os.close();
                socket.close();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
