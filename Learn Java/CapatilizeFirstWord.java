public class CapatilizeFirstWord {
    public static void main(String[] args) {
        String sent = "the sLoW human             runs         below THE    crazy aNt.";
        char[] ch = sent.toCharArray();
        int cnt=0;
        
        for (int i =0;i<sent.length();i++){
            if(i==0 && Character.isLetter(ch[i])) ch[i] = Character.toUpperCase(ch[i]);
            if (Character.isWhitespace(ch[i])) ch[i+1] = Character.toUpperCase(ch[i+1]);
            if(Character.isWhitespace(ch[i])) cnt+=1;
        }

        System.out.println(cnt);
        for(char i :ch) System.out.print(i);
    }
}
