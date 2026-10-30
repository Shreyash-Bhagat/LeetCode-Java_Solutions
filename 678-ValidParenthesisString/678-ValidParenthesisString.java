// Last updated: 30/10/2026, 11:04:00 am
class Solution {
    public boolean checkValidString(String s) {
        int open = 0;
        int maxopen = 0;
        for(char c : s.toCharArray()){
            if(c == '('){
                open++;
                maxopen++;
            }
            else if(c == ')'){
                open = Math.max(0,open-1);
                maxopen--;
            }
            else{
                open = Math.max(0,open-1);
                maxopen++;
            }
            if(maxopen<0) return false;
        }
        
        if(open == 0) return true;
        return false;
    }
}