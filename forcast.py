from azuredb import AzureSQLDatabase

class Forecast:
    def __init__(self, region_name,warning_summary, issue_date, wind,sea_state,weather,visibility):
        self.region_name = region_name
        self.warning_summary = warning_summary
        self.issue_date = issue_date
        self.wind = wind
        self.sea_state = sea_state
        self.weather = weather
        self.visibility = visibility
        self.query = f"INSERT INTO dbo.forecast (region, warning, issue_date, wind, sea_state, weather, visibility) VALUES ('{self.region_name}','{self.warning_summary}', '{self.issue_date}', '{self.wind}', '{self.sea_state}', '{self.weather}', '{self.visibility}')"
    
    def saveToDatabse(self):
        db = AzureSQLDatabase()
        db.connect()
        db.execute_query(self.query)

    def __str__(self):
        print( f'Region: {self.region_name}\nWarning: {self.warning_summary}\nIssue Date: {self.issue_date}\nWind: {self.wind}\nSea State: {self.sea_state}\nWeather: {self.weather}\nVisibility: {self.visibility}\n')