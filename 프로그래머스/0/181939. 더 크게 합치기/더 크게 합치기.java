class Solution {
    public int solution(int a, int b) {
        String ab = a + "" + b;
        String ba = b + "" + a;
        
        return Math.max(Integer.parseInt(ab), Integer.parseInt(ba));
    }
}