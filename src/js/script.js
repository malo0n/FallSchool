let userName = document.querySelector('.name_preview')
let userSex = document.querySelector('.preview_sex')
let nameInput = document.querySelector('.name')






nameInput.addEventListener('change', () => {
    userName.innerHTML = nameInput.value;
})


let radioInput = document.querySelectorAll('.custom-radio');
radioInput.forEach(element => {
    addEventListener('change', () => {
        if (r.checked && radio.value=="Парень") {
            userSex.innerHTML = "Парень";
        }
})})

