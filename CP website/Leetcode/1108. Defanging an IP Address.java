class Solution {
    public String defangIPaddr(String address) {
        
        // char [] ch  = address.toCharArray();
        // String ans="";
        // for (int i =0;i<ch.length;i++){
        //     if(ch[i] == '.'){
        //         ans+= "[.]";
        //     }
        //     else{ans+=ch[i];}
        // }
        // return ans;
        // String ans = address.replace(".","[.]");
        // return ans;
        
        return address.replace(".","[.]");
    }
}