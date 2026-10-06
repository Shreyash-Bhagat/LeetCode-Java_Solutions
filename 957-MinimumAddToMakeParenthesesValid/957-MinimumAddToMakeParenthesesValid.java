// Last updated: 6/10/2026, 10:00:39 am
class Solution {
    public int minAddToMakeValid(String s) {
        int ans = 0;
        // int close = 0;
        int len = -1;
        StringBuilder str = new StringBuilder("");
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) == '('){
                str.append(s.charAt(i));
                len++;
            }
            else if(str.length() >0  && s.charAt(i) == ')'  ){
                str.deleteCharAt(len);
                len--;
            }
            else{
                ans++;
            }
        }
        return (ans+len+1);
    }
}