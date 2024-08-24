class Token():
    def __init__(self, value, line):
        self.type = "undefined"
        self.value = value
        self.line = line

    def __repr__(self):
        return f"({self.type}, {self.value}, {self.line})"

    def displayToken(self):
        return f"\t({self.type}, {self.value}, {self.line})"
