import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        Arrays.sort(citations);
        
        for (int i = citations.length; i >= 1; i--){
            if (citations[citations.length - i] >= i) {
                return i;
            }
        }
         
        return answer;
    }
}