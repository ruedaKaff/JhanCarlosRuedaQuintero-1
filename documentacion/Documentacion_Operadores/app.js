/* DOCUMENTACION COMPARADORES */


function Igualdad(){
/* El operador de igualdad(==) se utiliza para comparar dos valores y devuelve "verdadero" si son iguales, "falso" si son diferentes.Este operador no compara los tipos de datos, por lo que puede haber conversiones de tipos implícitas.
    Ejemplo: */

let num1 = 10;
let num2 = "10";
console.log(num1 == num2); // Output: true
}

function igualdadEstricta() {
/* El operador de igualdad estricta(===) se utiliza para comparar dos valores y devuelve "verdadero" si son iguales y del mismo tipo, "falso" si son diferentes.
    Ejemplo:
 */

let num1 = 10;
let num2 = "10";
console.log(num1 === num2); // Output: false
}

function desigualdad() {
/* El operador de desigualdad(!=) se utiliza para comparar dos valores y devuelve "verdadero" si son diferentes, "falso" si son iguales.Al igual que con el operador de igualdad, este operador no compara los tipos de datos.
    Ejemplo: */


let num1 = 10;
let num2 = "5";
console.log(num1 != num2); // Output: true

}

function desigualdadEstricta() {
/* El operador de desigualdad estricta(!==) se utiliza para comparar dos valores y devuelve "verdadero" si son diferentes y del mismo tipo, "falso" si son iguales.
    Ejemplo: */


let num1 = 10;
let num2 = "10";
console.log(num1 !== num2); // Output: true
}

function mayorQue() {
/* El operador mayor que(>) se utiliza para comparar dos valores y devuelve "verdadero" si el primer valor es mayor que el segundo valor, "falso" en caso contrario.
    Ejemplo:
 */

let num1 = 10;
let num2 = 5;
console.log(num1 > num2); // Output: true
}

function menorQue() {
/* El operador menor que(<) se utiliza para comparar dos valores y devuelve "verdadero" si el primer valor es menor que el segundo valor, "falso" en caso contrario.
    Ejemplo: */


let num1 = 10;
let num2 = 5;
console.log(num1 < num2); // Output: false
}

function mayorIgualque(){
/* El operador mayor o igual que(>=) se utiliza para comparar dos valores y devuelve "verdadero" si el primer valor es mayor o igual que el segundo valor, "falso" en caso contrario.
    Ejemplo: */


let num1 = 10;
let num2 = 5;
console.log(num1 >= num2); // Output: true
}

function menorIgualque(){
/* El operador menor o igual que(<=) se utiliza para comparar dos valores y devuelve "verdadero" si el primer valor es menor o igual que el segundo valor, "falso" en caso contrario.
    Ejemplo: */


let num1 = 10;
let num2 = 5;
console.log(num1 <= num2); // Output: false
}