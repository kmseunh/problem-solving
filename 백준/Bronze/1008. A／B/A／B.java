import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[] input = sc.nextLine().split(" ");

        double A = Double.parseDouble(input[0]);
        double B = Double.parseDouble(input[1]);

        System.out.println(A / B);

        sc.close();
    }
}