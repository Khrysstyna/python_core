#Is this my tail?

def correct_tail(body, tail):
    tail=str(tail)
    sub = body[len(body)-1]
    sub=str(sub)
    if sub == tail:
        return True
    else:
        return False