import ctypes
import re
import configparser
import multiprocessing


class Hadanka:
    def __init__(self, veta: str):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.lock = multiprocessing.Lock()
        self.nalezeno = multiprocessing.Value(ctypes.c_bool, False)

        if not re.match("^[a-ž ]+$", veta):
            raise Exception("Věta smí obsahovat malá pismena české abecedy a mezery.")
        self._max_word_length = config.getint('settings', 'max_word_length')
        self._veta = veta
        self._slova = veta.split(' ')

        lengths = [(len(slovo), slovo) for slovo in self._slova]
        for length, slovo in lengths:
            if length > self._max_word_length:
                raise Exception("Slovo " + slovo + " je delší než povolená délka slova.")

    def pocet_slov(self):
        """
        Vrací počet slov v hadance.
        :return: počet slov
        """
        return len(self._slova)

    def hadej_slovo(self, slovo : str):
        """
        Metoda pro hádání slova.
        :param slovo: zkouška slova
        :return:nalezené pozice slova v hadance
        """
        _nalezena_slova = []
        for i in range(len(self._slova)):
            if self._slova[i] == slovo:
                # získání zámku
                self.lock.acquire()
                try:
                    # nastavení sdílené proměnné na True
                    self.nalezeno.value = True
                finally:
                    # uvolnění zámku
                    self.lock.release()
                _nalezena_slova.append(i)
        return _nalezena_slova

    def hadej_vetu(self, veta : str):
        """
        Metoda pro hádání věty.
        :param veta: zkouška věty
        :return: věta je správná
        """
        return self._veta == veta
    ########################################
    def get_veta(self):
        """
        Metoda pro získání věty.
        :return: vrací větu
        """
        return self._veta

    def get_slova(self):
        """
        Metoda pro získání slov.
        :return: vrací slova
        """
        return self._slova
    ########################################