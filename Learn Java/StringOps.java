

public class StringOps {
   public static void main(String[] args) {
       
    String n;
    n = "hekk";
    n = n.concat("w");
    System.out.println(n);

    String a=new String("JAVA");
    String b = new String("JAVA");

    System.out.println(a==b);//it checks for the reference and both are different refernces 
    System.out.println(a.equals(b));// it checks the value 

    /*
    String can be created using String variableName or String obj/variableNAme = new String();
    The main difference is that in first type which is using literals it check into the pool of Strings where 
    JVM store all other String literal and string pool help to reuse in memeory
    While creating strings using string literals, the value of the string is directly provided. Hence, the compiler first checks the string pool to see if the string already exists.

    If the string already exists, the new string is not created. Instead, the new reference points to the existing string.
    If the string doesn't exist, the new string is created.
    However, while creating strings using the new keyword, the value of the string is not directly provided. Hence the new string is created all the time.

     */
   } 
}
