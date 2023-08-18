/*
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Array count strings that initiates with 'a' - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
*/


(function countStringsWithInitialEqualsAArray(array) {
    if (!Array.isArray(array) || array.length === 0) {
        console.log('Entrada inválida.')
        return 0;
    }

    const result = array.reduce((acc, val) => acc += val.startsWith('a') ? 1 : 0, 0);
    console.log('result:', result);

    return result;
})(['front-end', 'angular', 'back-end', 'database', 'async'])