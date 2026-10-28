import java.util.Stack;

class Solution {
    boolean solution(String s) {
        boolean answer = false;
        Stack<String> stack = new Stack<>();
        
        for(int i=0; i<s.length(); i++){
            if (s.charAt(i) == '('){
                stack.push(String.valueOf(s.charAt(i)));
            } else {
                if (!(stack.isEmpty())){
                    if (stack.pop().equals("(")){
                        answer = true;
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
