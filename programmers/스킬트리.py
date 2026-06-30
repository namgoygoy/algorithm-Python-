def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        skill_clean = ""
        for letter in tree:
            if letter in skill:
                skill_clean += letter
        
        if skill.startswith(skill_clean):
            answer += 1
            
    return answer