// Last updated: 13/10/2026, 8:48:04 am
class Solution {
    public long maxAlternatingSum(int[] nums) {
        int[] arr = nums;
        Arrays.sort(arr);
        long ans = 0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]<0){
               arr[i] =  Math.abs(arr[i]);
            }
        }
        Arrays.sort(arr);
        int start = 0;
        int end = arr.length-1;
        while(start<=end){
            if(start == end){
                ans+=arr[end]*arr[end];
                return ans;
            }
            ans += arr[end]*arr[end];
            ans -= arr[start]*arr[start];
            end--;
            start++;

        }
        return ans;

        
    }
}