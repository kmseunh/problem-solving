import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[] input = sc.nextLine().split(" ");

        int sum = 0;

        for (String num : input) {
            int n = Integer.parseInt(num);
            sum += n * n;
        }

        System.out.println(sum % 10);

        sc.close();
    }
}