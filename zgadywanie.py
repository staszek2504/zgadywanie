print ("Pomyśl dowolną liczbę w zakresie od 1 do 100, a ja ją odgadnę za pomocą komend: < > i =")

dolna = 1
gorna = 101


while 1 == 1:

    zgadula = int((dolna+gorna)/2)
    print("Czy ta liczba to",zgadula,"?")
    komenda1 = str(input())
    if komenda1 == (">"):
       dolna = zgadula
    if komenda1 == ("<"):
        gorna = zgadula    
    if komenda1 == ("="):
       print("Zgadłem! Ta liczba to",zgadula,"!")
       break
    