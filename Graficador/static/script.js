const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

let isDrawing = false;
let currentColor = '#000000';
let currentLineWidth = 5;
let shouldErase = false;

function drawLine(x1, y1, x2, y2, color, lineWidth) {
  context.strokeStyle = color;
  context.lineWidth = lineWidth;
  context.lineCap = 'round';
  context.beginPath();
  context.moveTo(x1, y1);
  context.lineTo(x2, y2);
  context.stroke();
}


function saveDrawing() {
  const dataURL = canvas.toDataURL('image/png');
  const link = document.createElement('a');
  link.href = dataURL;
  link.download = 'drawing.png';
  link.click();
}


canvas.addEventListener('mousedown', (e) => {
  isDrawing = true;
  const x = e.offsetX;
  const y = e.offsetY;
  lastX = x;
  lastY = y;
});

canvas.addEventListener('mousemove', (e) => {
  if (!isDrawing) return;
  const x = e.offsetX;
  const y = e.offsetY;
  drawLine(lastX, lastY, x, y, shouldErase ? '#FFFFFF' : currentColor, currentLineWidth);
  lastX = x;
  lastY = y;
});

canvas.addEventListener('mouseup', () => {
  if (!isDrawing) return;
  isDrawing = false;
  const step = {
    color: shouldErase ? '#FFFFFF' : currentColor,
    lineWidth: currentLineWidth,
    fromX: lastX,
    fromY: lastY,
    toX: lastX,
    toY: lastY,
  };
});

canvas.addEventListener('mouseout', () => {
  isDrawing = false;
});

const colorPicker = document.getElementById('colorPicker');
const lineWidthRange = document.getElementById('lineWidthRange');
const eraserButton = document.getElementById('eraserButton');
const saveButton = document.getElementById('saveButton');

colorPicker.addEventListener('change', (e) => {
  shouldErase = false;
  currentColor = e.target.value;
});

lineWidthRange.addEventListener('input', (e) => {
  currentLineWidth = e.target.value;
});

eraserButton.addEventListener('click', () => {
  shouldErase = true;
  currentColor = '#FFFFFF';
});

saveButton.addEventListener('click', saveDrawing);

loadInput.addEventListener('change', (e) => {
  const file = e.target.files[0];
  loadDrawing(file);
});