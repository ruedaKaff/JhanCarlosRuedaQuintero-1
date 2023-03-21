let formSede = document.querySelector("#formSedes");


let campus = {};


/* registro sedes */
formSede.addEventListener
formSede.addEventListener("submit", (e) => {
    e.preventDefault();
    let data = Object.fromEntries(new FormData(e.target));
    
    if (data.sedeNombre in campus){ 
     alert('ESTA SEDE YA HA SIDO CREADA')
    }
    else {
        campus[`${data.sedeNombre}`] = {
            direccion: data.sedeDirection,
            telefono : data.sedeTelefono,
            nombre : data.sedeNombre
        }
    }
    console.log(campus);
    formSede.reset();

    
});