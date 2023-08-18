class Solution {
    public boolean isValid(String s) {
        // My Implementation
        Stack<Character> stack = new Stack<>();
        // stack.push()/.pop/.peek/.empty/.search()
        int i = 0;
        while (i < s.length()) {
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[')
                stack.push(s.charAt(i++));
            else {
                if (stack.empty())
                    return false;

                char x = stack.pop();
                
                if (s.charAt(i) == ')' && x == '(') {
                    i++;
                    continue;
                }
                else if (s.charAt(i) == '}' && x == '{') {
                    i++;
                    continue;
                }
                else if (s.charAt(i) == ']' && x == '[') {
                    i++;
                    continue;
                }
                else
                    return false;
            }
        }
        return stack.empty();

        // ChatGPT
        // Stack<Character> stack = new Stack<>();
        
        // for (char c : s.toCharArray()) {
        //     if (c == '(' || c == '{' || c == '[') {
        //         stack.push(c);
        //     } else if (c == ')' && !stack.isEmpty() && stack.peek() == '(') {
        //         stack.pop();
        //     } else if (c == '}' && !stack.isEmpty() && stack.peek() == '{') {
        //         stack.pop();
        //     } else if (c == ']' && !stack.isEmpty() && stack.peek() == '[') {
        //         stack.pop();
        //     } else {
        //         return false;
        //     }
        // }
        
        // return stack.isEmpty();
    }
}