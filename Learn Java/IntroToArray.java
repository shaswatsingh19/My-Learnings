public class IntroToArray {
    public static void main(String[] args) {
        int [] marks = new int[3];
        marks[0] = 100;
        marks[1] = 51;
        marks[2] = 86;
        // INdex out of bound error        marks[5] = 41;

        String [] name;
        name = new String[2];
        name[0] = "SHaswat";
        name[1] = "Singh";

        float [] age = new float[]{10.3f,12.2f};
        System.out.println(age[1]);


        // Printing in reverse order


        String [] children = new String[] {"Ram","Shyam","RADHA"        };
        for (int i = children.length-1;i>=0;i--){
            System.out.println(children[i]);
        }

        // FOR each loop 
        for(String identity:children){
            System.out.println(identity);
        }

        // multidimension array

        int [][] multi = new int [2][3];

        /*
        multi = 
           [  1 | 2 | 3
              4 | 5 | 6   ]
        
        */
        multi[0][0] = 1;
        multi[0][1] = 22;
        multi[0][2] = 222;
        multi[1][0] = 11;
        multi[1][1] = 222;
        multi[1][2] = 522;
        System.out.println(multi[0][0]);
        System.out.println(multi[0][1]);
        System.out.println(multi[0][2]);
        System.out.println(multi[1][0]);
        System.out.println(multi[1][1]);
        
        System.out.println(multi[1][2]);


        for (int i =0;i<multi.length;i++){
            for (int j=0;j<multi[i].length;j++){
                System.out.print(multi[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}
