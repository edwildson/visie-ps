/*
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Array sum odd index - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
*/


(function countStringsWithInitialEqualsAArray(array) {
    if (!Array.isArray(array) || array.length === 0) {
        console.log('Entrada inválida.')
        return 0;
    }

    const result = array.reduce((acc, val, index) => acc += index % 2 !== 0 ? val : 0, 0);
    console.log('result:', result);

    return result;
})([22, 28, 33, 54, 14, 2, 76])