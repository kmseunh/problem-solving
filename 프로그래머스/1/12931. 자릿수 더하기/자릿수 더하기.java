import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        for (char num : String.valueOf(n).toCharArray()) {
            answer += Character.getNumericValue(num);
        }

        return answer;
    }
}