import {TextField,Button} from '@mui/material'
import {useState} from 'react'

export default function QueryBox({onResult}:any){
 const [q,setQ]=useState('')
 const run=async()=>{
  const r=await fetch('/query',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({prompt:q})})
  onResult(await r.json())
 }
 return (
  <>
   <TextField fullWidth label='Query' value={q} onChange={e=>setQ(e.target.value)}/>
   <Button onClick={run}>Run</Button>
  </>
 )
}