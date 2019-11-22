# Vue.js

### Vue 인스터스

```javascript
const app = new Vue({
    // Vue인스턴스(ViewModel)가 어떤 HTML요소에 마운트 될지(적용될지)
    el: '',
    // 인스턴스에 사용하는 변수
    data: {},
    // 인스턴스가 사용할 매소드들
    method: {},
    // 미리 계산된 값을 반환(성능상의 이슈) => 캐실
    computed: {},
    // vue 인스턴스의 data 변경을 관찰하고 이에 반은
    watch: {
      지켜볼 data: {
        handler 메소드
    }
    },
})
```



### Vue Directive

```html
<p v-for></p>
<p v-if v-else v-else-if></p>
<p v-model></p>
<p v-on:(이벤트)></p><p @(이벤트)></p>
<p v-bind:(html속성이름)></p><p :(html속성이름)></p>
<p v-html></p>
<p v-text></p>
<p v-show></p>
```

### localStorage API

```javascript
// Creation
localStorage.setItem('key', 'value')

// Read
localStorage.getItem('key')

// Delete
localStorage.removeItem('key')

// Count
localStorage.length
```



### props

```javascript
// 1.Array
props: [],
props: {
	category: String,
  },
props: {
    category: {
        type: String,
        required: true,
        validator: function(value) {
            if (value.length !== 0){
                return true
            } else{
                return false
            }
        }
}
```





----

질문

completed의 계산 시점

localstorage의 수명

----

## SPA

### 단점

1. history 관리의 불편
2. SEO에 취약

### 해결법

1. hash bang 사용해 내부이동을 인지한다.(이건 저장됨)
2. js 의 라우팅을 사용하자(그중 하나가 vuerouter)



## vuerouter

설치는 `vue ui`에서 설치가 가능하다.(또는 vue install router와 vue add router를 사용해도 된다.)



## JWT





























