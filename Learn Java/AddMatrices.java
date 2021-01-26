public class AddMatrices {
    public static void main(String[] args) {
        int [][] mat1  = new int [2][3];
        mat1[0][0] = 11;
        mat1[0][1] = 12;
        mat1[0][2] = 13;
        mat1[1][0] = 14;
        mat1[1][1] = 15;
        mat1[1][2] = 16;

        
        int [][] mat2 = new int [][] {{1,2,3},{6,5,4}};
        int [][] mat3 = new int [2][3];

        for (int i=0;i<mat1.length;i++){
            for (int j = 0;j<mat1[i].length;j++){
                mat3[i][j] = mat1[i][j] + mat2[i][j];
                System.out.print(mat3[i][j]+" ");
            }
            System.out.println();
        }
        
    }
}
