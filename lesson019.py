"""Lesson 019"""
import math


def flattener(data):
    """flattens the list"""
    lst = []
    for i in data:
        if isinstance(i, list):
            lst.extend(flattener(i))
        elif not isinstance(i, dict):
            lst.append(i)
    return lst


def combo(num):
    """returns all combination of words"""
    if "0" in str(num) or "1" in str(num):
        return []
    phone = {
        2: "ABC",
        3: "DEF",
        4: "GHI",
        5: "JKL",
        6: "MNO",
        7: "PRS",
        8: "TUV",
        9: "WXY",
    }
    words = [phone[int(i)] for i in str(num)]
    result = [""]
    for word in words:
        # result = [i + j for i in result for j in word]
        n = []
        for i in result:
            for j in word:
                n.append(i + j)
        result = n
    return result


def nested_prime(n):
    """Returns Prime numbers upto n"""
    return [
        i
        for i in range(2, n + 1)
        if not any(i for j in range(2, round(math.sqrt(i) + 1)) if i % j == 0)
    ]


def old_school_reverse(n):
    """returns a reversed string"""
    if not isinstance(n, str):
        return n
    return "".join([n[-i] for i in range(1, len(n) + 1)])


def dict_a_noodle(a):
    """returns a dictionary such that key: value becomes the value: key"""
    return {
        (j if isinstance(i, str) else i): (i if isinstance(i, str) else j)
        for i, j in a.items()
    }


def fib_squares(a, b):
    """returns a list of numbers where the fibonacci numbers are squared"""
    fibs = [0, 1, 1]
    while fibs[-1] < b:
        fibs.append(fibs[-1] + fibs[-2])
    return [i**2 if i in fibs else i for i in range(a, b + 1)]


def dict_of_lists(data):
    """takes a deeply nested list of lists and flattens it out"""
    return {i: flattener(data).count(i) for i in flattener(data)}


def list_of_lists(data):
    """Cataloging a list of lists"""
    return list(set(flattener(data)))


def dict_from_lists(list1, list2):
    """Flattening a list of lists"""
    return {i: list2[list1.index(i)] for i in list1}


def set_complement(*args, verbose=False):
    """
    Return a set of the complement of all the lists provided in *args for every combination of lists
    Include the lists considered in each result when verbose=True
    """
    x = [*args]
    lst = []
    for i in enumerate(x):
        for j in enumerate(x):
            if i[1] != j[1]:
                if verbose:
                    lst.append([i[1], j[1]] + [[q for q in i[1] if q not in j[1]]])
                else:
                    lst.append([q for q in i[1] if q not in j[1]])
    return lst


def set_intersection(*args, verbose=True):
    """
    Return a list of lists of
    - the intersection of all sets
    - the intersection of every possible combination of sets from all sets provided

    Include the lists considered in each result when verbose=True
    """
    x = [*args]
    lst = []
    for i in enumerate(x):
        for j in enumerate(x):
            if i[1] != j[1]:
                if verbose:
                    lst.append([i[1], j[1]] + [[q for q in i[1] if q in j[1]]])
                else:
                    lst.append([q for q in i[1] if q in j[1]])
    return lst


def compare(e1, e2):
    """Finds weather the two dicts are similar or not"""
    if isinstance(e1, list) and isinstance(e2, list):
        if sorted(e1) == sorted(e2):
            return True
        return False
    if isinstance(e1, dict) and isinstance(e2, dict):
        if sorted(e1) != sorted(e2):
            return False
        return all(compare(e1[i], e2[i]) for i in e1)
    if e1 == e2:
        return True
    return False


def dict_compare(*args):
    """
    Using recursion, return a list of all combinations of dictionaries that
    are identical to each other for all combinations of dictionaries provided.

    Equivalence requires that all included lists are also identical in content
    but not in sortedness.

    Make no assumption about the order of keys or the depth of the data.

    Your compare function must use recursion.
    """
    x = [*args]
    return [
        [x[i], x[j]]
        for i in range(len(x))
        for j in range(i + 1, len(x))
        if compare(x[i], x[j])
    ]


def my_secret(message):
    """returns a coded message"""
    message = ("".join(message.split()))[:81]
    rows = round(math.sqrt(len(message)))
    columns = round(len(message) / rows)
    lst = [message[i : i + columns] for i in range(0, rows * columns, columns)]
    return " ".join(
        [
            "".join([lst[j][i : i + 1] for j in range(len(lst))])
            for i in range(len(lst[0]))
        ]
    )


def phone_words(ph1, ph2):
    """Create phone words"""
    combo1, combo2 = combo(ph1), combo(ph2)
    return {ph1: combo1, ph2: combo2}
