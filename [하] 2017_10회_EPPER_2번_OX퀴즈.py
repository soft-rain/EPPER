def solution(user_input):
    total_score = 0
    count = 0

    for i in list(user_input):
        if i == "O":
            count += 1
        else:
            count = 0
        total_score += count
    return total_score


if __name__ == "__main__":
    user_input = input()
    if len(user_input) > 1000:
        print("입력 범위를 초과하였습니다. \n")
        exit(1)
    print(solution(user_input))