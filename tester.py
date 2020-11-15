from aes import aes_encrypt

res = ""
msg = "Two One Nine Two #aes:Thats my Kung Fu"
temp_msg = msg.split("#")

if temp_msg[-1][:3] == "aes":
    key = temp_msg[1].split(":")[-1]
    msg = aes_encrypt(temp_msg[:-1], key)
    if msg == 0: 
        res = temp_msg[0]
    else:
        res = msg

print(res)