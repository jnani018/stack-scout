'use client';
import useSWR from 'swr';
const fetcher = (u:string)=>fetch(u).then(r=>r.json());

export default function Credits() {
  const { data } = useSWR('http://localhost:8000/v1/tools?has_credit=true', fetcher);
  return (
    <main>
      <h1>Credits & Free tiers</h1>
      <ul>
        {data?.items?.map((t:any)=>(<li key={t.id}><b>{t.name}</b> — check eligibility on detail</li>))}
      </ul>
    </main>
  )
}
