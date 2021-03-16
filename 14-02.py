def solution(score):
    total = 0
    s = len(score)
    # 리스트 요소 모두 더하기
    for i in range(s):
        total += score[i]

    # 평균 계산
    average = (total) / s
    # 평균보다 넘는 점수 세기
    count = 0
    for i in range(s):
        if score[i] > average:
            count = count + 1
    # 평균 넘는 점수의 퍼센트
    percentage = 100 * (count / N)

    print(format(percentage, ".3f"), "%")


# 정수 입력
N = int(input())

# 점수 저장
score = list(map(int, input().split()))
# 함수 호출
solution(score)