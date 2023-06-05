// Verificar la compatibilidad del navegador con la API de reconocimiento de voz
if ('webkitSpeechRecognition' in window) {
    console.log('API de reconocimiento de voz disponible');
  } else {
    console.log('API de reconocimiento de voz no disponible en este navegador');
  }
  
  // Crear una instancia del objeto SpeechRecognition
  let recognition;
  let speechDataElement = document.getElementById('speechData');
  const btnPause = document.getElementById('btnPause')
  const btnPlay = document.getElementById('btnPlay')
  const mainContent = document.getElementById('mainContent')
  
  
  // Inicializar el reconocimiento de voz
  function initializeSpeechRecognition() {
    recognition = new webkitSpeechRecognition();
  
    // Establecer el idioma del reconocimiento de voz (opcional)
    recognition.lang = 'es-ES';
  
    // Establecer si el reconocimiento de voz continuará escuchando después de una pausa (opcional)
    recognition.continuous = true;
  
    // Evento para recibir resultados de reconocimiento de voz
    recognition.onresult = function(event) {
      let transcript = event.results[event.results.length - 1][0].transcript;
      speechDataElement.innerHTML += transcript + '<br>';
    };
  }
    // 
    function startOrStopRecord(){
        playTickSound();
        if(!mainContent.classList.contains('active')){
            btnPause.classList.add('active')
            mainContent.classList.add('active')
            btnPlay.classList.remove('active')
            recognition.start();
            }
        else{
            btnPause.classList.remove('active')
            mainContent.classList.remove('active')
            btnPlay.classList.add('active')
            recognition.stop();
        }
    }

  function playTickSound() {
    const tickSound = document.getElementById('tickSound');
    tickSound.currentTime = 0; // Reiniciar la reproducción desde el principio
    tickSound.play();
}   
  
  // Inicializar el reconocimiento de voz al cargar la página
  initializeSpeechRecognition();
  