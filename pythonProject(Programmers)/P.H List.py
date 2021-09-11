def solution(phone_book):
    answer = True
    phone_book = list(map(int, phone_book))
    phone_book.sort()
    phone_book = list(map(str, phone_book))

    temp = phone_book.pop(0)
    print(phone_book, temp)
    for i in phone_book:
        if temp in i:
            answer = False
            print(answer)
            return answer
        if len(phone_book[0]) == len(temp) : temp = phone_book.pop(0)
        if len(i) > len(temp): break

    print(answer)
    return answer

if __name__ == '__main__':
    solution(["119", "97674223", "1195524421"])
    solution(["123","456","789"])
    solution(["12","123","1235","567","88"])