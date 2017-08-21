import json

class NomieBackup:
    def __init__(self, filename):
        with open(filename) as f:
            self.data = json.loads(f.read())

    def add_tracker(self, name):
        self.data['trackers'].append({'label': name})

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(self.data))
