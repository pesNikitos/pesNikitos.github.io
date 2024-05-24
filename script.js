const clickButton = document.getElementById('click-button');
const resetButton = document.getElementById('reset-button');
const clickCountDisplay = document.getElementById('click-count');

// Функция для получения текущего количества кликов из localStorage
function getClickCount() {
  return parseInt(localStorage.getItem('clickCount')) || 0;
}

// Функция для обновления отображения количества кликов
function updateClickCountDisplay() {
  clickCountDisplay.textContent = getClickCount();
}

// Функция обработчика кликов
function handleButtonClick() {
  let clickCount = getClickCount();
  localStorage.setItem('clickCount', clickCount + 1);
  updateClickCountDisplay();
}

// Функция для сброса количества кликов
function handleResetClick() {
  localStorage.setItem('clickCount', 0);
  updateClickCountDisplay();
}

// Инициализация
document.addEventListener('DOMContentLoaded', () => {
  updateClickCountDisplay();
  clickButton.addEventListener('click', handleButtonClick);
  resetButton.addEventListener('click', handleResetClick);
});
