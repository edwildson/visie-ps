<?php 
/*
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Change first letter - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
*/


function changeFirstLetterToAInArray($arr) {
    if (!is_array($arr) || count($arr) === 0) {
        echo 'Entrada inválida.';
        return 0;
    }
    
    $result = array_map(function($string) {
        return 'a' . substr($string, 1);
    }, $arr);
    echo 'result: ';
    print_r($result);
    
    return $result;
}

changeFirstLetterToAInArray(array('front-end', 'back-end', 'database'));
