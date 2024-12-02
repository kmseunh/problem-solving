import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[] input = sc.nextLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int X = Integer.parseInt(input[1]);

        String[] arr = sc.nextLine().split(" ");
        ArrayList<Integer> newArr = new ArrayList<>();

        for (String word : arr) {
            int num = Integer.parseInt(word);
            if (num < X) {
                newArr.add(num);
            }
        }

        for (int num : newArr) {
            System.out.print(num);
            System.out.print(" ");
        }
        sc.close();
    }
}