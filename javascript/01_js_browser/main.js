/* 1. <input> 태그 안의 값을 잡는다. */
const inputArea = document.querySelector('#js-userinput')
const button = document.querySelector('#js-go')
const resultArea = document.querySelector('#result-area')
const inputValue = inputArea.value

button.addEventListener('click', e => {
    requestGiphy(inputArea.value)
})

inputArea.addEventListener('keydown', e => {
    if (e.keyCode === 13){
        requestGiphy(inputArea.value)
    }
})
/* 2. Giphy API 를 통해 data 를 받아서 가공한다. */
const requestGiphy = keyword => {
    const API_KEY = token
    // let keyword = 'samsung'
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

    const GiphyAPICall = new XMLHttpRequest()
    GiphyAPICall.open('GET', URL)
    GiphyAPICall.send()

    GiphyAPICall.addEventListener('load', e => {
        const parsedData = JSON.parse(e.target.response)
        const imageData = parsedData.data
        pushToDOM(imageData)
    })
}
/* 3. GIF 파일들을 index.html(DOM)에 밀어 넣어서 보여준다. */

const pushToDOM = datas => {
    resultArea.innerHTML = ''
    datas.forEach( data => {
        let imgurl = data.images.original.url
        const elem = document.createElement('img')
        // elem.innerText = imgurl
        elem.src = imgurl
        elem.className = 'container-image'
        resultArea.appendChild(elem)
    })
    
}