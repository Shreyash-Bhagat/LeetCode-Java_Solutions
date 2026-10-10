// Last updated: 10/10/2026, 9:15:21 pm
class Solution {
    public int resilientSubarray(int[] nums, int k) {

        int max = 1;
        int[] arr = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            arr[i] = nums[i]%k;
            if(arr[i]<0){
                arr[i]+=k;
            } 
        }
        int currlen = 1;
        for(int i=1;i<arr.length;i++){
            if(arr[i] == arr[i-1]){
                currlen++;
            }
            else{
                int rem = arr[i-1];
                for(int j=currlen; j>=1 ;j--){
                    if(((j-1)*rem)%k == 0){
                        if(j>max){
                            max = j;
                        }
                        break;
                    }
                }
                currlen = 1;
            }
        }
        int finalRem = arr[arr.length-1];
        for(int j=currlen;j>=1;j--){
            if(((j-1)*finalRem)%k == 0){
                if(j>max){
                    max = j;
                }
                break;
            }
        }
        return max;
    }
}