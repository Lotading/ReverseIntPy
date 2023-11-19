def reverse(x: int) -> int:
        max_int = 2**31 - 1
        min_int = -2**31

        z = list(str(x))
        if z[0] == "-":
            z.pop(0)
            z.reverse()
            z.insert(0,"-")
        else:
            z.reverse()
        
        num = int(''.join(z))

        if num < min_int or num > max_int:
            return 0
        else:
            return num

def get_input():
    print("REVERSEint.exe")
    user_input = input("Write in num: ")
    try:
        num = int(user_input)
        return num
    except ValueError:
        print("not a num plz do again")
        return get_input()
    
result = reverse(get_input())
print(result)