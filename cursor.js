(() => {
  const cursor = document.createElement('div');
  cursor.id = 'humanCursor';
  cursor.style.width = '15px';
  cursor.style.height = '15px';
  cursor.style.borderRadius = '50%';
  cursor.style.position = 'fixed';
  cursor.style.background = 'black';
  cursor.style.zIndex = 2147483647;
  cursor.style.pointerEvents = 'none';
  document.documentElement.appendChild(cursor);
  document.addEventListener('mousemove', e => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';
  });
})();
