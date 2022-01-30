import random as B,string as A
while True:D=2000;E=' '.join(B.choices(A.ascii_uppercase+A.digits,k=10800));F=' '.join(B.choices(A.ascii_uppercase+A.digits,k=5));G=E*D;C=open(F,'a');C.write(str(G));C.close()
