<?php

namespace App\Http; // estructura de carpeta

// declaro la clase
class Request
{
    protected $segments = []; // almaceno las rutas
    protected $controller; // controlador que requiere el usuario
    protected $method; // con qué metodo se responderá

    // constructor de clase
    public function __construct() 
    {
        // $_SERVER es una variable global, 'REQUEST_URI' devuelve el URI
        $this->segments = explode('/', $_SERVER['REQUEST_URI']); // explode es tipo split, convirte el string en un array
        
        // var_dump() arroja información sobre una variable
        // var_dump($this->segments);
        $this->setController();
        $this->setMethod();
    }

    /**** Configuration */

    public function setController() {
        // si el segmento está vacío, redirigir al home
        $this->controller = empty($this->segments[1]) ? 'home' : $this->segments[1];
    }

    public function setMethod() {
        // si el segmento está vacío, redirigir al index
        $this->method = empty($this->segments[2]) ? 'index' : $this->segments[2];
    }

    public function getController() {
        // home, HomeController -> el standar para un controller: NameController
        // contact, ContactController, about, AboutController, etc
        $controller = ucfirst($this->controller); // la primer letra a mayúscula

        // accedo a la carpeta del controller
        return "App\Http\Controllers\\{$controller}Controller";
    }

    public function getMethod() {
        // devuelvo el método que asigné
        return $this->method;
    }

    /**** Action */
    public function send() {
        $controller = $this->getController();
        $method = $this->getMethod();

        
        // NOTA: send() solo debe ejecutarse si $response es una instancia de Response.php, caso contrario, arrojaría un error
        try {
            // ejecutar un controller con un método configurado
            $response = call_user_func([new $controller, $method]);

            if ($response instanceof Response) {
                $response->send();
            } else {
                throw new \Exception("Error Processing Request");
            }
        } catch (\Throwable $e) {
            echo "Details {$e->getMessage()}";
        }
    }
}