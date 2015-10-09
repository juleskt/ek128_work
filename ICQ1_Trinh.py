student_id = 'U24431781'
student_name = 'Julian Trinh'
seq = input("Que es tu sequence?")

seq_length = len(seq)

def is_plain(seq):
    check1 = 0

    for x in range (1, seq_length-1, 1):
        if seq[x] == seq[x-1]:
            check1 = check1 + 1
        else:
            check1 = check1 - 1
    if check1 > 0:
            return True
        
    else:
            return False

def is_ramp(seq):
    check1 = 0
    
    for x in range(1, seq_length-1, 1):
        if seq[x] > seq[x-1]:
            check1 = check1 + 1
        else:
            check1 = check1 - 1
    if check1 > 0:
            return True
    else:
            return False

def is_slope(seq):
    check1 = 0
    for x in range (1, seq_length, 1):
        if seq[x] < seq[x-1]:
           check1 = check1 + 1
        else:
            check1 = check1 - 1
    if check1 > 0:
        return True
    else:
        return False

def is_hill(seq):
        summit = max(seq)
        sumel = 0
            
        for x in range (1, seq_length, 1):
            if seq[x] == summit:
                sumel = x
            else:
                break
        
        if seq[sumel] <= seq[sumel-1] and seq[sumel] <= seq[sumel+1]:
            return True
        else:
            return False

def is_valley(seq):
    nadir = min(seq)
    nadel = 0

    for x in range (1, seq_length, 1):
        if seq[x] == nadir:
                nadel = x
        else:
            break
    if seq[nadel] >= seq[nadel-1] and seq[nadel] >= seq[nadel+1]:
            return True
    else:
            return False

is_plain(seq)
is_ramp(seq)
is_slope(seq)
is_hill(seq)
is_valley(seq)
