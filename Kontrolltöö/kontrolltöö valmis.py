#esimene ülesanne:
esimene_arv = input("sisestage esimesne arv: ")
teine_arv = input("sisestage teine arv: ")
for vastus in range (int(esimene_arv), int(teine_arv)):
    if(vastus % 2 == 0):
        print(vastus)


#teine ülesanne:
f = open("kttekst.txt","r")
sonad = []
mittusona = 0
mittusonaüv=0
for line in f:
    line.rstrip()
    words = line.split()
    for word2 in words:
        if(len(word2)<5):
            mittusonaüv+=1
    for word in words:
        mittusona+=1
       
print("teksitfailis on:",mittusona,"sõna")
print("teksifailis on sõnu mis on üle viie tähe pikkad: ",mittusonaüv)


#kolmas ülessanne:
esimene_l=[11, 15, 6, 13, 13, 25, 32, 11, 20, 5, 31, 16, 32, 29, 11, 13, 3, 29, 28, 24]
teine_l=[5, 19, 16, 4, 12, 7, 2, 28, 34, 29, 29, 36, 6, 8, 24, 18, 31, 7, 1, 7]
print("listides korduvad elemendid on: ", set(esimene_l)& set(teine_l))

suurim =0
for nb in esimene_l:
    if nb>suurim:
        suurim = nb
for nb in teine_l:
    if nb>suurim:
        suurim=nb
print("kahe listi suurim nb on: ",suurim)

väikseim = suurim
for nb in esimene_l:
    if nb< väikseim:
        väikseim = nb
for nb in teine_l:
    if nb< väikseim:
        väikseim =nb
print("kahe listi väikseim nb on: ",väikseim)
vastus=0
mittu =0
for nb in esimene_l:
    vastus = vastus+nb
    mittu+=1
vastus = int(vastus) / int(mittu)
print("esimese listi keskmine väärtus on: ",vastus)

vastus=0
mittu =0
for nb in teine_l:
    vastus = vastus+nb
    mittu+=1
vastus = int(vastus) / int(mittu)
print("teise listi keskmine väärtus on: ",vastus)

vastus=0
mittu =0
for nb in esimene_l:
    vastus = vastus+nb
    mittu+=1
vastus = int(vastus) / int(mittu)

for nb in teine_l:
    vastus = vastus+nb
    mittu+=1
vastus = int(vastus) / int(mittu)
print("mõlema listi keskmine väärtus on:",vastus)

