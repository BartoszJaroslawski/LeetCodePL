    
    
    
def twoSum(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            print("ustalony zakres pierwszej petli od", i, "do",len(nums)-2)
            for j in range(i+1, len(nums)):
                print("zakres drugiej petli od", i + 1, "do", len(nums)-1)
                print("a moze?" ,j)
                if nums[i] + nums[j] == target:
                    print("If zwraca prawde")
                    
                    return["Oto wynik: ", i, j] 

print("suma to: ",twoSum([2,3,4,5,6], 5))
print("Znalazl od razu te miejsca w tablicy")
print("suma to: ",twoSum([2,3,4,5,6], 11))
print("suma to: ",twoSum([2,3,4,5,6], 7))
print("suma to: ",twoSum([2,3,4,5,6], 9))
