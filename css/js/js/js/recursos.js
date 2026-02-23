async function carregar(){
    const res = await fetch("http://localhost:5000/recursos")
    const dados = await res.json()

    lista.innerHTML=""

    dados.forEach(r=>{
        lista.innerHTML += `
        <li>${r.nome}
        <button onclick="deletar(${r.id})">X</button>
        </li>`
    })
}

async function cadastrar(){
    await fetch("http://localhost:5000/recursos",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({
            nome:nome.value,
            tipo:tipo.value,
            status:status.value
        })
    })
    carregar()
}

async function deletar(id){
    await fetch("http://localhost:5000/recursos/"+id,{
        method:"DELETE"
    })
    carregar()
}

carregar()
