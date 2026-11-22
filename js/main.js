// Мобильное меню
document.addEventListener('DOMContentLoaded', () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav');
  if (burger && nav) {
    burger.addEventListener('click', () => nav.classList.toggle('is-open'));
  }
  // На мобильных пункт с подменю раскрывается по тапу
  document.querySelectorAll('.nav__item.has-drop > .nav__link').forEach(link => {
    link.addEventListener('click', e => {
      if (window.innerWidth <= 960) {
        e.preventDefault();
        link.parentElement.classList.toggle('is-open');
      }
    });
  });
});
