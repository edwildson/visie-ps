<?php
/*
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Array count strings that initiates with 'a' - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
*/

function countStringsInitialEqualsAArray($array) {
    if (!is_array($array) || count($array) === 0) {
        echo 'Entrada inválida.';
        return 0;
    }
    
    $result = array_reduce($array, function($acc, $val) {
        static $index = 0;
        $acc += ($index % 2 != 0 ? $val : 0);
        $index++;
        return $acc;
    }, 0);

    echo 'result: ', $result, "\n";
    
    return $result;
}

countStringsInitialEqualsAArray(array(22, 28, 33, 54, 14, 2, 76));
