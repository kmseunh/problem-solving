import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        
        StringBuilder result = new StringBuilder();
        
        for (char word: str.toCharArray()){
            if (Character.isUpperCase(word)){
                result.append(Character.toLowerCase(word));
            } else{
                result.append(Character.toUpperCase(word));
            }
        }
        
        System.out.println(result);
        sc.close();
    }
}