class Progress:

    def __init__(self, level, threshold, total):
        self.level = level
        self.threshold = threshold
        self.total = total
        self.pts = 0

    def get_pts(self):
        return self.pts

    def add_pt(self, n):
        self.pts += n
    
    def check_proficiency(self):
        if self.pts > self.threshold:
            return True
        else:
            return False

    # Can I make this look nicer?....
    def progress_report(self):
        return f"You scored {self.pts}/{self.total} in this {self.level} level!"