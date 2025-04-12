if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
    scores = sorted(set(scores))
    secondLowest = scores[1]
    names = []
    for name, score in records:
            if score == secondLowest:
                names.append(name)
    names = sorted(names)    
    for i in names:
            print(i)
