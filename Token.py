class Token():
    def __init__(self, value, line):
        self.class_part = "undefined"
        self.value = value
        self.line = line

    def __repr__(self):
        return f"({self.class_part}, {self.value}, {self.line})"

    def displayToken(self):
        return f"\t({self.class_part}, {self.value}, {self.line})"
