async function login(){
    const email = email.value
    const senha = senha.value

    const res = await fetch("http://localhost:5000/login",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({email,senha})
    })

    const data = await res.json()

    if(res.ok){
        localStorage.setItem("user",JSON.stringify(data))
        window.location="dashboard.html"
    }else{
        alert("Erro no login")
    }
}
