class CustomStack {
    private int [] stack;
    private int top = -1;
    public CustomStack(int maxSize) {
        stack = new int [maxSize];
    }
    
    public void push(int x) {
        if (top < stack.length-1){
            top+=1;
            stack[top] = x;
        }
    }
    
    public int pop() {
        if (top == -1){
            return -1;
        }
        int temp = top;
        top--;
        return stack[temp];
    }
    
    public void increment(int k, int val) {
        int i = 0;
        int l = stack.length;
        if(l<=k){
            while(i<l){
                stack[i] = stack[i] + val;
                i++;
            }
        }
        else{
            while(i<k){
                stack[i] = stack[i] + val;
                i++;
            }
        }
        
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */