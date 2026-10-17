function calcularPromedio() {
    const nombre = document.getElementById('nombre').value.trim();
    const n1 = parseFloat(document.getElementById('nota1').value);
    const n2 = parseFloat(document.getElementById('nota2').value);
    const n3 = parseFloat(document.getElementById('nota3').value);
    const divResultado = document.getElementById('resultado');

    if (!nombre || isNaN(n1) || isNaN(n2) || isNaN(n3)) {
        alert("Por favor completa todos los campos.");
        return;
    }

    const promedio = ((n1 + n2 + n3) / 3).toFixed(2);
    const aprobo = promedio >= 3.0;

    divResultado.classList.remove('hidden');
    divResultado.className = `resultado ${aprobo ? 'aprobado' : 'reprobado'}`;
    divResultado.innerHTML = `
        <p><strong>Estudiante:</strong> ${nombre}</p>
        <p><strong>Promedio Final:</strong> ${promedio}</p>
        <p><strong>Estado:</strong> ${aprobo ? 'APROBADO 🎉' : 'REPROBADO ❌'}</p>
    `;
}
