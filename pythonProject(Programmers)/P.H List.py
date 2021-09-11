def solution(phone_book):
    answer = True
    phone_book = list(map(int,phone_book))
    phone_book.sort()
    phone_book = list(map(str,phone_book))
    print(phone_book)

    cnt = 0
    phone_book_len = len(phone_book)
    while cnt < phone_book_len-1:
        temp = phone_book.pop(0)

        for PH in phone_book:
            if PH.startswith(temp):
                answer = False
                print(answer)
                return answer

        phone_book.append(temp)
        cnt +=1

    print(answer)
    return answer

if __name__ == '__main__':
    solution(["97674223", "1195524421", "1195524421234"])
    solution(["1","2","1"])
