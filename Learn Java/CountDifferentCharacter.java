public class CountDifferentCharacter {
    
    public static void main(String[] args) {
        String str = "Shaswat 123.";
        char [] ch = str.toCharArray();
        int totalSpace=0;int totalOther=0;int totalLetter=0;int totalNum=0;
        for (int i=0;i<str.length();i++){
            if(Character.isWhitespace(ch[i])) totalSpace+=1;
            else if (Character.isLetter(ch[i])) totalLetter +=1;
            else if (Character.isDigit(ch[i])) totalNum +=1;
            else totalOther+=1;
        }
        System.out.println(totalSpace+" "+totalLetter +" "+totalNum+" "+totalOther);
        int a = 'a';
        System.out.println(a);
    }
}
