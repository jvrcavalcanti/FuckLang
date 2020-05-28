import sys

class Interpreter:
    def __init__(self):
        self.spaces = {
            0: 0
        }
        self.index = 0
        self.debug = False

    def error(self, line: int):
        print("\nError line: " + str(line), end="")

    def get_space(self):
        return self.spaces[self.index]

    def set_space(self, value: int):
        self.spaces[self.index] = value

    def convert_ascii(self):
        return chr(self.get_space())

    def set_index(self, value: int):
        if self.index + value >= 0:
            self.index += value
            if not self.index in self.spaces:
                self.set_space(0)

    def set_value_space(self, value: int):
        if self.get_space() + value >= 0:
            self.set_space(self.get_space() + value)

    def run_comand(self, line: str):
        if line[0] == "+" or line[0] == "-":
            self.set_value_space(int(line))
            return True

        if line[0] == "<" or line[0] == ">":
            posi = 0
            nega = 0
            posi += line.count(">")
            nega += line.count("<")
            self.set_index(posi - nega)
            return True

        if line[0] == ".":
            print(self.convert_ascii(), end="")
            return True

        if line[0] == "@":
            self.set_space(0)
            return True

        if line[0] == "$":
            if not int(line[1:]) in self.spaces:
                return False
            self.set_space(self.spaces[int(line[1:])])
            return True

        if len(line) == 1 or line[0] == " " or line[0] == "#":
            return True

        return False

    def run(self, args: list):
        if "-d" in args:
            self.debug = True

        with open(args[0], "r") as file:
            comands = file.readlines()
            for line in range(len(comands)):
                comand = comands[line]

                result = self.run_comand(comand)
                
                if result is False:
                    self.error(line + 1)
                    break

        if self.debug:
            print()
            print("**** Debug ****")
            print("Spaces used: " + str(self.spaces))
            print("Last space used: " + str(self.index))

if __name__ == "__main__":
    inter = Interpreter()
    inter.run(sys.argv[1:])