class Solution {
    public int solution(int[] num_list) {
        StringBuilder evenNumbers = new StringBuilder();
        StringBuilder oddNumbers = new StringBuilder();

        for (int num : num_list) {
            if (num % 2 == 0) {
                evenNumbers.append(num);
            } else {
                oddNumbers.append(num);
            }
        }

        int evenSum = Integer.parseInt(evenNumbers.toString());
        int oddSum = Integer.parseInt(oddNumbers.toString());

        return evenSum + oddSum;
    }
}