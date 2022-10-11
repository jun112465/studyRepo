package socket.practice.udp;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;

public class UdpServer {


    public static void main(String[] args) throws IOException {

        DatagramSocket serverSocket = new DatagramSocket(9876);

        byte[] receiveData = new byte[1024];

        while(true){
            DatagramPacket receivePacket = new DatagramPacket(
                    receiveData, receiveData.length);

            serverSocket.receive(receivePacket);

            String sentence = new String(receivePacket.getData());
//            InetAddress IPAddress = receivePacket.getAddress();
//            int port = receivePacket.getPort();

            System.out.println(sentence);

        }
    }
}
