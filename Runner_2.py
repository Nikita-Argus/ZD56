class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(*participants)
        self.participants = list(participants)

    def start(self):
        finishers = {}