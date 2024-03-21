def decode(message_file):
    pyramid = []
    with open(message_file) as f:
        data = f.read().splitlines()

    for l in data:
        if l.strip():
            num, msg = l.split()
            pyramid.append([num, msg])

    pyramid.sort(key=lambda x: x[0])
    res = ""
    for item in pyramid:
        for x in range(100):
            if int(item[0]) == (x * x + x) /2:
                res += item[1] + " "
    return res 


decoded_message = decode('l.in')
print(decoded_message)

