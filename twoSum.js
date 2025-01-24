

function twoSum(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                console.log(nums[i], nums[j], target)
                return [i, j]
            }
        }
    }
}

twoSum([1,3,4], 7)



function twoSumWithMap(nums, target) {
    let map = new Map()
  
    //[2,3,5]
    // target: 8
    let answer = []
    for (let i = 0; i < nums.length; i++) {
        // 3
        let dif = target - nums[i]

        if (map.has(dif)) {
            answer.push(map.get(dif), i)
        }
        //TODO: FIx this 
        // { 2 => 0 }, { 3 => 1}
        map.set(nums[i], i)
    }
    return answer
}

console.log('withMap:', twoSumWithMap([2,3,5], 8))