// Last updated: 23/11/2026, 10:20:19 am
class ProductOfNumbers {

    public List<Integer> nums;
    public ProductOfNumbers() {
        nums = new ArrayList<>();
        nums.add(1);
    }
    
    public void add(int num) { //nums.add(num);
        if(num == 0){
            nums = new ArrayList<>();
            nums.add(1);

        }
        else{
            int last = nums.get(nums.size()-1);
            nums.add(last*num);
        }
    }
    
    public int getProduct(int k) {
        int n = nums.size();
        if(k >= n){
            return 0;
        }
        int total = nums.get(n-1);
        int before = nums.get(n-1-k);
        return total/before;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */