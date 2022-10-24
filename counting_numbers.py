

def counting():
    c_string=""
    c=1
    n_count = 0
    while c < 1000:
        for x in str(c):
            c_string += x
            if (len(c_string)-n_count)%10 == 0:
                c_string += "\n"
                n_count += 1
            if (len(c_string)-n_count) == 1000:
                print(c)
                c=1000
                break
        c += 1
    print(c_string)



if __name__ == "__main__":
    counting()
    print()