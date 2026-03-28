"use client"

import { useState } from "react"
import axios from "axios"

export default function Home() {
  const [text, setText] = useState("")
  const [result, setResult] = useState({ post: "", image_prompt: ""  })

  const generate = async () => {
    const res = await axios.post("http://localhost:8000/generate", {
      text: text,
    })
    setResult(res.data)
  }

  return (
    <div style={{ padding: 40 }}>
      <h1>OG Boost 🚀</h1>

      <textarea
        rows={5}
        style={{ width: "100%" }}
        onChange={(e) => setText(e.target.value)}
      />

      <button onClick={generate}>Générer</button>

      {result && (
        <>
          <h2>Post :</h2>
          <p>{result.post}</p>

          <h2>Image prompt :</h2>
          <p>{result.image_prompt}</p>
        </>
      )}
    </div>
  )
}
