def get_score():
    try:
        n = int(input('输入成绩(0-100)：'))
    except ValueError:
        return 0

    if 0 <= n <= 100:
        return n
    return 0

print('学生的成绩：',get_score())
