# Description: Progress tracker class used in all levels
class Progress:

    # Attributes
    def __init__(self, level, threshold, total):
        self.level = level
        self.threshold = threshold
        self.total = total
        self.pts = 0

    # -------------------------------------------------------
    # Methods
    
    # Retrieves current points
    def get_pts(self):
        return self.pts

    # Retrieves max points
    def get_total_qns(self):
        return self.total

    # Awards points
    def add_pt(self, n):
        self.pts += n
    
    # Check if user has enough points to be considered proficient (as set by self.threshold)
    def check_proficiency(self):
        if self.pts >= self.threshold:
            return True
        else:
            return False

    # Can I make this look nicer?....
    def progress_report(self):
        return f"""\n
        ＼(＾O＾)／
        You scored {self.pts}/{self.total} in the {self.level} level!
        """