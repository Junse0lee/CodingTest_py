#dic형태로 중복없이 진행 
#해당 숫자별 개수로 변환 
#해당 숫자의 수를 세고 
#만약 nums배열의 절반보다 크면 nums를 출력
#그게 아니면 dic형태의 해당 숫자들의 개수를 출력 

def solution(nums):
    return min(len(nums)//2, len(set(nums)))