def solution(phone_book):
    answer = True
    phone_book.sort()
    print(phone_book)
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            answer = False
            print(answer)
            return answer
    print(answer)
    return answer

if __name__ == "__main__":
    solution(["119", "97674223", "1195524421"])
    solution(["123","456","789"])
    solution(["124","123","1235","567","88"])