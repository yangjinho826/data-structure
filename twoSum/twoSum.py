class TwoSum():
    def two_sum_main(self, call_value : str, test_cases : list) -> None :
        method = getattr(self, call_value, None)

        for i, case in enumerate(test_cases, 1):
            print(f"Test Case {i}: nums={case['nums']}, target={case['target']}")
            print(method(case['nums'], case['target']))
            print("-" * 40)

    def two_sum_sort(self, nums : list, target : int ) -> bool:
        nums.sort()
        
        left = 0
        right = len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum < target:
                left  += 1
                continue
            
            if sum > target:
                right -= 1
                continue

            return True

        return False

        
