class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) > 2:
            p1 = coordinates[0]
            p2 = coordinates[1]

            if p2[1] != p1[1]:
                const_ = (p2[0] - p1[0]) / (p2[1] - p1[1])
                for coord in coordinates:
                    if const_ * (coord[1] - p1[1]) + p1[0] != coord[0]:
                        return False
            else:
                for coord in coordinates:
                    if coord[1] != p1[1]:
                        return False

        return True
