import sys
input = sys.stdin.readline 
def avg_grade(d: dict):
    a=d.values()
    s,c=0,0
    for item in a:
        try:
            s+=item 
            c+=1
        except Exception:
            continue 
    return s/c if c>0 else 0