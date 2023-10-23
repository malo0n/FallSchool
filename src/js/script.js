//вывод имени в превью
let userName = document.querySelector('.name_preview');
let nameInput = document.querySelector('.name');
nameInput.addEventListener('change', () => {
    userName.innerHTML = nameInput.value;
})

//вывод пола в превью
let userSex = document.querySelector('.preview_sex');
let radioInput = document.querySelectorAll('.custom-radio');
radioInput.forEach(element => {
    addEventListener('change', () => {
        if (element.checked) {
            userSex.innerHTML = element.value;
            userSex.style.cssText = 'color: #040013; font-weight:400; font-size: 9px; background-color: #FFF; width: auto;';
        }
})})

//вывод возраста в превью
let userAge = document.querySelector('.preview_age');
let ageInput = document.querySelector('.date input');
//функция вычисления возраста
function get_current_age(date) {
    return ((new Date().getTime() - new Date(date)) / (24 * 3600 * 365.25 * 1000));
}
ageInput.addEventListener('change', () => {
    userAge.innerHTML = (Math.floor(get_current_age(ageInput.value))) + ' лет';
    userAge.style.cssText = 'color: #040013; font-weight:400; font-size: 9px; background-color: #FFF; width: auto;';
})

//'развернуть' информацию пользователя "О себе"
let userInfo = document.querySelector('.about__me textarea');
let showMore = document.querySelector('.userInfoContainer img');
let infoBox = document.querySelector('.aboutUserInfo');
let infoText = document.querySelector('.aboutUserInfo p');
userInfo.addEventListener('change', () => {
    infoText.innerHTML = userInfo.value;
    document.querySelector('.userInfoContainerPreview').style.display = 'none';
    document.querySelector('.userInfoContainer').style.display = "flex";
    infoBox.style.cssText ='color: #040013; font-weight:400; font-size: 9px; background-color: #FFF; max-width:100%; word-wrap: break-word;';
    infoText.offsetWidth >= 200 ? showMore.style.display = "flex" : showMore.style.display = 'none';
})
showMore.addEventListener("click", () => {
        infoBox.classList.toggle('active');
        showMore.src = (showMore.src.includes("show_more.svg"))? "/src/img/svg/show_less.svg" : "/src/img/svg/show_more.svg";
});

//загрузка аватара
let inputAvatar = document.querySelector('.inputAvatar');
let userAvatar = document.querySelector('.userAvatar');
let userAvatarPreview = document.querySelector('.picture');
inputAvatar.addEventListener('change', function(){
    userAvatar.src = URL.createObjectURL(inputAvatar.files[0]);
    userAvatar.style.display = "block";
    document.querySelector('.avatar').style.display = "none";
    userAvatarPreview.style.backgroundImage = `url(${userAvatar.src})`;
    userAvatarPreview.style.border = "none";
});


//Блок с валидацией полей

//валидация имени и фамилии
function isValidName(name) {
    const pattern = /^[а-яА-Я a-zA-Z]/;
    return pattern.test(name);
}
let nameRequired = document.querySelector('.nameRequired');
let nameIncorrect = document.querySelector('.nameIncorrect');
function invalidNameInputStyle (input){
    input.style.border = "1px solid red";
    input.style.background = "rgba(255, 0, 0, 0.05)";
    document.querySelector('.input__name label').style.color = "red";
    if(!input.value){
        nameRequired.style.display = "flex";
        nameIncorrect.style.display = "none";
    }
    else {
        nameIncorrect.style.display = "flex";
        nameRequired.style.display = "none";
    }
}
function validNameInputStyle (input){
    input.style.border = "none";
    input.style.background = "#F4F4F6";
    document.querySelector('.input__name label').style.color = "rgb(93, 91, 102)";
    nameRequired.style.display = "none";
    nameIncorrect.style.display = "none";
}
nameInput.addEventListener('change', () =>{ //nameInput уже объявлен в самом начале, при дублировании данных в preview 
    let username = nameInput.value;         //остальные input'ы будут объявлены через const
    if(!isValidName(username)) invalidNameInputStyle(nameInput);
    else validNameInputStyle(nameInput);
})
nameInput.addEventListener('blur', () =>{
    if(!nameInput.value) invalidNameInputStyle(nameInput);
})

//валидация даты рождения

const dateInput = document.querySelector('.date input');
let dateRequired = document.querySelector('.dateRequired');
function invalidDateInputStyle (input){
    input.style.border = "1px solid red";
    input.style.background = "rgba(255, 0, 0, 0.05)";
    document.querySelector('.date label').style.color = "red";
    dateRequired.style.display = "flex";
}
function validDateInputStyle (input){
    input.style.border = "none";
    input.style.background = "#F4F4F6";
    document.querySelector('.date label').style.color = "rgb(93, 91, 102)";
    dateRequired.style.display = "none";
}
dateInput.addEventListener('change', () =>{ 
    let date = dateInput.value;         
    if(!date) invalidDateInputStyle(dateInput);
    else validDateInputStyle(dateInput);
})
dateInput.addEventListener('blur', () =>{
    if(!dateInput.value) invalidDateInputStyle(dateInput);
})

// валидация телеграма

const telegramInput = document.querySelector('.telegram input');
function isValidTelegram(telegram) {
    const pattern= /^@[a-zA-Z0-9]/;
    return pattern.test(telegram);
}
let telegramRequired = document.querySelector('.telegramRequired');
let telegramIncorrect = document.querySelector('.telegramIncorrect')
function invalidTelegramInputStyle (input){
    input.style.border = "1px solid red";
    input.style.background = "rgba(255, 0, 0, 0.05)";
    document.querySelector('.telegram label').style.color = "red";
    if(input.value == ""){
        telegramRequired.style.display = "flex";
        telegramIncorrect.style.display = "none";
    }
    else {
        telegramIncorrect.style.display = "flex";
        telegramRequired.style.display = "none";
    }
}
function validTelegramInputStyle (input){
    input.style.border = "none";
    input.style.background = "#F4F4F6";
    document.querySelector('.telegram label').style.color = "rgb(93, 91, 102)";
    telegramRequired.style.display = "none";
    telegramIncorrect.style.display = "none";
}

telegramInput.addEventListener('change', () =>{
    let telegram = telegramInput.value;
    if(!isValidTelegram(telegram)) invalidTelegramInputStyle(telegramInput);
    else validTelegramInputStyle(telegramInput);
})
telegramInput.addEventListener('blur', () =>{
    if(!telegramInput.value) invalidTelegramInputStyle(telegramInput);
})



//валидация номера телефона

function isValidPhone(phone) {
    const pattern= /^8[0-9]/;
    return pattern.test(phone);
}
const phoneInput = document.querySelector('.phone');
let phoneRequired = document.querySelector('.phoneRequired');
let phoneIncorrect = document.querySelector('.phoneIncorrect');
function invalidPhoneInputStyle (input){
    input.style.border = "1px solid red";
    input.style.background = "rgba(255, 0, 0, 0.05)";
    document.querySelector('.telnum label').style.color = "red";
    if(!input.value){
        phoneRequired.style.display = "flex";
        phoneIncorrect.style.display = "none";
    }
    else {
        phoneIncorrect.style.display = "flex";
        phoneRequired.style.display = "none";
    }
}
function validPhoneInputStyle (input){
    input.style.border = "none";
    input.style.backgroundColor = "#e8f0fe";
    document.querySelector('.telnum label').style.color = "rgb(93, 91, 102)";
    phoneRequired.style.display = "none";
    phoneIncorrect.style.display = "none";
}

phoneInput.addEventListener('change', () =>{
    let phone = phoneInput.value;
    if(!isValidPhone(phone)) invalidPhoneInputStyle(phoneInput);
    else validPhoneInputStyle(phoneInput);
})
phoneInput.addEventListener('blur', () =>{
    if(!phoneInput.value) invalidPhoneInputStyle(phoneInput);
})

//валидация поля "О себе"
const aboutUserInput = document.querySelector('.about__me textarea');
let aboutMeRequired = document.querySelector('.aboutMeRequired');
function invalidAboutUserInputStyle (input){
    input.style.border = "1px solid red";
    input.style.background = "rgba(255, 0, 0, 0.05)";
    document.querySelector('.about__me label').style.color = "red";
    if(!input.value){
        aboutMeRequired.style.display = "flex";
    }
    else {
        aboutMeRequired.style.display = "none";
    }
}
function validAboutUserInputStyle (input){
    input.style.border = "none";
    input.style.background = "#F4F4F6";
    document.querySelector('.about__me label').style.color = "rgb(93, 91, 102)";
    aboutMeRequired.style.display = "none";
}
aboutUserInput.addEventListener('blur', () =>{
    if(!aboutUserInput.value) invalidAboutUserInputStyle(aboutUserInput);
    else validAboutUserInputStyle(aboutUserInput);
})





  
  