'use client';
import useSWR from 'swr';
const fetcher = (u:string)=>fetch(u).then(r=>r.json());

export default function Admin() {
  const { data } = useSWR('http://localhost:8000/v1/evidence', fetcher);
  return (
    <main>
      <h1>Admin Evidence</h1>
      <ul>
        {data?.items?.map((e:any, i:number)=>(<li key={i}>
          <details><summary>{e.tool_id}</summary>
            <ul>
              {e.sources.map((s:any,j:number)=>(<li key={j}><a href={s.url} target="_blank">{s.url}</a></li>))}
            </ul>
          </details>
        </li>))}
      </ul>
    </main>
  )
}
