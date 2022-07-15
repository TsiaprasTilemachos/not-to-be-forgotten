
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
