<?php

namespace App\Http\Controllers;

class HomeController {
    public function index() { // index es el method descrito en la funcion setMethod() de request
        return view('home');
    }
}