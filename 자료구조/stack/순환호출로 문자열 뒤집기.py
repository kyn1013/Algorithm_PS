def reverse(msg, len):
    if(len == 1):
        print(msg[0], end='')
    else :
        print(msg[len-1], end='')
        len -= 1
        return reverse(msg,len)


instr = "자료구조"
reverse(instr, len(instr))
