import React, { useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import '../App.css'
import Service  from "../Services/Service";

import AceEditor from "react-ace";

import "ace-builds/src-noconflict/mode-typescript";
import "ace-builds/src-noconflict/mode-text";
import "ace-builds/src-noconflict/theme-textmate";
import "ace-builds/src-noconflict/theme-dracula"
import "ace-builds/src-noconflict/ext-language_tools";



function Reports(){
   
    const navigate = useNavigate();
    
    
    return(
        <>
        
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
            <a class="navbar-brand" href="">PyTypeCraft &nbsp;
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="#239B56" class="bi bi-code-square" viewBox="0 0 16 16">
            <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
            <path d="M6.854 4.646a.5.5 0 0 1 0 .708L4.207 8l2.647 2.646a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 0 1 .708 0zm2.292 0a.5.5 0 0 0 0 .708L11.793 8l-2.647 2.646a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708 0z"/>
            </svg>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <li class="nav-item">
                <a class="nav-link" aria-current="page" href='' onClick={()=>navigate('/')}>Inicio</a>
                </li>

                <li class="nav-item">
                <a class="nav-link" aria-current="page" href="" onClick={()=>navigate('/code')}>Análisis</a>
                </li>

                <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="" onClick={()=>navigate('/reports')} >Reportes</a>
                </li>


               
                
            </div>
            </div>
        </div>  
            </nav>
        <br></br>
        <h3 class="text-center">Descarga los reportes disponibles</h3>
        <br></br>
        <div class="container">
           <div class="row text-center">
                <div class="col text-center">
                <button type="button" class="btn btn-success btn-lg">
                <i class="bi bi-table"></i> Tabla de símbolos

                </button>
                </div>

                <div class="col text-center">
                <button type="button" class="btn btn-warning btn-lg">
                <i class="bi bi-diagram-3"></i> Arbol de análisis sintáctico</button>
                </div>

                <div class="col text-center">
                <button type="button" class="btn btn-danger btn-lg">
                <i class="bi bi-x-square"></i> Tabla de errores</button>
                </div>
            </div> 
        </div>
  
       </>
    );
}

export default Reports