import re

s = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
     ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
     ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
     ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
     ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
     ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
     ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
     ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
     ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
     ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
     ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
     ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
     ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
     ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
     ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
     ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

rcon = ['01000000', '02000000', '04000000', '08000000', '10000000',
        '20000000', '40000000', '80000000', '1b000000', '36000000']


def rotl(st):
    lt = re.findall(r'.{2}', st)
    st1 = lt[1] + lt[2] + lt[3] + lt[0]
    return st1


def subbyte(st):
    lt = re.findall(r'.{2}', st)
    s1 = ''
    for i in range(len(lt)):
        s1 += s[int(lt[i][0], 16)][int(lt[i][1], 16)]
    return int(s1, 16)


def keyexpansion(k):
    keyexpand = re.findall(r'.{8}', k)
    for i in range(4, 44):
        temp = keyexpand[i - 1]
        if i % 4 == 0:
            temp = subbyte(rotl(temp)) ^ int(rcon[i // 4 - 1], 16)
            temp = hex(temp)[2:]
        temp = int(temp, 16)
        keyexpand.append('{:08x}'.format(temp ^ int(keyexpand[i - 4], 16)))
    result = []
    st = ''
    for i in range(len(keyexpand)):
        st += keyexpand[i]
        if i % 4 == 3:
            result.append(st)
            st = ''
    return result


def shiftrow(st):
    result = divide(st)
    temp = [result[1][1], result[1][2], result[1][3], result[1][0]]
    result[1] = temp
    temp = [result[2][2], result[2][3], result[2][0], result[2][1]]
    result[2] = temp
    temp = [result[3][3], result[3][0], result[3][1], result[3][2]]
    result[3] = temp
    return result


def mul(a, b):
    if a == '01':
        return int(b, 16)
    elif a == '02':
        temp = (bin(int(b, 16))[2:]).zfill(8)
        if temp[0] == '1':
            return (int(bin(int(b, 16) * 2)[3:], 2)) ^ 0x1b
        else:
            return int(b, 16) * 2
    elif a == '03':
        return mul('01', b) ^ mul('02', b)
    elif a == '0e':
        return mul('02', hex(mul('02', hex(mul('02', b))[2:]))[2:]) ^ mul('02', hex(mul('02', b))[2:]) ^ mul('02', b)
    elif a == '0b':
        return mul('02', hex(mul('02', hex(mul('02', b))[2:]))[2:]) ^ mul('03', b)
    elif a == '0d':
        return mul('02', hex(mul('02', hex(mul('02', b))[2:]))[2:]) ^ mul('02', hex(mul('02', b))[2:]) ^ mul('01', b)
    elif a == '09':
        return mul('02', hex(mul('02', hex(mul('02', b))[2:]))[2:]) ^ mul('01', b)


def mixcolumn(st):
    constant = [['02', '03', '01', '01'],
                ['01', '02', '03', '01'],
                ['01', '01', '02', '03'],
                ['03', '01', '01', '02']]
    result = [[], [], [], []]
    for i in range(4):
        for j in range(4):
            st1 = hex(mul(constant[i][0], st[0][j]) ^ mul(constant[i][1], st[1][j]) ^
                      mul(constant[i][2], st[2][j]) ^ mul(constant[i][3], st[3][j]))[2:].zfill(2)
            result[i].append(st1)
    return result


def combine(st):
    cip = ''
    for i in range(4):
        for j in range(4):
            cip += st[j][i]
    return cip


def divide(st):
    k = re.findall('.{2}', st)
    result = [[], [], [], []]
    for i in range(len(k)):
        if i % 4 == 0:
            result[0].append(k[i])
        elif i % 4 == 1:
            result[1].append(k[i])
        elif i % 4 == 2:
            result[2].append(k[i])
        else:
            result[3].append(k[i])
    return result


def encode(plaintext, k, gz, pos):
    keyexpan = keyexpansion(k)
    addroundkey = hex(int(plaintext, 16) ^ int(keyexpan[0], 16))[2:].zfill(32)
    for i in range(1, 10):
        st = subbyte(addroundkey)
        st = hex(st)[2:].zfill(32)
        st1 = shiftrow(st)
        if i == 9:
            st1[0][pos] = hex(int(st1[0][pos], 16) ^ gz)[2:]
        st2 = mixcolumn(st1)
        addroundkey = hex(int(combine(st2), 16) ^ int(keyexpan[i], 16))[2:].zfill(32)
    st = subbyte(addroundkey)
    st = hex(st)[2:].zfill(32)
    st1 = shiftrow(st)
    addroundkey = hex(int(combine(st1), 16) ^ int(keyexpan[10], 16))[2:].zfill(32)
    return addroundkey


def zhuru(plaintxt, k, cipher):
    guzhang = [0xa0, 0x89]
    xtime = [['02', '03', '01', '01'], ['01', '02', '03', '01'],
             ['01', '01', '02', '03'], ['03', '01', '01', '02']]
    pos_key = []
    possible = []
    for i0 in range(8):
        cip = encode(plaintxt, k, guzhang[i0 % 2], i0 // 2)
        cip1 = hex(int(cipher, 16) ^ int(cip, 16))[2:].zfill(32)
        lt1 = re.findall('.{2}', cip1)
        ltc = re.findall('.{2}', c)
        midlt1 = []
        midltc = []
        for i in range(len(lt1)):
            if lt1[i] != '00':
                temp = [i, lt1[i]]
                midlt1.append(temp)
                temp = [i, ltc[i]]
                midltc.append(temp)
        possible_key = []
        for j in range(len(midltc)):
            temp = []
            for i in range(255):
                if subbyte(hex(i ^ mul(xtime[i0 // 2][j], hex(guzhang[i0 % 2])[2:]))[2:].zfill(2)) == subbyte(
                        hex(i)[2:].zfill(2)) ^ int(midlt1[j][1], 16):
                    midkey = subbyte(hex(i)[2:].zfill(2)) ^ int(midltc[j][1], 16)
                    temp1 = [midltc[j][0], hex(midkey)[2:].zfill(2)]
                    temp.append(temp1)
            possible_key.append(temp)
        possible.append(possible_key)
        print(possible_key)
    for i in range(4):                                                            # 求每一组的交集
        for j in range(len(possible[2 * i])):
            for k in range(len(possible[2 * i][j])):
                for l in range(len(possible[2 * i + 1][j])):
                    if possible[2 * i][j][k][1] == possible[2 * i + 1][j][l][1]:
                        pos_key.append(possible[2 * i][j][k])
                        break
    last_key = ''
    for i in range(len(pos_key)):                                               # 将求出的密钥联接起来
        for item in pos_key:
            if item[0] == i:
                last_key += item[1]
                break
    print(pos_key)
    return last_key


if __name__ == '__main__':
    m = '0001000101a198afda78173486153566'
    key = '00012001710198aeda79171460153594'
    c = '6cdd596b8f5642cbd23b47981a65422a'
    pos_key1 = zhuru(m, key, c)
    lt = keyexpansion(key)
    print(lt[10])
    print(pos_key1)
