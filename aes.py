"""
Simplified AES algorithm by Ted Byun 

"""


def initialize(plaintext):
    while len(plaintext) % 16 != 0:
        plaintext += '{'

    index = len(plaintext)//16
    x = 0
    array = []
    for i in range(index):
        string = []
        j = 0
        while j != 16:
            string.append(plaintext[x])
            x += 1
            j += 1 
        string = ''.join(string)
        array.append(string)
    array.append(str(index))
    return array

def matrix(array):
    array = list(array)
    x = 0
    y = 0
    new = []
    for i in range(4):
        string = []
        for j in range(4):
            string.append(array[x])
            x = x + 4
        x = y + 1
        y += 1
        string = ''.join(string)
        new.append(list(string))
    return new

def hex_index(c):
    if (c == '0'):
        x = 0
    elif (c == '1'):
        x = 1
    elif (c == '2'):
        x = 2
    elif (c == '3'):
        x = 3
    elif (c == '4'):
        x = 4
    elif (c == '5'):
        x = 5
    elif (c == '6'):
        x = 6
    elif (c == '7'):
        x = 7
    elif (c == '8'):
        x = 8
    elif (c == '9'):
        x = 9
    elif (c == 'a'):
        x = 10
    elif (c == 'b'):
        x = 11
    elif (c == 'c'):
        x = 12
    elif (c == 'd'):
        x = 13
    elif (c == 'e'):
        x = 14
    elif (c == 'f'):
        x = 15
    return x

def subBytes(block):
    s_box = []
    array = [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]

    x = 0
    for i in range(16):
        temp = []
        for j in range(16):
            temp.append(array[x])
            x += 1
        s_box.append(temp)
    
    sub1 = []
    for i in range(4):
        sub2 = []
        sub2.append(hex(ord(block[i])))
        sub1.append(sub2[0][2:])
    
    for i in range(4):
        if (len(sub1[i]) == 1):
            sub1[i] = '0' + sub1[i]

    for i in range(4):
        c = sub1[i][0]
        d = sub1[i][1]
        x = hex_index(c)
        y = hex_index(d)
        block[i] = chr(s_box[x][y])

def shiftRows(block):
    for i in range(4):
        if (i == 0):
            pass
        elif (i == 1):
            temp = block[i][0]
            block[i].pop(0)
            for x in temp:
                block[i].append(x)
        elif (i == 2):
            temp = block[i][0:2]
            block[i].pop(0)
            block[i].pop(0)
            for x in temp:
                block[i].append(x)
        elif (i == 3):
            temp = block[i][0:3]
            block[i].pop(0)
            block[i].pop(0)
            block[i].pop(0)
            for x in temp:
                block[i].append(x)

def binary_addition(block, column, row):
    if (row == 1):
        return block
    elif (row == 2):
        if (column[0] == '0'):
            new = bit_shift(block,column)
            return new
        else:
            block = bit_shift(block,column)
            result = block ^ 27
            return result  
    elif (row == 3):
        if (column[0] == '0'):
            new = bit_shift(block,column)
            result = new ^ block
            return result
        else:
            new = bit_shift(block,column)
            result = (new ^ 27) ^ block
            return result

def bit_shift(block,column):
    string = ""
    for i in range(8):
        if (i == 7):
            string = string + '0'
        else:
            if (column[i+1] == '0'):
                string = string + '0'
            elif (column[i+1] == '1'):
                string = string + '1'
    
    for x in range(256):
        temp = bin(x)
        temp = temp[2:]
        while (len(temp) != 8):
                temp = '0' + temp
        if (temp == string):
            return x

def mixColumn(block):
    check = [[0 for x in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
            temp = int(block[i][j],16)
            block[i][j] = temp
            temp = bin(temp)
            temp = temp[2:]
            while (len(temp) != 8):
                temp = '0' + temp
            check[i][j] = temp
    
    result = [[0 for x in range(4)] for x in range(4)]
    submatrix = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]

    for x in range(4):
        for i in range(4):
            temp = 0
            for y in range(4):
                show = binary_addition(block[y][x],check[y][x],submatrix[i][y])
                temp = temp ^ show
            result[x][i] = temp
    return result

def get(word):
    s_box = []
    array = [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
    x = 0
    for i in range(16):
        temp = []
        for j in range(16):
            temp.append(array[x])
            x += 1
        s_box.append(temp)
    
    sub1 = []
    for i in range(4):
        sub2 = []
        sub2.append(hex(word[i]))
        sub1.append(sub2[0][2:])
    
    for i in range(4):
        if (len(sub1[i]) == 1):
            sub1[i] = '0' + sub1[i]

    for i in range(4):
        c = sub1[i][0]
        d = sub1[i][1]
        x = hex_index(c)
        y = hex_index(d)
        word[i] = s_box[x][y]

def addroundKey(key, round):
    init = round*4 
    end = round*4 + 4
    last = []
    for i in range(4):
        last.append(key[init-1][i])
    temp = key[init-1][0]
    key[init-1].pop(0)
    key[init-1].append(temp)
    get(key[init-1])
    round_table = [1,2,4,8,16,32,64,128,27,54]
    round_constant = round_table[round-1]
    key[init-1][0] = round_constant ^ key[init-1][0]
    w = []
    for i in range(44):
        w.append([])

    for i in range(0, init):
        for j in range(4):
            w[i].append(1)

    for i in range(init):    
        for j in range(4):
            w[i][j] = key[i][j]

    for i in range(init, init+4):
        for j in range(4):
            w[i].append(1)
    
    for j in range(4):
        w[init][j] = w[init-4][j] ^ w[init-1][j]

    for j in range(4): 
        w[init+1][j] = w[init][j] ^ w[init-3][j]

    for j in range(4): 
        w[init+2][j] = w[init+1][j] ^ w[init-2][j]
    
    for j in range(4): 
        w[init+3][j] = w[init+2][j] ^ last[j]
    return w

def aes_encrypt(msg, key):
    array = initialize(msg)
    length = int(array[-1])
    array.pop(-1)
    blocks = []
    
    for i in range(length):
        sorted_array = []
        sorted_array = matrix(array[i])
        blocks.append(sorted_array)

    if len(key) != 16:
        return 1 
    
    init_key = []
    for i in range(16):
        init_key.append(ord(key[i]))
    w = []
    for j in range(44):
        w.append([])
    
    index = 0
    for x in range(4):
        for y in range(4):
            w[x].append(init_key[index])
            index += 1
    round = 0
    w_round = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            w_round[j][i] = w[(4*round) + i][j]
    for j in range(length):
        for x in range(4):
            for y in range(4):
                blocks[j][x][y] = ord(blocks[j][x][y])
                blocks[j][x][y] = blocks[j][x][y] ^ w_round[x][y]
    for x in range(length):
        for y in range(4):
            for j in range(4):
                blocks[x][y][j] = chr(blocks[x][y][j])

    valid = 10
    while (valid != 0):
        for x in range(length):
            for y in range(4):
                subBytes(blocks[x][y])
        for x in range(length):
            shiftRows(blocks[x])
        
        if (round < 9):
            before_addkey = []
            for x in range(length):
                for y in range(4):
                    for j in range(4):
                        blocks[x][y][j] = hex(ord(blocks[x][y][j]))
                        blocks[x][y][j] = blocks[x][y][j][2:]
                result = mixColumn(blocks[x])
                before_addkey.append(result)
            
            for x in range(length):
                for y in range(4):
                    for j in range(4):
                        blocks[x][j][y] = before_addkey[x][y][j]
        else:
            for x in range(length):
                for y in range(4):
                    for j in range(4):
                        blocks[x][y][j] = ord(blocks[x][y][j])

        round += 1
        
        w = addroundKey(w,round)
        w_round = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i in range(4):
            for j in range(4):
                w_round[j][i] = w[(4*round) + i][j]

        for j in range(length):
            for x in range(4):
                for y in range(4):
                    blocks[j][x][y] = blocks[j][x][y] ^ w_round[x][y]              
        for x in range(length):
            for y in range(4):
                for j in range(4):
                    blocks[x][y][j] = chr(blocks[x][y][j])
        valid -= 1

    res = ""
    for x in range(lenght):
        for y in range(4):
            for j in range(4):
                res += blocks[x][j][y]
    
    return res

# def main():
#     array = initialize()
#     length = int(array[-1])
#     array.pop(-1)
#     blocks = []
#     for i in range(length):
#         sorted_array = []
#         sorted_array = matrix(array[i])
#         blocks.append(sorted_array)

#     key = input("Enter the key to encrypt with (length of 16 characters): ")
#     if (len(key) != 16):
#         while (len(key) != 16):
#             print("Invalid length for the key. Please try again.")
#             key = input("Enter the key to encrypt with (length of 16 characters): ")
    
#     init_key = []
#     for i in range(16):
#         init_key.append(ord(key[i]))
#     w = []
#     for j in range(44):
#         w.append([])
    
#     index = 0
#     for x in range(4):
#         for y in range(4):
#             w[x].append(init_key[index])
#             index += 1
#     round = 0
#     w_round = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#     for i in range(4):
#         for j in range(4):
#             w_round[j][i] = w[(4*round) + i][j]
#     for j in range(length):
#         for x in range(4):
#             for y in range(4):
#                 blocks[j][x][y] = ord(blocks[j][x][y])
#                 blocks[j][x][y] = blocks[j][x][y] ^ w_round[x][y]
#     for x in range(length):
#         for y in range(4):
#             for j in range(4):
#                 blocks[x][y][j] = chr(blocks[x][y][j])

#     valid = 10
#     while (valid != 0):
#         for x in range(length):
#             for y in range(4):
#                 subBytes(blocks[x][y])
#         for x in range(length):
#             shiftRows(blocks[x])
        
#         if (round < 9):
#             before_addkey = []
#             for x in range(length):
#                 for y in range(4):
#                     for j in range(4):
#                         blocks[x][y][j] = hex(ord(blocks[x][y][j]))
#                         blocks[x][y][j] = blocks[x][y][j][2:]
#                 result = mixColumn(blocks[x])
#                 before_addkey.append(result)
            
#             for x in range(length):
#                 for y in range(4):
#                     for j in range(4):
#                         blocks[x][j][y] = before_addkey[x][y][j]
#         else:
#             for x in range(length):
#                 for y in range(4):
#                     for j in range(4):
#                         blocks[x][y][j] = ord(blocks[x][y][j])

#         round += 1
        
#         w = addroundKey(w,round)
#         w_round = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#         for i in range(4):
#             for j in range(4):
#                 w_round[j][i] = w[(4*round) + i][j]

#         for j in range(length):
#             for x in range(4):
#                 for y in range(4):
#                     blocks[j][x][y] = blocks[j][x][y] ^ w_round[x][y]              
#         for x in range(length):
#             for y in range(4):
#                 for j in range(4):
#                     blocks[x][y][j] = chr(blocks[x][y][j])
#         valid -= 1
#     string_f = ''
#     for x in range(length):
#         for y in range(4):
#             for j in range(4):
#                 string_f += blocks[x][j][y]
#     print(string_f)

