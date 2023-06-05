


function updateCountdown() {
    const now = new Date();
    const currentYear = now.getFullYear();
    const nextYear = currentYear + 1;
    const newYear = new Date(nextYear, 0, 1);
    const remainingTime = newYear - now;

    // Calcular los componentes de tiempo (días, horas, minutos, segundos)
    const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
    const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

    // Mostrar el contador en la página
    const diaElement = document.getElementById('diaCant')
    const horaElement = document.getElementById('horaCant')
    const minutoElement = document.getElementById('minutoCant')
    const segElement = document.getElementById('segundoCant')
    diaElement.textContent = days;
    horaElement.textContent = hours;
    minutoElement.textContent = minutes;
    segElement.textContent = seconds;

    // Reproducir el sonido cuando baja un segundo
    if (remainingTime > 0) {
        playTickSound();
    }
}

function playTickSound() {
    const tickSound = document.getElementById('tickSound');
    tickSound.currentTime = 0; // Reiniciar la reproducción desde el principio
    tickSound.play();
}

setInterval(updateCountdown, 1000);
const tickSound = document.getElementById('tickSound');
tickSound.addEventListener('ended', playTickSound);
updateCountdown();