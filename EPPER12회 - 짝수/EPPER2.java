import java.util.Scanner;
public class EPPER2 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		int num = n%15;
		if(num == 0) num = 15;  //�������� 0�� ���� 0���� �ƴ϶� 15��
		System.out.print((n+14)/15 +" " + num);
	}
}