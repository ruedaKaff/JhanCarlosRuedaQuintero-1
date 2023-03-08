let table = [{
    Traditional: "90-100",
    "14-Point Range": "12-14",
    Letter: "A",
    SBG_Rating: 4,
    Proficiency_Level_With_Standard: "Exceeds proficiency"

},
{
    Traditional: "80-89",
    "14-Point Range": "9-11",
    Letter: "B",
    SBG_Rating: 3,
    Proficiency_Level_With_Standard: "Demonstrates proficiency"

},
{
    Traditional: "70-79",
    "14-Point Range": "6-8",
    Letter: "C",
    SBG_Rating: 2,
    Proficiency_Level_With_Standard: "Approaches proficiency"

},
{
    Traditional: "60-69",
    "14-Point Range": "3-5",
    Letter: "D",
    SBG_Rating: 1,
    Proficiency_Level_With_Standard: "Falls well below proficiency"

},
{
    Traditional: "<60",
    "14-Point Range": "1-2",
    Letter: "E",
    SBG_Rating: 0,
    Proficiency_Level_With_Standard: "Lacks all proficiency"

},
{
    Traditional: "0",
    "14-Point Range": "0",
    Letter: "Z",
    SBG_Rating: 0,
    Proficiency_Level_With_Standard: "No attempt made"

}
]
console.table(table);

let index = 0;

let opt = prompt(`>>BIENVENIDO<<
Escoja el formato de la nota a ingresar:
1.Traditional
2.14-point range
3.Letter`)
console.log(opt);
switch (opt) {
    case '1':
        let grade = prompt("Ingresa una nota de 0 a 100.");
        traditional(grade);
        
        break;
    case '2':
        console.log("14-point range");
        break;
    case '3':
        console.log("Letter");
        break;

    default:
        console.log("Opcion invalida");
        break;
}


function traditional(nota) {

    if (nota >= 0 && nota <= 100) {
        nota == 100
            ? alert("Nota mas alta")
            : alert("No es el ganador")

        if (nota >= 90 && nota <= 100) {
            index = 0;
            let equality = gradeSBG(index,nota);
            console.table(equality);
            alert(equality.Recomendacion.toUpperCase());
        }
        if (nota >= 80 && nota <= 89) {
            index = 1;
            let equality = gradeSBG(index,nota);
            console.table(equality);
            alert(equality.Recomendacion.toUpperCase());
        }
        if (nota >= 70 && nota <= 79) {
            index = 2;
            let equality = gradeSBG(index,nota);
            console.table(equality);
            alert(equality.Recomendacion.toUpperCase());
        }
        if (nota >= 60 && nota <= 69) {
            index = 3;
            let equality = gradeSBG(index,nota);
            console.table(equality);
            alert(equality.Recomendacion.toUpperCase());
        }
        if (nota < 60) {
            index = 4;
            let equality = gradeSBG(index,nota);
            console.table(equality);
            alert(equality.Recomendacion.toUpperCase());
        }
        if (nota == 0) {
            index = 5;
            let equality = gradeSBG(index,nota);
            console.table(equality);
            alert(equality.Recomendacion.toUpperCase());
        }


    }
    else {
        alert("Ingreso un valor fuera del rango")
    }
}

function gradeSBG(index,nota) {
    
    return {
        Calificacion : nota,
        Equivalente_SBG: table[index].SBG_Rating,
        Recomendacion : table[index].Proficiency_Level_With_Standard
    }
    
}
