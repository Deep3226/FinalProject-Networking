import json
import random



class Util:
    def __init__(self, start_id=1):
        self.id = start_id
        self.temp = round(random.uniform(15, 25), 2)
        self.humid = round(random.uniform(30, 70), 2)
        self.aqi = round(random.uniform(50, 150), 0)
        self.hours = 0
        self.day = 0
        self.dates = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.date = 'Monday'


    def get_json_data(self):
        self.id += 1
        new_temp = round(random.uniform(self.temp - 1, self.temp + 1), 2)
        new_temp = round(15+10*random.random(), 2)
        diff_temp = round(new_temp - self.temp, 2)
        self.temp = new_temp
        self.humid = round(random.uniform(self.humid - 5, self.humid + 5), 2)
        self.aqi = round(random.uniform(self.aqi - 10, self.aqi + 10), 0)
        self.hours = self.hours+1
        if (self.hours==25):
            self.hours=1
            self.day=self.day+1
            if(self.day == 7):
                self.day = 0
        self.date = self.dates[self.day]

        data = {
            'id': self.date,
            'time': self.hours,
            'temperature': self.temp,
            'humidity': self.humid,
            'air_quality': self.aqi,
            'diff_temperature': diff_temp
        }

        return json.dumps(data)
