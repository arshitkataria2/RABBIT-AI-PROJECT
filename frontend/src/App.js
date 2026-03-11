import React, { useState } from "react";

export default function App(){

const [file,setFile] = useState(null)
const [email,setEmail] = useState("")
const [message,setMessage] = useState("")

const upload = async(e)=>{
e.preventDefault()

const form = new FormData()
form.append("file",file)
form.append("email",email)

const res = await fetch("http://localhost:8000/upload",{
method:"POST",
body:form
})

const data = await res.json()
setMessage(data.message)
}

return(

<div style={{width:"400px",margin:"100px auto"}}>

<h2>Sales Insight Automator</h2>

<form onSubmit={upload}>

<input
type="file"
accept=".csv,.xlsx"
onChange={(e)=>setFile(e.target.files[0])}
/>

<br/><br/>

<input
type="email"
placeholder="Enter email"
value={email}
onChange={(e)=>setEmail(e.target.value)}
/>

<br/><br/>

<button type="submit">
Generate Summary
</button>

</form>

<p>{message}</p>

</div>

)
}