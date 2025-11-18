class District:
    def __init__(self, district_id, district_name, city_id):
        self.district_id = district_id
        self.district_name = district_name
        self.city_id = city_id

    def to_dict(self):
        return {
            "district_id": self.district_id,
            "district_name": self.district_name,
            "city_id": self.city_id
        }