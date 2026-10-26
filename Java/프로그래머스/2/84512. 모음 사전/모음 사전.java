class Solution {
    int answer = 0;
    public int solution(String word) {
        
        dfs("", word);
                
        return answer;
    }
    
   public boolean dfs(String current, String word) {
        String[] vowels = {"A", "E", "I", "O", "U"};

        if (word.equals(current)) {
            return true;
        }

        if (current.length() == 5) {
            return false;
        }

        for (String vowel : vowels) {
            answer++;

            if (word.equals(current + vowel)) {
                return true;
            }

            if (dfs(current + vowel, word)) {
                return true;
            }
        }

        return false;
    }
}