import java.util.*;
public class EPPER10 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int K = scanner.nextInt();
		int[][] adj = new int[N][N]; //인접행렬
		int[] time = new int[N];
		int[] total = new int[N];
		int[] indegree = new int[N]; //내차수
		for(int i=0; i<N; i++) time[i] = scanner.nextInt();
		for(int i=0; i<K; i++) {
			int X = scanner.nextInt() - 1;
			int Y = scanner.nextInt() - 1;
			adj[X][Y] = 1;
			indegree[Y]++;
		}
		int W = scanner.nextInt() - 1;
		
		LinkedList<Integer> queue = new LinkedList<Integer>();
		for(int i=0; i<N; i++) { //내차수가 0인 애들 큐에 넣기
			if(indegree[i] == 0) {
				total[i] = time[i];
				queue.add(i);
			}
		}
		while(!queue.isEmpty()) {
			int q = queue.poll();
			for(int i=0; i<N; i++) {
				if(adj[q][i] == 1) {  //다음에 연결된 애들 total time 구하기
					total[i] = Math.max(total[i], total[q] + time[i]);  //최대인 것을 선택
					if(--indegree[i] == 0) queue.add(i);
				}
			}
		}
		System.out.println(total[W]);
	}
}