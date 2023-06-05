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



function Code(){
    const navigate = useNavigate();
    
    
    const miEditor = useRef();
    const miConsola = useRef();
   
    const [file, setFile] = useState()
    let fileReader

    function handleChange(event) {
      setFile(event.target.files[0])
     
    }

    
    const handleFileRead =(e) =>{
        const content = fileReader.result
        
       
        miEditor.current.editor.setValue(content)
        miEditor.current.editor.clearSelection()
    };
   
    const handleSubmit = (event) =>{
        event.preventDefault()
        fileReader = new FileReader()
        fileReader.onloadend = handleFileRead;
        if (file!=null){ //Para evitar errores 
        fileReader.readAsText(file)
        }

    };
    
    const changeEditor = (valueA) => {
        alert("hola")
    }

    const postParse = (event) =>{
        event.preventDefault();
      //  alert(miEditor.current.editor.getValue())
        Service.parse(miEditor.current.editor.getValue())
        .then(({consola}) => {
            miConsola.current.editor.setValue(consola)
            miConsola.current.editor.clearSelection()
        })
        
        
       // miConsola.current.editor.setValue("Resultado de la ejecución")
        //miConsola.current.editor.clearSelection()
    }
    const clean = () =>{
        miEditor.current.editor.setValue("")
        miConsola.current.editor.setValue("")
    }

    

   

  
    
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
                <a class="nav-link active" aria-current="page" href="" onClick={()=>navigate('/code')}>Análisis</a>
                </li>

                <li class="nav-item">
                <a class="nav-link" aria-current="page" href="" onClick={()=>navigate('/reports')} >Reportes</a>
                </li>

               
                
            </div>
            </div>
        </div>  
            </nav>
      

  
        <form onSubmit={handleSubmit}>
          <input type="file" accept=".ts" onChange={handleChange}  />
          <button type="submit" class="btn btn-primary">Cargar</button>
        </form>

        <br></br>
        <div class="container-fluid">
        <div class="row">
        
        <div class="col" >
        <AceEditor
        setOptions={{ useWorker: false }}
        value=""
        placeholder="//Ingresa tu código aquí! :D"
        ref={miEditor}
        mode="typescript"
        theme="textmate"
        name="UNIQUE_ID_OF_DIV"
        width="100%"
        height="450px"
        fontSize={17}
        editorProps={{ $blockScrolling: true}}
        
         />
        </div>

        <div class="col" >
        <AceEditor
        setOptions={{ useWorker: false }}
        value=""
        ref={miConsola}
        mode="text"
        theme="dracula"
        name="UNIQUE_ID_OF_DIV"
        width="100%"
        height="450px"
        fontSize={17}
        editorProps={{ $blockScrolling: true }}
        readOnly={true}
        showGutter={false}
         />
        </div>
        

        
        

        </div>
        </div>
       
            &nbsp; &nbsp;
            <button type="button" class="btn btn-success" onClick={postParse}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play" viewBox="0 0 16 16">
            <path d="M10.804 8 5 4.633v6.734L10.804 8zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C4.713 12.69 4 12.345 4 11.692V4.308c0-.653.713-.998 1.233-.696l6.363 3.692z"/>
            </svg>
                Ejecutar
            </button>
                &nbsp; &nbsp;
            <button type="button" class="btn btn-secondary" onClick={clean}>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-stars" viewBox="0 0 16 16">
                <path d="M7.657 6.247c.11-.33.576-.33.686 0l.645 1.937a2.89 2.89 0 0 0 1.829 1.828l1.936.645c.33.11.33.576 0 .686l-1.937.645a2.89 2.89 0 0 0-1.828 1.829l-.645 1.936a.361.361 0 0 1-.686 0l-.645-1.937a2.89 2.89 0 0 0-1.828-1.828l-1.937-.645a.361.361 0 0 1 0-.686l1.937-.645a2.89 2.89 0 0 0 1.828-1.828l.645-1.937zM3.794 1.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387A1.734 1.734 0 0 0 4.593 5.69l-.387 1.162a.217.217 0 0 1-.412 0L3.407 5.69A1.734 1.734 0 0 0 2.31 4.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387A1.734 1.734 0 0 0 3.407 2.31l.387-1.162zM10.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732L9.1 2.137a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L10.863.1z"/>
                </svg>
                    Limpiar
            </button>
        
        </>
    );
}

export default Code