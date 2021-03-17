
#올바른 괄호 배열
def solution(op, close, total):
	res = 0
	if(close ==total):
		return 1
	if(op==total):
		res+=solution(op, close+1, total)
	else:
		if(op>close):
			res+=solution(op, close+1, total)
			res+=solution(op+1, close, total)
		else:
			res+=solution(op+1, close, total)
	return res

n = int(input())
print(solution(0,0,n))
