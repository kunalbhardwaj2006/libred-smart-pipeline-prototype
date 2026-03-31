// 🚀 TypeScript Async Batch Processing Prototype
// Demonstrates how LibrEd pipeline ideas can translate to Node.js / TS

type QuestionResult = {
  question: string
  result: string
  processedAt: number
}

// 🔹 Simulate LLM processing
async function processQuestion(question: string): Promise<QuestionResult> {
  await new Promise((resolve) => setTimeout(resolve, 200)) // simulate delay

  return {
    question,
    result: "classified",
    processedAt: Date.now(),
  }
}

// 🔹 Process batch in parallel
async function processBatch(batch: string[]): Promise<QuestionResult[]> {
  return Promise.all(batch.map((q) => processQuestion(q)))
}

// 🔹 Main async pipeline
async function runPipeline() {
  console.log("🚀 Running TypeScript Async Pipeline...\n")

  const questions = [
    "What is OS?",
    "Define DBMS",
    "Explain CPU scheduling",
    "What is normalization?",
    "Define deadlock",
  ]

  const batchSize = 2
  const batches: string[][] = []

  // Create batches
  for (let i = 0; i < questions.length; i += batchSize) {
    batches.push(questions.slice(i, i + batchSize))
  }

  console.log(`📦 Total batches: ${batches.length}`)

  const start = Date.now()

  // Run batches in parallel
  const results = await Promise.all(
    batches.map((batch, index) => {
      console.log(`⚡ Processing batch ${index + 1}`)
      return processBatch(batch)
    })
  )

  const finalResults = results.flat()

  const end = Date.now()

  console.log("\n✅ Processing complete")
  console.log(`⏱ Total time: ${end - start} ms`)
  console.log(`📊 Total results: ${finalResults.length}`)

  console.log("\n📌 Sample Output:")
  console.log(finalResults.slice(0, 2))
}

// ▶️ Run
runPipeline()
