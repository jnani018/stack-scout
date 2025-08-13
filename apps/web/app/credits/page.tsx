'use client';
import { useState } from 'react';

export default function Credits() {
  const [email, setEmail] = useState('you@university.edu');
  const [res, setRes] = useState<any>(null);

  async function check() {
    const r = await fetch('http://localhost:8000/v1/credits/check', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ tool_id: 't3', user_claims: { student_email: email.includes('.edu') } })
    });
    setRes(await r.json());
  }

  return (
    <main style={{maxWidth:920, margin:'24px auto', padding:'0 16px'}}>
      <h1>Credits checker</h1>
      <div style={{display:'flex', gap:8}}>
        <input value={email} onChange={e=>setEmail(e.target.value)} style={{flex:1, padding:10, border:'1px solid #ddd', borderRadius:8}} />
        <button onClick={check} style={{padding:'10px 14px', borderRadius:8, border:'1px solid #ddd'}}>Check</button>
      </div>
      {res && <pre style={{marginTop:12, background:'#f6f6f6', padding:12, borderRadius:8}}>{JSON.stringify(res, null, 2)}</pre>}
    </main>
  );
}