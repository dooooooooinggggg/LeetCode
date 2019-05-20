import "sort"

func singleNumber(nums []int) int {
	sort.Slice(nums, func(i, j int) bool { return nums[i] < nums[j] })
	for i := 0; i < len(nums)-2; i += 2 {
		if nums[i] != nums[i+1] {
			if nums[i+1] == nums[i+2] {
				return nums[i]
			}
			return nums[i+1]
		}
	}
	return nums[len(nums)-1]
}
