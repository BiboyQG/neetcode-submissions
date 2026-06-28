class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_history = [homepage]
        self.forward_history = []

    def visit(self, url: str) -> None:
        self.back_history.append(url)
        self.forward_history = []

    def back(self, steps: int) -> str:
        if steps >= len(self.back_history):
            steps = len(self.back_history) - 1
        while steps:
            self.forward_history.append(self.back_history.pop())
            steps -= 1
        return self.back_history[-1]

    def forward(self, steps: int) -> str:
        if steps > len(self.forward_history):
            steps = len(self.forward_history)
        while steps:
            self.back_history.append(self.forward_history.pop())
            steps -= 1
        return self.back_history[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)