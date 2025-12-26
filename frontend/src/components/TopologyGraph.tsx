import {useEffect,useRef} from 'react'
import {Network} from 'vis-network'
export default function TopologyGraph({topology}:any){
 const ref=useRef<HTMLDivElement>(null)
 useEffect(()=>{
  if(ref.current){
    new Network(ref.current,{nodes:topology.nodes,edges:topology.edges})
  }
 },[topology])
 return <div ref={ref} style={{height:400}}/>
}