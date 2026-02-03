import os, json
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai


BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "out"
RESULTS_DIR = BASE_DIR / "results"


EVIDENCE_FILES = [
    OUT_DIR / "analysis_kaspi_fy2024_fs.txt",
    OUT_DIR / "analysis_kaspi_20f_2024.txt",
]


EXISTING_RESULT_FILES = [
    RESULTS_DIR / "audit-results.md",
    RESULTS_DIR / "phase_2_jtbd_setup.md",
    RESULTS_DIR / "phase2_results.md",
    RESULTS_DIR / "ROI.md",
]


MODEL_NAME = "gemini-2.5-flash"


MAX_CHARS = 20000


def try_parse_json(text: str):
    text = text.strip()
    try:
        return json.loads(text)
    except:
        pass
    # попытка вырезать первый JSON-объект
    i = text.find("{")
    j = text.rfind("}")
    if i != -1 and j != -1 and j > i:
        return json.loads(text[i:j+1])
    raise ValueError("No valid JSON in response")


def read_text(p: Path) -> str:
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore").strip()


def build_context() -> str:
    chunks = []
    total = 0

    for p in EVIDENCE_FILES:
        t = read_text(p)
        if not t:
            continue

        remaining = MAX_CHARS - total
        if remaining <= 0:
            break

        t = t[:remaining]
        total += len(t)

        chunks.append(f"\n\n===== FILE:{p.as_posix()} =====\n{t}\n")
    
    return "\n".join(chunks).strip()

def gen_file(model, title: str, task: str, context: str) -> str:
    msg = (
        SYSTEM
        + "\n\nIMPORTANT: Follow the STRICT RULES exactly.\n\n"
        + "PROJECT CONTEXT (FILES DUMP):\n" + context + "\n\n"
        + "TASK:\n" + task + "\n\n"
        + "Return ONLY the markdown content for this file. No JSON. No code fences.\n"
    )
    r = model.generate_content(msg, generation_config={"max_output_tokens": 2500, "temperature": 0.2})
    return (r.text or "").strip()


SYSTEM = """You are an audit/report-writing agent for a Cloud Computing for Big Data assignment.
STRICT RULES:
- Use ONLY the provided files as evidence.
- Do NOT invent numbers, percentages, money values, or claims that are not explicitly present in evidence.
- If something is missing, write: "Not found in evidence".
- Every important claim must include a short quoted snippet under an "Evidence:" line.
- Keep quotes short (1-2 sentences).
OUTPUT FORMAT:
Return a single JSON object with keys:
- "audit-results.md"
- "phase2_results.md"
- "ROI.md"
- "phase_2_jtbd_setup.md"
Optionally also:
- "board_memo.md"
Each value is full markdown content for that file.
"""


PROMPT = """Generate/overwrite the final deliverables.

Requirements for each file:

1) audit-results.md
- Executive summary (5-8 bullets)
- 3-6 key risks / bottlenecks (each with Evidence quote)
- 3-6 recommendations (each tied to at least one Evidence quote)
- "What we could not confirm" section (missing evidence)

2) phase_2_jtbd_setup.md
- JTBD (When/I want/So I can)
- Forces (Push/Pull/Anxiety/Habit)
- Context + constraints (from evidence if present; else say Not found)

3) phase2_results.md
- Root causes (at least 4) with Evidence
- 5 Whys (synthetic) BUT:
  - it must be consistent with evidence, no made-up numbers
- Metrics to monitor (no fake numbers, just what to measure)
- Proposed AI Agent (purpose, inputs/outputs, decisions, non-goals)

4) ROI.md
- ROI framing (what value means here)
- Measurement plan (what to measure, data sources)
- Opportunity-cost logic (no fake numbers)
- Risks of optimization (false positives etc.) with Evidence if present

Optionally board_memo.md:
- TO/FROM/DATE/SUBJECT
- 1-page memo style
"""


def main():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("No API key. Put GOOGLE_API_KEY in .env")
        return

    context = build_context()
    if not context:
        print("No context found. Ensure out/analysis_*.txt exists.")
        return

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")

    tasks = {
        "audit-results.md": """Create audit-results.md with:
- Executive summary (5-8 bullets)
- 3-6 key risks / bottlenecks (each with Evidence quote)
- 3-6 recommendations (each tied to at least one Evidence quote)
- "What we could not confirm" section (missing evidence)
""",
        "phase_2_jtbd_setup.md": """Create phase_2_jtbd_setup.md with:
- JTBD (When/I want/So I can)
- Forces (Push/Pull/Anxiety/Habit)
- Context + constraints (from evidence if present; else say Not found)
""",
        "phase2_results.md": """Create phase2_results.md with:
- Root causes (at least 4) with Evidence
- 5 Whys (synthetic) but consistent with evidence
- Metrics to monitor (no numbers, only what to measure)
- Proposed AI Agent (purpose, inputs/outputs, decisions, non-goals)
""",
        "ROI.md": """Create ROI.md with:
- ROI framing (what value means here)
- Measurement plan (what to measure, data sources)
- Opportunity-cost logic (no numbers)
- Risks of optimization with Evidence if present
""",
    }

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    for fname, task in tasks.items():
        text = gen_file(model, fname, task, context)
        (RESULTS_DIR / fname).write_text(text + "\n", encoding="utf-8")

    print("Generated results/: " + ", ".join(tasks.keys()))


# def main():
#     load_dotenv()
#     api_key = os.getenv("GOOGLE_API_KEY")
#     if not api_key:
#         print("No API key. Put GOOGLE_API_KEY in .env")
#         return
    
#     context = build_context()
#     if not context:
#         print("No context found. Ensure out/analysis_*.txt exists.")
#         return

#     genai.configure(api_key=api_key)

#     model = genai.GenerativeModel(model_name=MODEL_NAME)

#     print("AVAILABLE MODELS:")
#     for m in genai.list_models():
#         if "generateContent" in m.supported_generation_methods:
#             print(" -", m.name)


#     msg = (
#         SYSTEM
#         + "\n\nIMPORTANT: Follow the STRICT RULES exactly.\n\n"
#         + "PROJECT CONTEXT (FILES DUMP):\n" + context + "\n\n"
#         + "TASK:\n" + PROMPT + "\n\n"
#         + "Return ONLY valid JSON. No markdown, no code fences, no extra text.\n"
#     )
#     r = model.generate_content(
#         msg,
#         generation_config={"max_output_tokens": 3000, "temperature": 0.2},
#     )
#     text = (r.text or "").strip()

#     try:
#         data = try_parse_json(text)
#     except Exception as e:
#         RESULTS_DIR.mkdir(parents=True, exist_ok=True)
#         (RESULTS_DIR / "_raw_model_output.txt").write_text(text, encoding="utf-8")
#         print("Model did not return valid JSON. Saved raw output to results/_raw_model_output.txt")
#         return
    
#     RESULTS_DIR.mkdir(parents=True, exist_ok=True)
#     for name, content in data.items():
#         if not isinstance(content, str) or not content.strip():
#             continue
#         (RESULTS_DIR / name).write_text(content.strip() + "\n", encoding="utf-8")
#     print("Generate results/: " + ", ".join(sorted(data.keys())))


if __name__ == "__main__":
    main()