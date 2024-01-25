numbers = [int(x) for x in input().split()]


def negative_sum(*args):
    neg_sum = 0
    for arg in args[0]:
        if arg < 0:
            neg_sum += arg
    return neg_sum


def positive_sum(*args):
    pos_sum = 0
    for arg in args[0]:
        if arg > 0:
            pos_sum += arg
    return pos_sum


def compare(a, b):
    if abs(a) > abs(b):
        return "The negatives are stronger than the positives"
    elif abs(a) < abs(b):
        return "The positives are stronger than the negatives"


print(negative_sum(numbers))
print(positive_sum(numbers))
print(compare(negative_sum(numbers), positive_sum(numbers)))
