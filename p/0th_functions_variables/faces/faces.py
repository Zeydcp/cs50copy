def main():
    ipt = input()
    opt = convert(ipt)
    print(opt)

def convert(change):
    change = change.replace(':)', '🙂')
    change = change.replace(':(', '🙁')
    return change

main()