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

invs = [['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],
        ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],
        ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],
        ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],
        ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],
        ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],
        ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],
        ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],
        ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],
        ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],
        ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],
        ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],
        ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'],
        ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],
        ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],
        ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']]
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


def invsubbyte(st):
    lt = re.findall(r'.{2}', st)
    s1 = ''
    for i in range(len(lt)):
        s1 += invs[int(lt[i][0], 16)][int(lt[i][1], 16)]
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


def invkeyexpansion(k):
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
    result1 = [result[0]]
    for i in range(1, len(result)-1):
        result1.append(combine(invmixcolumn(divide(result[i]))))
    result1.append(result[len(result)-1])
    return result1


def shiftrow(st):
    result = divide(st)
    temp = [result[1][1], result[1][2], result[1][3], result[1][0]]
    result[1] = temp
    temp = [result[2][2], result[2][3], result[2][0], result[2][1]]
    result[2] = temp
    temp = [result[3][3], result[3][0], result[3][1], result[3][2]]
    result[3] = temp
    return result


def invshiftrow(st):
    result = divide(st)
    temp = [result[1][3], result[1][0], result[1][1], result[1][2]]
    result[1] = temp
    temp = [result[2][2], result[2][3], result[2][0], result[2][1]]
    result[2] = temp
    temp = [result[3][1], result[3][2], result[3][3], result[3][0]]
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
            st1 = hex(mul(constant[i][0], st[0][j]) ^ mul(constant[i][1], st[1][j]) ^\
                      mul(constant[i][2], st[2][j]) ^ mul(constant[i][3], st[3][j]))[2:].zfill(2)
            result[i].append(st1)
    return result


def invmixcolumn(st):
    constant = [['0e', '0b', '0d', '09'],
                ['09', '0e', '0b', '0d'],
                ['0d', '09', '0e', '0b'],
                ['0b', '0d', '09', '0e']]
    result = [[], [], [], []]
    for i in range(4):
        for j in range(4):
            st1 = hex(mul(constant[i][0], st[0][j]) ^ mul(constant[i][1], st[1][j]) ^\
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


def encode(plaintext, k):
    keyexpan = keyexpansion(k)
    result = ''
    result += '明文:'+plaintext + '\n'
    result += '密钥:'+k + '\n'
    result += '加密扩展密钥:' + '\n'
    for i in range(len(keyexpan)):
        result += '\t' + keyexpan[i] + '\n'
    result += '明文初始状态:' + plaintext + '\n'
    result += '密钥:' + keyexpan[0] + '\n'
    addroundkey = hex(int(plaintext, 16) ^ int(keyexpan[0], 16))[2:].zfill(32)
    result += 'AddRoundKey:' + addroundkey + '\n'
    result += '\n'
    for i in range(1, 10):
        result += 'N=' + str(i) + '\n'
        st = subbyte(addroundkey)
        st = hex(st)[2:].zfill(32)
        result += 'SubBytes:' + st + '\n'
        st1 = shiftrow(st)
        result += 'ShiftRows:' + combine(st1) + '\n'
        st2 = mixcolumn(st1)
        result += 'MixColumns:' + combine(st2) + '\n'
        result += '轮密钥:' + keyexpan[i] + '\n'
        addroundkey = hex(int(combine(st2), 16) ^ int(keyexpan[i], 16))[2:].zfill(32)
        result += 'AddRoundKey:' + addroundkey + '\n'
        result += '\n'
    result += 'N=' + str(10) + '\n'
    st = subbyte(addroundkey)
    st = hex(st)[2:].zfill(32)
    result += 'SubBytes:' + st + '\n'
    st1 = shiftrow(st)
    result += 'ShiftRows:' + combine(st1) + '\n'
    result += '轮密钥:' + keyexpan[10] + '\n'
    addroundkey = hex(int(combine(st1), 16) ^ int(keyexpan[10], 16))[2:].zfill(32)
    result += 'AddRoundKey:' + addroundkey + '\n'
    result += '得到密文:' + addroundkey + '\n'
    return result


def decode(cipher, k):
    result = ''
    keyexpan = invkeyexpansion(k)
    result += '密文:' + cipher + '\n'
    result += '密钥:' + k + '\n'
    result += '解密扩展密钥:' + '\n'
    for i in range(len(keyexpan)):
        result += '\t' + keyexpan[i] + '\n'
    result += '密文初始状态:' + cipher +'\n'
    result += '密钥:' + keyexpan[0] + '\n'
    addroundkey = hex(int(cipher, 16) ^ int(keyexpan[10], 16))[2:].zfill(32)
    result += 'AddRoundKey:' + addroundkey + '\n'
    result += '\n'
    for i in range(1, 10):
        result += 'N=' + str(10-i+1) + '\n'
        st = invsubbyte(addroundkey)
        st = hex(st)[2:].zfill(32)
        result += 'InvSubBytes:' + st + '\n'
        st1 = invshiftrow(st)
        result += 'InvShiftRows:' + combine(st1) + '\n'
        st2 = invmixcolumn(st1)
        result += 'InvMixColumns:' + combine(st2) + '\n'
        result += '轮密钥:' + keyexpan[i] + '\n'
        addroundkey = hex(int(combine(st2), 16) ^ int(keyexpan[10-i], 16))[2:].zfill(32)
        result += 'AddRoundKey:' + addroundkey + '\n'
        result += '\n'
    result += 'N= ' +  str(1) + '\n'
    st = invsubbyte(addroundkey)
    st = hex(st)[2:].zfill(32)
    result += 'InvSubBytes:' + st + '\n'
    st1 = invshiftrow(st)
    result += 'InvShiftRows:' + combine(st1) + '\n'
    result += '轮密钥:' + keyexpan[0] + '\n'
    addroundkey = hex(int(combine(st1), 16) ^ int(keyexpan[0], 16))[2:].zfill(32)
    result += 'AddRoundKey:' + addroundkey + '\n'
    result += '解密得到明文:' + addroundkey + '\n'
    return result


if __name__ == '__main__':
    m = '0001000101a198afda78173486153566'
    key = '00012001710198aeda79171460153594'
    c = '6cdd596b8f5642cbd23b47981a65422a'
    cip1 = encode(m, key)
    cip2 = decode(c, key)
    cip = cip1 + '\n\n' + cip2
    print(cip)
    with open('result.txt', 'w') as f:
        f.write(cip)
    f.close()
