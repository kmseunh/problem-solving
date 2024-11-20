class Solution {
    public int solution(String[] babbling) {
        String[] sounds = {"aya", "ye", "woo", "ma"};
        int answer = 0;
        
        for(String b_word : babbling){
            for(String s_word : sounds){
                b_word = b_word.replace(s_word, " ");
            }
            
            b_word = b_word.trim();
            if(b_word.length() == 0){
                answer++;
            }
        }       
        return answer;
    }
}