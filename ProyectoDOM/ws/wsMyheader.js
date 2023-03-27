/* export default {
    function saludar()
    {
        return hola mundo
    }
} */

self.addEventListener("message", (e)=>{
    console.log(e.data);
    postMessage({mensaje : `el mensaje  '${e.data.mensaje}' obtenido `})
})