with open('input.txt', 'r') as in_file, open('output.txt', 'w') as out_file:
    for line in in_file:
        out_file.write(line.upper())
        print('대문자 변환이 완료되었습니다.')
        print('output.txt')