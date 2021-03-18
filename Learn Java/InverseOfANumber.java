import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class InverseOfANumber {

public static void main(String[] args) throws IOException{
  // write your code here  
  BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

  String str = reader.readLine();

  int arr[] = new int[str.length()];

  int n = Integer.parseInt(str);

//   CountDigit obj = new CountDigit();
//   int cnt = obj.countDigit(n);
//   System.out.println(cnt);

  for (int i = 0; i < arr.length; i++) {
    int index = arr.length - i;

    String ch = Integer.toString(index);

    int ind  = str.indexOf(ch);
    int newIndex = str.length() - ind;


    arr[i] = newIndex;
    
}

for (int i : arr) {
    System.out.print(i);
}
}

}
