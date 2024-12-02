import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNextInt()) {

            String[] input = sc.nextLine().split(" ");
            System.out.println(Integer.parseInt(input[0]) + Integer.parseInt(input[1]));

        }
        sc.close();

    }
}