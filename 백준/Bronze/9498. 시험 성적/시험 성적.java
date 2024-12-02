import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int year = sc.nextInt();

        if (year >= 90) {
            System.out.println("A");
        } else if (year >= 80) {
            System.out.println("B");
        } else if (year >= 70) {
            System.out.println("C");
        } else if (year >= 60) {
            System.out.println("D");
        } else {
            System.out.println("F");
        }

        sc.close();
    }
}