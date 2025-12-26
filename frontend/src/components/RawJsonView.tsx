export default function RawJsonView({data}:any){
 return <pre>{JSON.stringify(data,null,2)}</pre>
}