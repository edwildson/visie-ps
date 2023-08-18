/*
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Change first letter - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
*/


(function changeFirstLetterToAInArray(array) {
    if (!Array.isArray(array) || array.length === 0) {
        console.log('Entrada inválida.')
        return 0;
    }

    const result = array.map((string) => 'a' + string.slice(1));
    console.log('result:', result);

    return result;
})(['front-end', 'back-end', 'database'])