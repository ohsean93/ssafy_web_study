const nums = [1, 2, 3, 4]

console.log(nums)
console.log(nums[0])
// console.log(nums[-1]) // 안됨
console.log(nums[nums.length-1])
console.log(nums.reverse())
console.log(nums)

console.log(nums.push(0))
console.log(nums.push(-1))
console.log(nums)
console.log(nums.pop())
console.log(nums.pop())
console.log(nums)

// nushift, shift, includes, indexOf

console.log(nums.unshift(5))
console.log(nums)
console.log(nums.shift())
console.log(nums)
console.log(nums.includes(3))
console.log(nums.includes(0))
console.log(nums.indexOf(2))


const square = num => num ** 2

// 반복문 : for (let num of nums){}

// nums.forEach(함수) : 배열을 순회하며 각각에 함수를 적용
let newNums = []
nums.forEach(function(num){
    newNums.push(num*num)
})
// console.log(nums.forEach(square))
console.log(newNums)

const squareNums = nums.map(square)
console.log(squareNums)