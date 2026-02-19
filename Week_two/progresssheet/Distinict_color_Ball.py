class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_mapper = {}
        color_count = {}
        distinct_count = 0
        result = []

        for index, color in queries:

            if index in color_mapper:
                old_color = color_mapper[index]
                color_count[old_color] -= 1

                if color_count[old_color] == 0:
                    distinct_count -= 1

            color_mapper[index] = color

            if color not in color_count or color_count[color] == 0:
                distinct_count += 1
                color_count[color] = 0

            color_count[color] += 1

            result.append(distinct_count)

        return result
