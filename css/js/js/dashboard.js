fetch("http://localhost:5000/dashboard")
.then(res=>res.json())
.then(data=>{
    recursos.innerText = data.recursos
    usuarios.innerText = data.usuarios
})
