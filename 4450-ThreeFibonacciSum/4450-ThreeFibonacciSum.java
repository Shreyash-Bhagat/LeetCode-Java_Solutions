// Last updated: 11/10/2026, 8:57:08 am
class Solution {
    public boolean threeFibonacciSum(int n) {
        int a = 0;
        int b = 1;
        int sum = 0;
        // ArrayList<Integer> arr = new ArrayList<>();
        while(n > sum){
            sum = a+b;
            int total = a+b+sum;
            if(total == n){
                return true;
            }
            else if(total > n){
                return false;
            }
            // arr.add(total);
            a = b;
            b =sum;
        }
        return false;
    }
}