<?php

namespace App\Http\Controllers;

class AboutController {
    public function index() { // index es el method descrito en la funcion setMethod() de request
        return view('about'); // la funcion view() se declara en el helpers.php
    }
}