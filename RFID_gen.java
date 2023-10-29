import java.util.Random;
import java.util.Scanner;

public class test1 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the number of cargos:"+" ");
        int entry=sc.nextInt();
        for(int i=1;i<=entry;i++){
            Random rd=new Random();
            System.out.println(i+" : "+ Math.abs(rd.nextInt()));
        }

    }
}
