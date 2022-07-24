class Solution:
    def distanceBetweenBusStops(self, distance,start,destination):
        sum_distance = 0
        for i in distance:
            sum_distance = sum_distance + i
        if start > destination:
            start, destination = destination, start
        distances = 0
        for i in range(start, destination):
            distances = distances + distance[i]
        return distances if distances < sum_distance-distances else sum_distance-distances

