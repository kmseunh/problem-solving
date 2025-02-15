import java.util.*;

class Solution {
    public int solution(int[] num_list) {
        int dupList = 1;
        for (int num : num_list){
            dupList *= num;
        }
        
        int sumList = Arrays.stream(num_list).sum();
        
        return (dupList < sumList * sumList) ? 1 : 0;
    }
}