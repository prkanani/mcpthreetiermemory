class Facilitator:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, I am {self.name}, a facilitator."


if __name__ == "__main__":
    pritesh = Facilitator("Pritesh Kanani")
    print(pritesh.introduce())
