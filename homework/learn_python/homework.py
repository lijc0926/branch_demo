for i in range(1, 201):
    if i == 1 or i == 2:
        continue
    else:
        code = 1
        for j in range(2, int(i/2)+1):
            if i%j == 0:
                code += 1
        if code == 1:
            print(f'{i}这个数是质数')
