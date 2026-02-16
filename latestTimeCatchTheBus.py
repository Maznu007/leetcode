class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        s = set(passengers)
        j=0
        last_bording_time = -1
        last_filled_bus = False

        for i in buses:
            seats = 0
            while seats<capacity and j<len(passengers) and passengers[j]<= i:
                last_bording_time=passengers[j]
                j+=1
                seats+=1
            if i ==buses[-1]:
                if seats<capacity:
                    last_filled_bus=False
                else:
                    last_filled_bus = True
        if last_filled_bus== False:
            ansr = buses[-1]
        else:
            ansr = last_bording_time -1
        
        while ansr in s:
            ansr = ansr -1
        return ansr