export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{fontFamily:'Inter, system-ui', maxWidth: 1000, margin: '24px auto', padding: '0 16px'}}>
        <header style={{display:'flex', justifyContent:'space-between', marginBottom: 16}}>
          <a href="/">StackScout.AI</a>
          <nav style={{display:'flex', gap:12}}>
            <a href="/tools">Tools</a>
            <a href="/credits">Credits</a>
            <a href="/admin">Admin</a>
          </nav>
        </header>
        {children}
      </body>
    </html>
  )
}
