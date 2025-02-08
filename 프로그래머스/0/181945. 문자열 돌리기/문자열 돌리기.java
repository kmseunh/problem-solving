import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        
        for(char word : str.toCharArray()){
            System.out.println(word);
        }
        
        sc.close();
    }
}