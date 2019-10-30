const nothing = () => {
    console.log(1)
}

console.log('start')

// const startTime = new Date().getTime()
setTimeout(nothing,3000)
setTimeout(nothing,1)
setTimeout(nothing,300)
// sleep = sec => {
//     while ( new Date().getTime() - startTime < sec) {}
//     console.log(1)
// }

// sleep(1000)

console.log('end')