function add(x, y) {
    return x + y
}

// 함수 표현식 (주로 사용)
const sub = function(x, y) {
    return x - y
}

// arrow function(ES6)
const mul = (x, y) => {
    return x * y
}

const ssafy = function (name) {
    return `안녕, ${name}`
}

// 인자쪽 괄호는 인자가 1개일떄
//  를락을 없애는 조건은 표현식이 하나만 있을 경우
const ssafy1 = name => `안녕, ${name}`

const ssafy2 = () => {}

const square = num => num ** 2

console.log(square(2))
