<?php

namespace App\Http\Controllers;

class ContactController {
    public function index() { // index es el method descrito en la funcion setMethod() de request
        return view('contact');
    }
}