<?php
// con el helper puedo reutilizar funciones para las vistas y los controladores

use App\Http\Response; // Para poder usar solo Response y no \App\Http\Response($view)

if (! function_exists('viewPath')) {
    function viewPath($view) {
        return __DIR__ . "/../views/$view.php"; // recupero una vista
    }
}

if (! function_exists('view')) {
    function view($view) {
        return new Response($view);
    }
}