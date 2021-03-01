public class keywordFinal {
    public static void main(String[] args) {
        /*
        We can use final keyword with variable,class 
        If initalized it cann't be chaged
         */

         final int age=14;

         System.out.println(age);

        //  age = 12; it can't run as error show "The final local variable age cannot be assigned. It must be blank and not using a compound assignment"
         System.out.println(age);
         // if we make final method or final class we can't override by inheriting it method 

         String ag="helo";
         boolean a =ag instanceof String; // instanceof used to check whether this is an instance or not as boolan
         System.out.println(a);
    }
}
