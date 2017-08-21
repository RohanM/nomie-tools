import json
import random

class NomieBackup:
    def __init__(self, filename):
        with open(filename) as f:
            self.data = json.loads(f.read())

    def add_tracker(self, name):
        id = self._random_id()
        self.data['trackers'].append({'_id': id, 'label': name})
        return id

    def add_tracker_to_group(self, tracker_id, group_name):
        groups = self.data['meta'][self._groups_meta_index()]['groups']
        if group_name not in groups:
            groups[group_name] = []
        groups[group_name].append(tracker_id)

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(self.data))

    def _random_id(self):
        # 13 digits decimal - 6 digits hex
        # eg. 0123456789012-abcdef
        return "{:013d}-{:06x}".format(random.randint(0, 9999999999999), random.randint(0, 16777215))

    def _groups_meta_index(self):
        # Find meta section with id "hyperStorage-groups"
        return [i for i, x in enumerate(self.data['meta']) if x['_id'] == "hyperStorage-groups"][0]
