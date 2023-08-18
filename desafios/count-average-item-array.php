<?php 

/*
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Array Average - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
*/

function average($array) {
    $count = count($array);

    return array_sum($array) / $count;
}

function count_average_item_array($array) {
    if (!is_array($array) || count($array) === 0) {
        echo 'Entrada inválida.';
        return 0;
    }

    $avg = average($array);

    $result = array_reduce($array, function($acc, $val) use ($avg) {
        return $acc + ($val > $avg ? 1 : 0);
    }, 0);

    echo 'result: '. $result;

    return $result;
}

count_average_item_array([22, 28, 33, 54, 14, 2, 76]);