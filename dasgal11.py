#shatrin hulug deerh 2 bers koordinat ugugdsun bol negnee ideh esehiig shalga
x = int(input("bers 1iin x koordinat: "))
y = int(input("bers 1iin y koordinat: "))
a = int(input("bersiin x koordinat: "))
b = int(input("bersiin y koordinat: "))
if x==a or y==b:
    print("idsen")
elif abs(x-a) == abs(y-b):
    print("idsen")
else:
    print("ideegui")