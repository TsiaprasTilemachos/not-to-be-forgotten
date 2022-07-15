
#
# Utilities used to help when dealing with fixed point numbers and
# specifically Q31. Used to test consept for embedded programming a.k.a C programming
#
def q31_to_float(fix):
    neg = ((fix>>31)&0x01) == 1
    flt = float(fix & 0x7fffffff) / float(1 << 31)
    if neg:
        flt = -flt
    return flt;

def float_to_q31(flt):
    fix = 0
    neg = flt<0
    flt = abs(flt)
    fix = int(flt * (1 << 31))
    
    if neg:
        fix = fix | 0x80000000
    return fix;

def Hex(num) :
    m = dict.fromkeys(range(16), 0);
    digit = ord('0')
    c = ord('a')
    for i in range(16) :
        if (i < 10) :
            m[i] = chr(digit)
            digit += 1
        
        else :
            m[i] = chr(c)
            c += 1
    res = ""
    if (not num) :
        return "0"

    if (num > 0) :
        while (num) :
            res = m[num % 16] + res
            num //= 16
    else :
        n = num + 2**16
        while (n) :
            res = m[n % 16] + res
            n //= 16

    return res
