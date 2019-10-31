// const DogAPI = new XMLHttpRequest()

// DogAPI.open('GET', ...)
// DogAPI.senf()
// DogAPI.addEventListener('load')

const dogURL = 'https://dog.ceo/api/breeds/image/random'
const catURL = 'https://api.thecatapi.com/v1/images/search'
const dogButton = document.querySelector('#dog')
const catButton = document.querySelector('#cat')
const showRoom = document.querySelector('#showroom')

// const a = axios.get(URL)
// a.then(result =>{
//     console.log(result.data.message)
// })

const getDogAndPush = () => {
    axios.get(dogURL)
        .then(response => {
            let imageurl = response.data.message
            let dog_img = document.createElement('img')
            dog_img.src = imageurl
            dog_img.className = 'container-image'
            showRoom.appendChild(dog_img)
        })
}

const getCatAndPush = () => {
    axios.get(catURL)
        .then(response => {
            // console.log(response)
            let imageurl = response.data[0].url
            let cat_img = document.createElement('img')
            cat_img.src = imageurl
            cat_img.className = 'container-image'
            showRoom.appendChild(cat_img)
        })
}

dogButton.addEventListener('click', e => getDogAndPush())
catButton.addEventListener('click', e => getCatAndPush())