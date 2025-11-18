class Firedepartment:
    def __init__(self, fire_department_id, fire_department_name, district_id, adress):
        self.fire_department_id = fire_department_id
        self.fire_department_name = fire_department_name
        self.district_id = district_id
        self.adress = adress

    def to_dict(self):
        return {
            "fire_department_id": self.fire_department_id,
            "fire_department_name": self.fire_department_name,
            "district_id": self.district_id,
            "adress": self.adress
        }