let course = document.querySelector('.course');
let faculty = document.querySelector('.degree');
let educationProgram = document.querySelector('.educationProgram');
let courseUser = document.querySelectorAll('.radio');
courseUser.forEach(element => {
    addEventListener('change', () => {
        if (element.checked) {
            course.innerHTML = element.value;
            course.style.cssText = 'color: #040013; font-weight:400; font-size: 9px; background-color: #FFF; width: auto';
        }
})});
let degree = document.querySelector('.degree');
let radioInput = document.querySelectorAll('.custom-radio');
let studentBox = document.querySelector('.studentContainer');
let workerBox = document.querySelector('.workerContainer');
radioInput.forEach(element => {
    addEventListener('change', () => {
        if (element.checked && element.value == "student") {
            studentBox.style.display = "flex";
            workerBox.style.display = "none";

        }
        else if (element.checked && element.value == "worker") {
            studentBox.style.display = "none";
            workerBox.style.display = "flex";
            degree.innerHTML = "";
            course.innerHTML = "";
            jobPreview.innerHTML = "";
        }
        
})});
let showMore = document.querySelector('.userInfoContainer img');
let infoBox = document.querySelector('.aboutUserInfo');
let infoText = document.querySelector('.aboutUserInfo p');
window.onload = () => {
    document.querySelector('.picture').style.backgroundImage = `url(${window.localStorage.getItem('avatar')})`;
    document.querySelector('.name_preview').innerHTML = window.localStorage.getItem('name');
    document.querySelector('.preview_sex p').innerHTML = window.localStorage.getItem('gender');
    document.querySelector('.preview_age').innerHTML = window.localStorage.getItem('age');
    document.querySelector('.aboutUserInfo p').innerHTML = window.localStorage.getItem('userInfo');
    infoText.offsetWidth >= 200 ? showMore.style.display = "flex" : showMore.style.display = 'none';
    infoBox.style.cssText ='color: #040013; font-weight:400; font-size: 9px; background-color: #FFF; max-width:100%; word-wrap: break-word;';

}

// вот объясни мне, почему это работает =>
let jobPreview = document.querySelector('.preview_job');
let studentJob = document.querySelector('.studentJob input');
studentJob.addEventListener('change', () => {
    jobPreview.innerHTML = studentJob.value;
    
    jobPreview.style.backgroundColor = "#fff";

});

//а это НЕ РАБОТАЕТ
let workerJob = document.querySelector('.userJobContainer input');
workerJob.addEventListener('change', () => {
    jobPreview.innerHTML = workerJob.value;
    jobPreview.style.backgroundColor = "#fff";
});




showMore.addEventListener("click", () => {
        infoBox.classList.toggle('active');
        showMore.src = (showMore.src.includes("show_more.svg"))? "/static/img/svg/show_less.svg" : "/static/img/svg/show_more.svg";
});

inputDegree = document.querySelector('.degree_input');
inputFaculty = document.querySelector('.faculty_input');
inputCourse = document.querySelector('.course_input');
inputDegree.addEventListener('propertychange', () => {
    document.querySelector('.degree').innerHTML = inputDegree.innerHTML;
    console.log(5);
});

const dropdowns = document.querySelectorAll('.dropdown');
dropdowns.forEach(p => {
    p.style.color = "#5D5B66";
});
dropdowns.forEach(dropdown =>{

    const select = dropdown.querySelector('.select');
    const caret = dropdown.querySelector('.caret');
    const menu = dropdown.querySelector('.menu');
    const options = dropdown.querySelectorAll('.menu li');
    const selected = dropdown.querySelector('.selected');
    const input = dropdown.querySelector('input');
    select.addEventListener('click', () =>{
        select.classList.toggle('select-clicked');
        caret.classList.toggle('caret-rotate');
        menu.classList.toggle('menu-open');

    });
    options.forEach(option =>{
        option.addEventListener('click', () =>{
            selected.innerHTML = option.innerText;
            input.innerHTML = selected.innerHTML;
            selected.style.color = "#040013";
            select.classList.remove('selected-clicked');
            caret.classList.remove('caret-rotate');
            menu.classList.remove('menu-open');
            options.forEach(option =>{
                option.classList.remove('active');
            });
            option.classList.add('active');
        });
    });
});




//соре еще раз, тут еще можно допилить много чего, но я так задолбался
//это пипец...