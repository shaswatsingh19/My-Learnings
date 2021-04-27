class Solution {
    public int calPoints(String[] ops) {
        
        Stack<Integer> stk = new Stack<>();
        for (int i=0;i<ops.length;i++){
            if (ops[i].equals("C")){
                stk.pop();
            }
            else if (ops[i].equals("D")){
                int d = 2* stk.peek();
                stk.push(d);
            }
            else if (ops[i].equals("+")){
                int s = 0;
                int f = stk.peek();
                s+=f;
                stk.pop();
                s += stk.peek();
                stk.push(f);
                stk.push(s);
            }
            else{
                int a = Integer.parseInt(ops[i]);
                stk.push(a);
            }
        }
        
        int sum = 0;
        for(int val : stk) sum+= val;
        return sum;
    }
}