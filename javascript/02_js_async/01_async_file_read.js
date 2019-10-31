const fs = require('fs')

let f2 = ''

// console.log('파일 읽기 전')
// fs.readFile('data2.json', (err, data)=> {
//     console.log('파일 읽기')
//     const f = JSON.parse(data)
//     setTimeout(()=>{
//         console.log(f)
//     },1000)
//     console.log(f.name)
// })
// console.log('끝')

console.log('파일 읽기 전')
f2 = fs.readFileSync('data2.json')
console.log(2)

console.log(f2)
console.log(1)

console.log('끝')
