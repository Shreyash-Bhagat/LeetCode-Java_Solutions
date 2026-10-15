// Last updated: 15/10/2026, 9:26:54 am
class Solution {
    public int sumCounts(List<Integer> nums) {
        //Method-1
        int ans = 0;
        // for(int i=0;i<nums.size();i++){
            
        //     for(int j=i;j<nums.size();j++){
        //         HashSet<Integer> hm = new HashSet<>();
        //         for(int k=i;k<=j;k++){
        //             hm.add(nums.get(k));
        //         }
        //         ans += hm.size()*hm.size();
                
        //     }
        // }
        // return ans;

        for(int i=0;i<nums.size();i++){
            boolean[] br = new boolean[101];
            int d =0;
            for(int j=i;j<nums.size();j++){
                int num = nums.get(j);

                if(!br[num]){
                    br[num] = true;
                    d++;
                }
                ans += d*d;
            }
            
        }
        return ans;
    }
}