from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)

    def delete_member(self, id):
        self._members = [m for m in self._members if m['id'] != id]

    def update_member(self, id, member):
        for i, m in enumerate(self._members):
            if m['id'] == id:
                self._members[i] = member
                break

    def get_member(self, id):
        for m in self._members:
            if m ['id'] == id:
                return m
        return None

    def get_all_members(self):
        return self._members