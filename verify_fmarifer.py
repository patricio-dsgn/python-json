
class Marifer:

    @classmethod
    def veri_1(self,cosa_a, cosa_b):
        print(cosa_a, cosa_b)

    @classmethod
    def veri_2(self,a):
        x = input(a)
        return x




Marifer.veri_1('arbol','perro')

test = Marifer.veri_2('ingresa algo Maldito!!: ')

print(test)