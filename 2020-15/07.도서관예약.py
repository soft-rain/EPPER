def solution(s, s_len, e, e_len):
	answer =0
	N=s_len	#N : 학생의 수
	e1=e2=-1	#e1, e2는 각 자리
	
	for i in range(0,N):
		for j in range(0,N-1):
			if (e[j]>e[j+1]) or (e[j]==e[j+1] and s[j]>s[j+1]):
				s[j],s[j+1] = s[j+1],s[j]
				e[j],e[j+1] = e[j+1],e[j]
	for i in range(0,N):	#학생 수만큼 반복
		if e1<=s[i]:	#1번 자리가 비어있으면 학생 할당
			e1=e[i]	#1번 자리에 학생의 종료 시간을 대입
			answer+=1 #학생 1명이 할당되었으니 answer +1함
		elif e2<=s[i]:	#2번 자리가 비어있으면 학생을 할당
			e2=e1	#1번 자리의 값을 2번으로 대입하여 이미 자리에 할당된 학생의 종료 시간을 보존
			e1=e[i]	#1번 자리에 학생의 종료 시간을 대입
			answer+=1	#학생 1명 할당되었으니 answer +1함
	return answer	#학생이 할당된 횟수를 저장한 answer반환

n=int(input())
s=list(map(int,input().split()))
e=list(map(int,input().split()))
s_len=len(s)
e_len=len(e)
print(solution(s,s_len,e,e_len))