// 0. 자바 스크립트롸 인사하기

// python
// name = 'jhon'
// print(name)

// x = 1 // 이렇게 선언하면 전역변수가 되어서 문제가 생김
let x = 1 // 지역변수 x 선언
// let x = 3 // 선언은 2번 불가
x = 3 // 재설정은 가능
console.log(x)

// 이래도 안됨(전역변수를 설정했기 떄문에)
// y = 1
// let y = 3
//

if (x == 3){
    let x = 4
    let y = 5
    console.log(x)
}

console.log(x)
// console.log(y)  // 이건 오류남

const MY_FAV = 13 // 상수 선언 못 바꿈, 재선언, 재설정 불가

console.log('내가 좋아하는 숫자 ' + MY_FAV)

console.log(`내가 좋아하는 숫자 ${MY_FAV}`)


// var z = 1 // 과거의 지역변수 할당 맨위로 올라가는 효과 => 안씀

