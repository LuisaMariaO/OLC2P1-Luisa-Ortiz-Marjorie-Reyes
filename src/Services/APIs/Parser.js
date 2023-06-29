import axios from 'axios'

const instance = axios.create(
    {
        baseURL: 'http://18.116.73.0',
        timeout: 15000,
        headers:{
            'Content-Type':'application/json'
        }
    }
)

export const parse = async(value) =>{
    const { data } = await instance.post("/parse", { code: value })
    return data
}

export const compile = async(value) =>{
    const { data } = await instance.post("/compile", { code: value })
    return data
}

export const symbtable = async() =>{
    const {data} = await instance.get("/symbtable")
    return data
}

export const errortable = async() =>{
    const {data} = await instance.get("/errortable")
    return data
}

export const sintacttree = async() =>{
    const {data} = await instance.get("/sintacttree")
    return data
}