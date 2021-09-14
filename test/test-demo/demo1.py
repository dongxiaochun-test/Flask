list_a_b = list((chr(a) for a in range(97,123)))
print(list_a_b)

msg = "hello WORFD"
msg = msg.lower()
print(msg)
msg_index = []

for i in msg:
    if i in list_a_b:
        index_value = list_a_b.index(i)
        msg_index.append(index_value+1)
print(msg_index)