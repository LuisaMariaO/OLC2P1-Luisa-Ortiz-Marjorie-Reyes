import axios from 'axios'

const instance = axios.create(
    {
        baseURL: 'http://localhost:5000',
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