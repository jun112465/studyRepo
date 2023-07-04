import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class MakeImg{
    public static void main(String[] args) throws IOException {
        String str = "lets make a img file";

        BufferedImage img = new BufferedImage(200, 200, BufferedImage.TYPE_INT_RGB);
        Graphics g = img.getGraphics();

        g.setColor(Color.white); //색상을 흰색으로 지정.
        g.fillRect(0, 0, 400, 400); // 사각형을 그림. 즉 흰색으로 채워진 사각형
        g.setColor(Color.blue); //색상을 블루로 지정
        g.drawString(str, 10, 100); //str에 있는 문자열을 x좌표 10, y좌표 100에 그림
        g.setColor(Color.red);
        g.fillOval(150,150, 100, 100); //원형 그리기
        //void java.awt.Graphics.fillOval(int x, int y, int width, int height)
        OutputStream out = new FileOutputStream("pic.jpg"); //파일로 출력하기위해 파일출력스트림 생성
        ImageIO.write(img, "JPG", out); //이미지 출력! , 이미지를 파일출력스트림을 통해 JPG타입으로 출력
        out.close();  //출력스트림 닫기
    }
}