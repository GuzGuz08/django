


(function () {

    const btnEliminacion = document.querySelectorAll(".btnElimiacion");
    
    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro quieres eliminar este cargo?')
            if (!confirmacion) {
                e.preventDefault();
                
            }
        })

    })
}) 
()
            
    
