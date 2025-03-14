from twoSum.twoSum import TwoSum;

class TwoSumTest():
    def test_data(self):
        return [
            # ✅ 일반적인 케이스 (짝이 존재)
            {"nums": [4, 1, 9, 7, 5, 3, 16], "target": 14},  # (9, 5)
            {"nums": [2, 7, 11, 15], "target": 9},           # (2, 7)
            {"nums": [3, 2, 4], "target": 6},               # (2, 4)
            {"nums": [-1, 2, 1, -4, 3], "target": 2},       # (-1, 3)
            
            # ✅ 중복 요소가 있는 경우
            {"nums": [1, 3, 3, 3, 5, 6], "target": 6},      # (3, 3)
            {"nums": [5, 5, 5, 5], "target": 10},          # (5, 5)
            
            # ✅ 정렬된 입력값
            {"nums": [1, 2, 3, 4, 5, 6], "target": 7},      # (1, 6)
            {"nums": [-10, -5, 0, 5, 10], "target": 0},     # (-10, 10)
            
            # ✅ 짝이 존재하지 않는 경우
            {"nums": [1, 2, 3, 4], "target": 10},          # 없음
            {"nums": [1], "target": 2},                    # 없음 (리스트에 하나의 숫자만 존재)
            {"nums": [], "target": 5},                     # 없음 (빈 리스트)
        ]
    
    def test_main(self):
        call_value = 'two_sum_sort'
        two_sum_instance = TwoSum()
        two_sum_instance.two_sum_main(call_value, self.test_data())