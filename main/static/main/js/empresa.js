document.addEventListener('DOMContentLoaded', function() {
  const btnLeerMas = document.getElementById('btn-leer-mas');
  const contenedorHistoria = document.getElementById('historia-contenedor');

  btnLeerMas.addEventListener('click', function() {
      // Si el contenedor está colapsado, expandirlo
    if (contenedorHistoria.style.maxHeight === '' || contenedorHistoria.style.maxHeight === '250px') {
      contenedorHistoria.style.maxHeight = contenedorHistoria.scrollHeight + 'px';
      btnLeerMas.textContent = 'Leer menos';
    } else {
      contenedorHistoria.style.maxHeight = '250px';
      btnLeerMas.textContent = 'Leer más';
    }
  });
});
