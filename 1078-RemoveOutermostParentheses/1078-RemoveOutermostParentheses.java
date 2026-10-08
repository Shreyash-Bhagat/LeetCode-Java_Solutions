// Last updated: 8/10/2026, 10:27:39 am
class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        int depth = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                if (depth > 0) {
                    sb.append(ch);
                }
                depth++;
            } else if (ch == ')') {
                depth--;
                if (depth > 0) {
                    sb.append(ch);
                }
            }
        }
        return sb.toString();
    }
}