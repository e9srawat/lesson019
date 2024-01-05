import math
def flattener(data):
    lst = []
    for i in data:
        if isinstance(i,list):
            lst.extend(flattener(i))
        elif not isinstance(i, dict):
            lst.append(i)
    return (lst)

def combo(num):
    if "0" in str(num) or "1" in str(num):
        return []
    phone = {2:'ABC',
    3:'DEF',
    4:'GHI',
    5:'JKL',
    6:'MNO',
    7:'PRS',
    8:'TUV',
    9:'WXY'}
    words = [phone[int(i)] for i in str(num)]
    result = ['']
    for word in words:
        #result = [i + j for i in result for j in word]
        n = []
        for i in result:
            for j in word:
                n.append(i+j)
        result = n
    return result

def nested_prime(n):
    return [i for i in range(2,n+1) if not any(i for j in range(2, round(math.sqrt(i)+1)) if i%j == 0)]
  
def old_school_reverse(n):
    if not isinstance(n,str):
        return n
    return "".join([n[-i] for i in range(1, len(n)+1)])

def dict_a_noodle(a):
    return {(j if isinstance(i,str) else i):(i if isinstance(i,str) else j) for i,j in a.items()}

def fib_squares(a, b):
    fibs =[0,1,1]
    while fibs[-1]<b:
        fibs.append(fibs[-1]+fibs[-2])
    return [i**2 if i in fibs else i for i in range(a,b+1)]
    
def dict_of_lists(data):
    return {i:flattener(data).count(i) for i in flattener(data)}

def list_of_lists(data):
    return list(set(flattener(data)))

def dict_from_lists(list1, list2):
    return {i:list2[list1.index(i)] for i in list1}

def my_secret(message):
    message = ("".join(message.split()))[:81]
    rows = round(math.sqrt(len(message)))
    columns = round(len(message)/rows)
    lst =[message[i:i+columns] for i in range(0,rows*columns, columns)]
    return  " ".join(["".join([lst[j][i:i+1] for j in range(len(lst))]) for i in range(len(lst[0]))])

def phone_words(ph1, ph2):
    combo1, combo2 = combo(ph1), combo(ph2)
    return {ph1:combo1,ph2:combo2}
print(phone_words(2345678, 234567))


#message ="if man was meant to stay on the ground god would have given us roots"
#print(my_secret(message))
#data = [[[1, 2, 3], [4, [5, 6]], 6, [7, 8, 9], [8, [8, 9, "a"], {5: 6}, ["b"], "ab"]], [5, 2, 1], 1]
#print(dict_of_lists(data))
#print(dict_of_lists([[[1, 2, 3], [4, [5, 6]], 6, [7, 8, 9], [8, [8, 9, "a"], {5: 6}, ["b"], "ab"]], [5, 2, 1], 1]))
#print(fib_squares(1,90))
#print(dict_a_noodle({'one':1, 'two':2, 3:'three'}))

#imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau