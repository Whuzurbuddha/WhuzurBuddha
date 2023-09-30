$(document).ready(function(){
    let isDragging = false;
    let offsetX = 0;

    const object = document.getElementById(OBJECT YOU WANT TO MOVE);
    const container = document.getElementById(MOVE IN DIV);

    object.style.left = '0px';

    object.addEventListener('mousedown', (event) => {
        isDragging = true;
        offsetX = event.clientX - parseInt(object.style.left);
    });

    document.addEventListener('mousemove', (event) => {
        if (isDragging) {
            let leftPos = event.clientX - offsetX;
            const maxX = container.offsetWidth - object.offsetWidth;

            leftPos = Math.min(maxX, Math.max(0, leftPos));
            object.style.left = leftPos + 'px';
        }
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
    });
});
