//вывод имени в превью
let userName = document.querySelector('.name_preview');
let nameInput = document.querySelector('.input__name input');
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






  
  