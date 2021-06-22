def print_spam():

    def more_spam():
        y = "more "
        y += x

        def even_more_span():
            z = "even "
            z += y
            return z

        y += even_more_span()
        return y

    x = "spam "
    x += more_spam()
    return x


print(print_spam())
print(locals())
print(globals())
