import java.util.*;
public class EPPER8 {
	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		int T = in.nextInt();
		for(int t=0; t<T; t++){
			int time=in.nextInt();
			if(time<=0) break;
			int x=0;
			int y=0;
			int n=(int)Math.ceil(Math.sqrt(time));
			int start=(n-1)*(n-1);
			
			if(n%2==0){//n이 짝수이면 오른쪽 아래로 갈수록 1 추가
				for(int i=1;i<=n;i++){
					x++;
					start++;
					y=n;
					if(start==time) break;
				}
				if(start!=time){
					for(int i=1;i<n;i++){
						start++;
						x=n;
						y--;
						if(start==time) break;
					}
				}
				System.out.println(x+" "+y);
			}
			else{//홀수이면 위로 왼쪽으로 갈수록 1 추가
				for(int i=1;i<=n;i++){
					y++;
					start++;
					x=n;
					if(start==time) break;
				}
				if(start!=time){
					for(int i=1;i<n;i++){
						start++;
						y=n;
						x--;
						if(start==time) break;
					}
				}
				System.out.println(x+" "+y);
			}
		}
	}
}