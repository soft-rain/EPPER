import java.util.*;
public class EPPER6 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String s1 = scanner.next();
		String s2 = scanner.next();
		s1 = s1.toLowerCase();  //��� �ҹ��ڷ� �ٲٱ�
		s2 = s2.toLowerCase();
		char[] c1 = s1.toCharArray();  //�迭�� �ٲ㼭
		char[] c2 = s2.toCharArray();
		Arrays.sort(c1);  //�������� ����
		Arrays.sort(c2);
		s1 = Arrays.toString(c1); s2 = Arrays.toString(c2);  //�ٽ� String ��ü�� �ٲ㼭
		if(s1.equals(s2)) System.out.println("Yes");  //���ؼ� ������ Yes
		else System.out.println("No");
	}
}