while True:
        print("\nвиберіть функцію \n.1 додати \n.2 відняти \n.3 множити \n.4 ділити")
        a = int(input())
        if a == 1:
            b = int(input("Ведіть число яке будете додавати"))
            c = int(input("Ведіть число на яке будете додавати"))
            d = (b+c)
            print(d)
        elif a == 2:
            e = int(input("Ведіть число яке будете віднімати"))
            f = int(input("Ведіть число на яке будете віднімати"))
            g = (e-f)
            print(g)
        elif a == 3:
            h = int(input("Ведіть число яке будете множити"))
            r = int(input("Ведіть число на яке будете множити"))
            i = (h*r)
            print(i)
        elif a == 4:
            j = int(input("Ведіть число яке будете ділити"))
            u = int(input("Ведіть число на яке будете ділити"))
            if u == 0 :
                print("на ноль ділити не можна")
                break
            o = (j/u)
            print(o)
        