<?php 

//carga todo lo necesario con require, en este caso todo lo que está registrado en composer.json
require __DIR__ . '/../vendor/autoload.php';

// declaro una variable con $
$request = new App\Http\Request; // la ruta al archivo Request.php
$request->send(); // ejecuta el método de la clase Request