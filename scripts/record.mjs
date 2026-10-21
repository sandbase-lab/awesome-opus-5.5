#!/usr/bin/env node
// Record a generated HTML page to MP4, the way most videos in this list were made.
//
//   npm i -D playwright@1.56.1 && npx playwright install chromium
//   (or skip the download and use an installed Google Chrome: RECORD_CHANNEL=chrome)
//   node scripts/record.mjs opus.html out.mp4 [seconds=10] [width=1280] [height=720]
//
// Needs ffmpeg on PATH for the final WebM -> MP4 step.
import { chromium } from 'playwright'
import { execFileSync } from 'node:child_process'
import { mkdtempSync, readdirSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join, resolve } from 'node:path'
import { pathToFileURL } from 'node:url'

const [input, output = 'out.mp4', seconds = '10', width = '1280', height = '720'] = process.argv.slice(2)
if (!input) {
  console.error('usage: node scripts/record.mjs <page.html> [out.mp4] [seconds] [width] [height]')
  process.exit(1)
}
const size = { width: Number(width), height: Number(height) }
const dir = mkdtempSync(join(tmpdir(), 'rec-'))
// WebGL in headless Chromium needs a GPU-less backend; SwiftShader is bundled.
const browser = await chromium.launch({ channel: process.env.RECORD_CHANNEL || undefined, args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] })
try {
  const context = await browser.newContext({ viewport: size, recordVideo: { dir, size } })
  const page = await context.newPage()
  page.on('pageerror', (e) => console.error('page error:', e.message))
  await page.goto(pathToFileURL(resolve(input)).href, { waitUntil: 'load' })
  await page.waitForTimeout(Number(seconds) * 1000)
  await context.close() // flushes the recording
  const webm = join(dir, readdirSync(dir).find((f) => f.endsWith('.webm')))
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-i', webm, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', output], { stdio: 'inherit' })
  console.log(`Saved ${output}`)
} finally {
  await browser.close()
  rmSync(dir, { recursive: true, force: true })
}
