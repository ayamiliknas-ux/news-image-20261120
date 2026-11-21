// Copy the pre-rendered news image to the output directory.
import { copyFileSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const out = process.env.MAKEFUN_OUTPUT_DIR || "out";
mkdirSync(out, { recursive: true });
const here = dirname(fileURLToPath(import.meta.url));
const src = join(process.env.MAKEFUN_BOT_DIR || here, "entry.png");
try {
  copyFileSync(src, join(out, "entry.png"));
} catch {
  copyFileSync(join(here, "entry.png"), join(out, "entry.png"));
}
console.log("wrote", join(out, "entry.png"));
