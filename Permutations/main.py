class Solution(object):
    def recursive(self, answer, victim, remaining):
        if not remaining:
            answer.append(victim)
            return
        print(victim, remaining)
        for i in range(len(remaining)):
            next_victim = victim[:]
            next_victim.append(remaining[i])
            self.recursive(answer, next_victim, remaining[:i] + remaining[i + 1:])
    
    def permute(self, nums):
        answer = []
        self.recursive(answer, [], nums)

        return answer
        