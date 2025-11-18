class Rescuer:
    def __init__(self, rescuers_id, first_name, last_name, fire_department_id, rang):
        self.rescuers_id = rescuers_id
        self.first_name = first_name
        self.last_name = last_name
        self.fire_department_id = fire_department_id
        self.rang = rang

    def to_dict(self):
        return {
            "rescuers_id": self.rescuers_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "fire_department_id": self.fire_department_id,
            "rang": self.rang
        }