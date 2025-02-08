import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);     
        
        StringBuilder sb = new StringBuilder(sc.next()).append(sc.next());
        
        System.out.println(sb);
        sc.close();
    }
}