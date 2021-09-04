import java.util.*;
public class EPPER6 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String s1 = scanner.next();
		String s2 = scanner.next();
		s1 = s1.toLowerCase();  //모두 소문자로 바꾸기
		s2 = s2.toLowerCase();
		char[] c1 = s1.toCharArray();  //배열로 바꿔서
		char[] c2 = s2.toCharArray();
		Arrays.sort(c1);  //오름차순 정렬
		Arrays.sort(c2);
		s1 = Arrays.toString(c1); s2 = Arrays.toString(c2);  //다시 String 객체로 바꿔서
		if(s1.equals(s2)) System.out.println("Yes");  //비교해서 같으면 Yes
		else System.out.println("No");
	}
}