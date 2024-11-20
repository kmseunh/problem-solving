class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        
        if(
            isParallel(dots[0], dots[1], dots[2], dots[3]) ||
            isParallel(dots[0], dots[2], dots[1], dots[3]) ||
            isParallel(dots[0], dots[3], dots[1], dots[2]) ||
            isParallel(dots[1], dots[2], dots[0], dots[3])
          ){
            answer = 1;
        }
        return answer;
    }
    
    boolean isParallel(int[] p1, int[] p2, int[] p3, int[] p4){
    double slope1 = (double) (p2[1] - p1[1]) / (p2[0] - p1[0]); 
    double slope2 = (double) (p4[1] - p3[1]) / (p4[0] - p3[0]); 
    
    return slope1 == slope2;
    }
}