'use client';
import { useState } from 'react';

export default function Home() {
  const [prompt, setPrompt] = useState('Build a RAG app under $0 for 30 days');
  const [plan, setPlan] = useState<any>(null);
  async function createPlan() {
    const resp = await fetch('http://localhost:8000/v1/plan', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ prompt, constraints: { no_card: true } })
    });
    const json = await resp.json();
    setPlan(json);
  }
  return (
    <main>
      <h1>Type a goal. Get a plan.</h1>
      <div style={{display:'flex', gap:8}}>
        <input style={{flex:1, padding:8}} value={prompt} onChange={e=>setPrompt(e.target.value)} />
        <button onClick={createPlan} style={{padding:'8px 12px'}}>Plan</button>
      </div>
      {plan && <section style={{marginTop:16}}>
        <h2>Plan</h2>
        <ul>
          {plan.items.map((x:any, i:number)=>(<li key={i}><b>{x.role}</b>: {x.tool} — ${x.cost}/mo</li>))}
        </ul>
        <p>Total: ${plan.totals.monthly}/mo</p>
        <details>
          <summary>Citations</summary>
          <ul>
            {plan.items.flatMap((x:any)=>x.citations).map((c:string, i:number)=>(<li key={i}><a href={c} target="_blank">{c}</a></li>))}
          </ul>
        </details>
      </section>}
    </main>
  )
}
