// Last updated: 9/10/2026, 10:57:41 am
class Solution {
    public int minInsertions(String s) {
        int closeneed = 0;
        int insert = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) == '('){
                closeneed+=2;
                if(closeneed%2 != 0){
                    insert++;
                    closeneed--;
                }
            }
            else{
                closeneed--;
                if(closeneed < 0){
                    insert++;
                    closeneed+=2;
                }
            }
        }
        return closeneed+insert;
    }
}