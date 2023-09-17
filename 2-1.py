def rev_str(str):
    if str != '':
        return str[-1] + rev_str(str[0:-1])
    else:
        return str
if __name__ == '__main__':
    str = input()
    print(rev_str('ABCDE'))
    print(rev_str('Come again, Forever young!'))
    print(rev_str('Amore, Roma'))
