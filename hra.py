import multiprocessing
from hadanka import Hadanka
import configparser

class Hra:
    def __init__(self):
        self.delka_slov = 0

    def hraj(self, hadanka : Hadanka, seznam_slov : list):
        """
        Metoda pro hraní hadanky
        :param hadanka:
        :param seznam_slov:
        :return: void
        """
        uhadnuto = []
        for i in range(0, hadanka.pocet_slov()):
            uhadnuto.append('nevim')

        for slovo in seznam_slov:
            vysledek = hadanka.hadej_slovo(slovo)
            if(len(vysledek)>0):
                for pozice in vysledek:
                    uhadnuto[pozice] = slovo
                    print("Uhodl jsem slovo " + slovo + " na pozici " + str(pozice))

        print(" ".join(uhadnuto))
        self.delka_slov = len(uhadnuto)

    def metoda_pro_hraní(self, hadanka, hra):
        """
        Doplňte kód metody tak, aby se vytvořila nová instance třídy Hra a spustila metoda hraj.
        :param hadanka:
        :param hra:
        :return: string s výsledkem hry
        """
        # seznam slov pro hadání
        seznam_slov = [x.strip() for x in open('CZ.txt', encoding="utf8").readlines()]
        delka_seznamu = len(seznam_slov)

        # vytvoření více procesů
        procesy = []
        for i in range(multiprocessing.cpu_count()):
            p = multiprocessing.Process(target=hra.hraj, args=(
            hadanka, seznam_slov[i::multiprocessing.cpu_count()]))
            procesy.append(p)
            p.start()

        config = configparser.ConfigParser()
        config.read('config.ini')
        timeout = config.getint('settings', 'timeout')

        # čekání na dokončení procesů
        for p in procesy:
            if hra.delka_slov == hadanka.pocet_slov():
                if p.is_alive():
                    p.kill()
            p.join(timeout)

        if (hadanka.hadej_vetu(hadanka.get_veta())):
            return "Vyhral jsem, věta je: " + hadanka.get_veta()
        else:
            return "Prohral jsem"

if __name__ == '__main__':

    # vytvoření instance tříd Hadanka a Hra
    hadanka = Hadanka(input("Zadejte větu, jenž bude hádankou: "))
    hra = Hra()
    print(hra.metoda_pro_hraní(hadanka, hra))
