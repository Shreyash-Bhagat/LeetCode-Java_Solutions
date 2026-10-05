// Last updated: 5/10/2026, 3:44:05 pm
class Solution {
    public int scoreOfParentheses(String s) {
        StringBuilder str = new StringBuilder("");
        if(s.length() < 2) return 0;
        int len = -1;
        int ans = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) == '('){
                str.append(s.charAt(i));
                len++;
            }
            else{
                if (s.charAt(i - 1) == '(') {
                    ans += (1 << len); 
                }
                str.deleteCharAt(len);
                len--;
                
            }
            
        }
        return ans;
    }
}