class Validadores:
    @staticmethod
    def ValidaCod(txt):
        if txt == '': return True
        try:
            value = int(txt)
        except ValueError:
            return False
        return 0 < value

    @staticmethod
    def ValidaPlaca(txt):
        if len(txt) > 7:
            return False
        elif len(txt) <= 3:
            try:
                int(txt[len(txt)-1])
            except:
                return True
            else:
                return False
        elif len(txt) == 4 or len(txt) >= 6:
            try:
                int(txt[len(txt)-1])
            except:
                return False
            else:
                return True
        return True

    @staticmethod
    def ValidaModelo(txt):
        if len(txt) > 30:
            return False
        return True