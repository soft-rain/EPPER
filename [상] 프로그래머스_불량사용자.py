def dfs(b, visited, s, user_id, banned_id):
    if b == len(banned_id):
        string = ""
        for i in range(len(user_id)):
            if i in visited:
                string += str(i)
        # 중복되지 않게 문자열 조합을 젖아
        s.add(string)
        return s
    for i in range(len(user_id)):
        # 이미 제재된 아이디 제외
        if i in visited:
            continue
        # 문자열의 길이가 다르면 해당 제재 아이디와 관계 없으므로 제외
        if len(user_id[i]) != len(banned_id[b]):
            continue
        temp = True
        for j in range(len(user_id[i])):
            if user_id[i][j] == banned_id[b][j] or banned_id[b][j] == "*":
                continue
            # 한 문자라도 다르거나 *가 아닐 때
            else:
                temp = False
                break
            # 제재 사용자에 포함되는 야이디일 때
        if temp == True:
            # 응모자 아이디 사용 표시
            visited.append(i)
            s = dfs(b + 1, visited, s, user_id, banned_id)
            # 응모자 아이디 사용 표시 해제
            visited.remove(i)
    return s


def solution(user_id, banned_id):
    answer = 0
    s = set()  # 문자열 조합을 저장할 집합
    visited = []  # 응모자 아이디 사용 표시할 배열

    s = dfs(0, visited, s, user_id, banned_id)
    answer = len(s)  # 문자열 조합의 개수 저장
    return answer