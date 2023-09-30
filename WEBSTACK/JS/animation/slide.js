$(document).ready(function(){
    let isDragging = false;
    let offsetX = 0;
    let groups = document.getElementById(DIV TO GET VISIBLE)

    const object = document.getElementById(OBJECT TO MOVE);
    const container = document.getElementById(MOVING AREA);

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
            if (leftPos === maxX) {
                groups.style.visibility = 'visible'
            }else if (leftPos === 0) {
                groups.style.visibility = 'hidden'
            }
        }
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
    });
});

