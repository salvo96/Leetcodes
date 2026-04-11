class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        num_teams = len(skill) / 2

        sum_skills = 0
        for player_skill in skill:
            sum_skills += player_skill

        team_sum = sum_skills // num_teams
        if sum_skills % num_teams != 0:
            return -1

        skill_match_dict = dict()
        for player_skill in skill:
            skill_match_dict[team_sum - player_skill] = player_skill

        sum_chemistry = 0
        for player_skill in skill:
            skill_value = skill_match_dict.get(player_skill)
            if not skill_value:
                return -1
            sum_chemistry += player_skill * skill_value

        return int(sum_chemistry / 2)
