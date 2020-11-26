def solution(phone_book):
    answer = True
    bookSize = len(phone_book)
    for i in range(bookSize):
        curWord = phone_book[i]
        
        for j in range(bookSize):
            if i == j : continue
            else :
                minLength = min(len(curWord), len(phone_book[j]))
                count = 0
                for k in range(minLength):
                    if curWord[k] == phone_book[j][k] : count += 1
                if count == minLength : return False
    return answer

