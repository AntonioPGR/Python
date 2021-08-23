class Validadores:
    def validate_entry2(self, txt):
        if txt == '': return True
        try:
            value = int(txt)
        except ValueError:
            return False
        return 0 <= value <= 100