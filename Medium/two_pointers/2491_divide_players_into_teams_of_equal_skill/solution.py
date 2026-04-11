class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        num_teams = len(skill) / 2

        sum_skills = 0
        for num in skill:
            sum_skills += num

        team_sum = sum_skills / num_teams

        skill = sorted(skill)

        left, right = 0, len(skill) - 1

        sum_chemistry = 0
        while left < right:
            if skill[left] + skill[right] != team_sum:
                return -1
            sum_chemistry += skill[left] * skill[right]
            left, right = left + 1, right - 1

        return sum_chemistry
