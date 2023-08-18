/*
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Greeting - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
*/

function removeSpaces(string) {
    return string.trim();
}

function changeCommaToExclamation(string) {
    return string.replace(',', '!');
}

function greeting(string) {
    const hora = new Date().getHours();
    let greet = '';

    if (hora >= 0 && hora < 12) {
        greet = "Bom dia,";
    } else if (hora >= 12 && hora < 18) {
        greet = "Boa tarde,";
    } else {
        greet = "Boa noite,";
    }

    return string.replace(/olá|Olá/g, greet);
}

(function changeFirstLetterToAInArray(string) {
    if (!(typeof string === 'string' || string instanceof String)) {
        console.log('Entrada inválida.')
        return 0;
    }

    console.log('String antes: ', string)

    string = removeSpaces(string);
    string = changeCommaToExclamation(string);

    string = greeting(string);

    console.log('result:', string);

    return string;
})( ' Olá usuário, bem-vindo ao sistema  ')