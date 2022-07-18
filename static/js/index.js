

let closeBtn = document.querySelector('.fa-close')


closeBtn.addEventListener('click', () => {
    document.querySelector('.side-menu').classList.remove('active')
})

let openBtn = document.querySelector('.fa-list-ul')


openBtn.addEventListener('click', () => {
    document.querySelector('.side-menu').classList.add('active')
})

// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


let boshSahifa = document.querySelector('#boshSahifa')
let yaqinAtrof = document.querySelector('#yaqinAtrof')
let joylashuv = document.querySelector('#joylashuv')

let a = document.querySelector("#a")
let b = document.querySelector("#b")
let c = document.querySelector("#c")

boshSahifa.addEventListener('click', () => {
    boshSahifa.classList.add('active')
    yaqinAtrof.classList.remove('active')
    joylashuv.classList.remove('active')
    
    a.classList.add('active')
    b.classList.remove('active')
    c.classList.remove('active')
})

yaqinAtrof.addEventListener('click', () => {
    boshSahifa.classList.remove('active')
    yaqinAtrof.classList.add('active')
    joylashuv.classList.remove('active')
    
    a.classList.remove('active')
    b.classList.add('active')
    c.classList.remove('active')
})

joylashuv.addEventListener('click', () => {
    boshSahifa.classList.remove('active')
    yaqinAtrof.classList.remove('active')
    joylashuv.classList.add('active')
    
    a.classList.remove('active')
    b.classList.remove('active')
    c.classList.add('active')
})

