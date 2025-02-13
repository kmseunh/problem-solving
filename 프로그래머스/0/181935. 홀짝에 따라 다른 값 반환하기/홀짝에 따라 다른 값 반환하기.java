class Solution {
    public int solution(int n) {
        return (n % 2 == 0) ? even(n) : odd(n);
    }

    public int even(int num) {
        int result = 0;
        for (int i = 2; i <= num; i += 2) {
            result += i * i;
        }
        return result;
    }

    public int odd(int num) {
        int result = 0;
        for (int i = 1; i <= num; i += 2) {
            result += i;
        }
        return result;
    }
}