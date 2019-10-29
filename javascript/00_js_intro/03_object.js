const fs = require('fs')

const me = {
    name: 'john',
    sleep: function() {
        console.log('쿨쿨')
    },
    appleProducts: {
        macBook: '2018pro',
        ipad: '2018pro',
    },
}

console.log(me['name'])
console.log(me.name)
console.log(me.sleep)
console.log(me.sleep())

const data = {
    name: 'john',
    appleProducts: {
        macBook: '2018pro',
        ipad: '2018pro',
    },

}


// object => JSON
const meJSON = JSON.stringify(data)
console.log(typeof(meJSON))
console.log(meJSON)
fs.writeFile('data.json', meJSON, err => {})
fs.writeFileSync('data2.json', meJSON)

// object <= JSON
const data2 = JSON.parse(meJSON)
console.log(typeof data2)
console.log(data2)
