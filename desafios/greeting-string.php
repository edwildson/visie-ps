<?php 
/*
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Greeting - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
*/

function removeSpaces($s) {
    return trim($s);
}

function changeCommaToExclamation($s) {
    return str_replace(',', '!', $s);
}

function greeting($s) {
    $hora = date('H');
    $greet = '';

    if ($hora >= 0 && $hora < 12) {
        $greet = "Bom dia,";
    } elseif ($hora >= 12 && $hora < 18) {
        $greet = "Boa tarde,";
    } else {
        $greet = "Boa noite,";
    }

    return preg_replace('/olá|Olá/', $greet, $s);
}

function changeFirstLetterToAInString($string) {
    if (!is_string($string)) {
        echo 'Entrada inválida.';
        return 0;
    }

    echo 'String antes: ', $string, "\n";

    $string = removeSpaces($string);
    $string = changeCommaToExclamation($string);
    $string = greeting($string);

    echo 'result:', $string, "\n";

    return $string;
}

changeFirstLetterToAInString(' Olá usuário, bem-vindo ao sistema  ');
