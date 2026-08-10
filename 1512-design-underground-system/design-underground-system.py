from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.station_to_station = defaultdict(lambda: (0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, t1 = self.check_in[id]
        time = t-t1
        t2, journeys = self.station_to_station[(start, stationName)]
        self.station_to_station[(start, stationName)] = (t2+time, journeys+1)
        del self.check_in[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, journeys = self.station_to_station[(startStation, endStation)]
        return time/journeys


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)