<?php

namespace App\Http; // estructura de carpeta

class Response {
    protected $view; // puede retornar lo que sea, array, json, pdf, vistas, etc...

    public function __construct($view) {

        $this->view = $view; // decimos ejecuta la vista home, contacts, etc
    }

    public function getView() {
        return $this->view;
    }

    public function send() {
        $view = $this->getView();
        // recupero el file specífico
        $content = file_get_contents(viewPath($view)); // viewPath() está en helpers.php

        // se imprimen las vistas dentro de un layout.php
        require viewPath('layout'); // viewPath está en helpers.php
    }
}