import { Container, Typography, CssBaseline } from '@mui/material'
import QueryBox from './components/QueryBox'
import TopologyGraph from './components/TopologyGraph'
import RawJsonView from './components/RawJsonView'
import { useState } from 'react'
import { queryBackend } from "./api";


export default function App() {
  const [data, setData] = useState<any>(null)

  return (
    <>
      <CssBaseline />
      <Container maxWidth="lg" sx={{ mt: 4 }}>
        <Typography variant="h4" gutterBottom>
          AWS Cloud AI Agent
        </Typography>

        <QueryBox onResult={setData} />

        {data && (
          <>
            <TopologyGraph topology={data.topology} />
            <RawJsonView data={data} />
          </>
        )}
      </Container>
    </>
  )
}
