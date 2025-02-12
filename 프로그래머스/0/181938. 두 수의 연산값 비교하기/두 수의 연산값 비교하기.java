class Solution {
    public int solution(int a, int b) {
        String ab = a + "" + b;
        int ab2 = a * b * 2;
        return Math.max(Integer.parseInt(ab), ab2);
    }
}