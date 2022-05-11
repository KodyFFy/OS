
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int cyclel = 100000000;
        long timer_s = 0, timer_e = 0;
        double timer_all = 0;

        int suma = 0;
        System.out.print("Введите число b: ");
        int b = in.nextInt();
        System.out.print("Введите число c: ");
        int c = in.nextInt();

        timer_s = System.currentTimeMillis();
        for (int i = 0; i < cyclel; i++) {
            suma += b * 2 + c - i;
        }
        timer_e = System.currentTimeMillis();
        timer_all = (timer_e - timer_s);
        System.out.println("Затраченное время: " + timer_all + " миллисекунд");

    }
}