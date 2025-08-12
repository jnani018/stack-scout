'use client';
import useSWR from 'swr';
const fetcher = (u:string)=>fetch(u).then(r=>r.json());

export default function Tools() {
  const { data } = useSWR('http://localhost:8000/v1/tools', fetcher);
  return (
    <main>
      <h1>Tools</h1>
      <ul>
        {data?.items?.map((t:any)=>(<li key={t.id}><b>{t.name}</b> — {t.category}</li>))}
      </ul>
    </main>
  )
}
