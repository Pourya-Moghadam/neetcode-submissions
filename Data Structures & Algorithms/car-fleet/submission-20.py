class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleet = []
        for p, s in zip(position, speed):
            cars.append((p, s))
        
        cars.sort(reverse=True)

        for p, s in cars:
            time = (target - p) / s
            if fleet and fleet[-1] >= time:
                continue
            fleet.append(time)
        
        return len(fleet)
            