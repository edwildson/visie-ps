/*
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Array Average - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
*/

function average(array) {
    let count = array.length;

    return array.reduce((acc, val) => acc += val/count, 0);
}

(function countAverageItemArray(array) {
    if (!Array.isArray(array) || array.length === 0) {
        console.log('Entrada inválida.')
        return 0;
    }

    let avg = average(array);

    const result = array.reduce((acc, val) => acc += val > avg ? 1 : 0, 0);
    console.log('result:', result);

    return result;

    
})([22, 28, 33, 54, 14, 2, 76])