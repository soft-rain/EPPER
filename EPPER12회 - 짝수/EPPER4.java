import java.util.Scanner;
public class EPPER4 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		for(int i=0; i<n/2+1; i++) {  //윗 삼각형은 n/2+1줄
			for(int j=n/2-i; j>0; j--) System.out.print(" ");
			for(int j=0; j<=2*i; j++) System.out.print("*");
			System.out.println();
		}
		for(int i=n/2-1; i>=0; i--) {  //아래 삼각형은 n/2줄, 위의 for문과 i를 반대로
			for(int j=n/2-i; j>0; j--) System.out.print(" ");
			for(int j=0; j<=2*i; j++) System.out.print("*");
			System.out.println();
		}
	}
}