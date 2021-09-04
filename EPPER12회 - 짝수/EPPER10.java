import java.util.*;
public class EPPER10 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int K = scanner.nextInt();
		int[][] adj = new int[N][N]; //�������
		int[] time = new int[N];
		int[] total = new int[N];
		int[] indegree = new int[N]; //������
		for(int i=0; i<N; i++) time[i] = scanner.nextInt();
		for(int i=0; i<K; i++) {
			int X = scanner.nextInt() - 1;
			int Y = scanner.nextInt() - 1;
			adj[X][Y] = 1;
			indegree[Y]++;
		}
		int W = scanner.nextInt() - 1;
		
		LinkedList<Integer> queue = new LinkedList<Integer>();
		for(int i=0; i<N; i++) { //�������� 0�� �ֵ� ť�� �ֱ�
			if(indegree[i] == 0) {
				total[i] = time[i];
				queue.add(i);
			}
		}
		while(!queue.isEmpty()) {
			int q = queue.poll();
			for(int i=0; i<N; i++) {
				if(adj[q][i] == 1) {  //������ ����� �ֵ� total time ���ϱ�
					total[i] = Math.max(total[i], total[q] + time[i]);  //�ִ��� ���� ����
					if(--indegree[i] == 0) queue.add(i);
				}
			}
		}
		System.out.println(total[W]);
	}
}