"""
Mahabharata Quiz - Local Server Runner & AI API Gateway
Serves static website files and provides a secure, server-side gateway to Google Gemini API
without exposing any API keys in client-side frontend JavaScript.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import json
import urllib.request
import urllib.error
import re

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Candidate Gemini models in order of preference
GEMINI_MODELS = ["gemini-2.5-flash", "gemini-1.5-flash", "gemini-2.0-flash"]

def load_env_file():
    """Loads environment variables from .env if present"""
    env_path = os.path.join(DIRECTORY, ".env")
    if os.path.exists(env_path):
        try:
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip().strip('"').strip("'")
                        if k and not os.environ.get(k):
                            os.environ[k] = v
        except Exception as e:
            print(f"[Server] Error reading .env: {e}")

def get_api_key(request_headers=None):
    """Retrieves API key from environment, .env file, or request header"""
    load_env_file()
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key and request_headers:
        key = request_headers.get("X-Gemini-Key") or request_headers.get("x-gemini-key")
    if not key and hasattr(Handler, "session_api_key"):
        key = Handler.session_api_key
    return (key or "").strip()

def save_api_key(api_key):
    """Saves API key to server session and writes to gitignored .env"""
    api_key = (api_key or "").strip()
    Handler.session_api_key = api_key
    os.environ["GEMINI_API_KEY"] = api_key

    env_path = os.path.join(DIRECTORY, ".env")
    try:
        lines = []
        key_found = False
        if os.path.exists(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip().startswith("GEMINI_API_KEY="):
                        lines.append(f"GEMINI_API_KEY={api_key}\n")
                        key_found = True
                    else:
                        lines.append(line)
        if not key_found:
            lines.append(f"GEMINI_API_KEY={api_key}\n")
        with open(env_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
    except Exception as e:
        print(f"[Server] Could not write .env: {e}")

# Detailed prompt instructions for each Age Group
AGE_INSTRUCTIONS = {
    "kids": """
AGE GROUP: Kids (Ages 6–10)
- Language & Vocabulary: Very simple, joyful, and easy-to-read English. Short, clear sentences. No archaic or complex Sanskrit jargon.
- Core Topics: Famous stories and iconic heroes:
  * Arjuna's archery concentration (seeing only the toy bird's eye on the tree)
  * Bhima's tremendous strength, hearty appetite, and love for ladoos / sweets
  * Lord Krishna's childhood, playing the divine flute, butter, and being Arjuna's beloved charioteer
  * Lord Ganesha writing down the epic for Sage Vyasa
  * The five Pandava brothers staying united and loyal to each other
  * Ekalavya's devotion to archery with his clay statue
  * Escaping the wax house of lac (Lakshagriha)
- Tone: Exciting, fun, inspirational, and easy to understand for elementary school children.
""",
    "young_learners": """
AGE GROUP: Young Learners (Ages 11–15)
- Language & Vocabulary: Engaging, story-driven, and clear English suitable for middle-school students.
- Core Topics: Key events, weapons, warrior exploits, and relationships:
  * The game of dice (Chausar) and the condition of 12 years forest exile + 1 year in disguise (Agyatvasa)
  * Disguises in King Virata's court (Arjuna as Brihannala, Bhima as Ballava the cook)
  * Divine astras & weapons: Arjuna's Gandiva bow, Krishna's Sudarshana Chakra, Pashupatastra from Shiva, Indra's Vasavi Shakti to Karna
  * Young heroes: Brave 16-year-old Abhimanyu entering the Chakravyuha
  * Relationships: Kunti raising the Pandavas, Krishna as cousin and guide, Hidimbi and magical Ghatotkacha
  * The 18-day battle of Kurukshetra, sacred conches (Panchajanya, Devadatta)
- Tone: Adventurous, captivating, focused on friendship, valor, and righteousness.
""",
    "students": """
AGE GROUP: Students (Ages 16–20)
- Language & Vocabulary: Formal, structured, and analytical English suitable for high school and university students.
- Core Topics: Strategy, chronology, character motivations, and the Bhagavad Gita:
  * Military formations (Vyuhas): Chakravyuha, Krauncha Vyuha; 11 Kaurava Akshauhinis vs 7 Pandava Akshauhinis
  * The philosophical Yaksha Prashna dialogue on truth, pride, mind, and Dharma
  * The Bhagavad Gita: Arjuna's grief (Arjuna Vishada Yoga), Nishkama Karma (selfless action without attachment), Vishwarupa Darshana, the three Gunas
  * Strategic maneuvers: Krishna's peace mission (Udyoga Parva), Shalya as Karna's demoralizing charioteer, the fall of Drona ("Ashwatthama is dead"), the fall of Jayadratha
  * Ethical debates: Vikarna protesting Draupadi's disrobing, Yuyutsu crossing over for Dharma, Karna's conflict between loyalty to Duryodhana and cosmic justice
- Tone: Thoughtful, intellectual, exploring ethics, statecraft, and deep philosophical concepts.
""",
    "adults": """
AGE GROUP: Adults (Ages 21+)
- Language & Vocabulary: Sophisticated, literary, and deeply nuanced English suitable for scholars and adult readers.
- Core Topics: Deep nuances of Dharma, specific Parvas, complex genealogies, boons, curses, and lesser-known traditions:
  * Specific Parvas: Adi, Sabha, Vana, Udyoga, Bhishma, Drona, Karna, Shalya, Sauptika (night assault), Stri (Gandhari's lamentation), Shanti (Bhishma's Rajadharma/Mokshadharma), Anushasana, Ashvamedhika, Mausala, Mahaprasthanika, Svargarohana
  * The subtleties of Dharma: Apaddharma (conduct permissible in crisis), Dharma-sankata (insoluble moral dilemmas), Rajadharma (kingship ethics), Vidura Niti
  * Lineage and origins: Niyoga tradition, Sage Vyasa, Shantanu and Ganga, Satyavati/Matsyagandha, Kripa and Kripi, the five Upapandavas
  * Curses and boons: Gandhari's 36-year doom upon the Vrishnis, Sage Shringi's curse on Parikshit, Parashurama's amnesia curse on Karna, Amba's rebirth as Shikhandi
  * Lesser-known warriors and episodes: Barbarika (Khatu Shyam), Bhagadatta and the Vaishnavastra, Bhurisravas, Iravan, Jarasandha's wrestling death, Janamejaya's Sarpa Satra
- Tone: Scholarly, profound, philosophical, exploring the human condition and eternal cosmic order.
"""
}

# Detailed prompt instructions for each Difficulty
DIFFICULTY_INSTRUCTIONS = {
    "easy": """
DIFFICULTY LEVEL: Easy
- Direct, factual, unmistakable questions.
- The question should test clear, well-established knowledge.
- One unmistakably correct answer and 3 distinct, plausible, but definitely incorrect options.
- No trick questions or confusing double negatives.
""",
    "medium": """
DIFFICULTY LEVEL: Medium
- Requires connecting events, understanding cause-and-effect, or recalling specific details of episodes.
- Distractors should be plausible characters or places from the epic to test genuine understanding.
""",
    "hard": """
DIFFICULTY LEVEL: Hard
- Detailed, intricate, subtle, or lesser-known information.
- Precise Sanskrit terms, specific Parvas/chapters, conditions of boons or curses, obscure warriors, or deep philosophical nuances.
- Highly plausible distractors that challenge well-read scholars of the epic.
"""
}

# Detailed prompt instructions for Categories
CATEGORY_INSTRUCTIONS = {
    "characters": "Focus specifically on the personalities, titles, genealogies, distinct virtues, vows, and pivotal deeds of characters.",
    "stories": "Focus specifically on key stories, narrative arcs, famous episodes, confrontations, and turning points in the epic.",
    "weapons": "Focus specifically on divine Astras (Brahmashira, Pashupatastra, Vaishnavastra, Narayanastra, Vasavi Shakti), sacred bows (Gandiva, Vijaya, Sharanga, Pinaka), conch shells, maces, and chariots.",
    "places": "Focus specifically on ancient kingdoms, capital cities (Hastinapura, Indraprastha, Dwaraka), sacred forests (Kamyaka, Naimisharanya), battlegrounds (Kurukshetra, Jyotisar), and holy rivers.",
    "relationships": "Focus specifically on familial lineages, parentage, divine origins, teacher-disciple bonds, marriages, sibling bonds, and historic loyalties/rivalries.",
    "values": "Focus specifically on moral philosophy, ethical quandaries, Satya, Dharma, selfless action (Nishkama Karma), Vidura Niti, and the eternal teachings of the Bhagavad Gita.",
    "mixed": "Provide a well-balanced mixture covering various categories (Characters, Stories & Events, Weapons & Astras, Places, Relationships, and Values & Lessons)."
}

def build_gemini_prompt(age_group, category, difficulty, count):
    """Builds a comprehensive, tailored prompt enforcing all requirements."""
    age_guide = AGE_INSTRUCTIONS.get(age_group.lower(), AGE_INSTRUCTIONS["young_learners"])
    diff_guide = DIFFICULTY_INSTRUCTIONS.get(difficulty.lower(), DIFFICULTY_INSTRUCTIONS["medium"])
    cat_guide = CATEGORY_INSTRUCTIONS.get(category.lower(), CATEGORY_INSTRUCTIONS["mixed"])

    prompt = f"""You are a master Vedic scholar and world-class educational curriculum designer specializing in the epic Mahabharata.
Generate exactly {count} unique multiple-choice questions about the Mahabharata strictly tailored to the following criteria:

{age_guide}

{diff_guide}

CATEGORY INSTRUCTION:
{cat_guide}

CRITICAL RULES:
1. Every generated question MUST be completely unique. Do not repeat facts, characters, or questions within the same quiz.
2. Each question MUST have EXACTLY 4 distinct options. All options must be non-empty strings.
3. The "answer" MUST be the 0-indexed integer (0, 1, 2, or 3) indicating which option is correct.
4. "explanation" MUST be 1-2 informative, educational sentences explaining why the answer is correct and providing enriching epic context.
5. "category" must be one of: "characters", "stories", "weapons", "places", "relationships", "values".
6. "difficulty" must be "{difficulty.lower()}".
7. "ageGroup" must be "{age_group.lower()}".

OUTPUT FORMAT:
Return strictly a valid JSON array of objects. Do NOT include markdown code blocks, backticks, or any conversational text before or after the JSON.

SCHEMA:
[
  {{
    "id": "ai_{age_group.lower()}_{difficulty.lower()}_1",
    "question": "Question text here?",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": 0,
    "explanation": "Clear educational explanation here.",
    "category": "{category.lower() if category.lower() != 'mixed' else 'characters'}",
    "difficulty": "{difficulty.lower()}",
    "ageGroup": "{age_group.lower()}"
  }}
]
"""
    return prompt.strip()

def call_gemini_api(prompt, api_key):
    """Calls Gemini API using server-side key, trying preferred models."""
    if not api_key:
        raise ValueError("No Gemini API key provided or configured on server.")

    request_body = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "topP": 0.9,
            "responseMimeType": "application/json"
        }
    }
    body_bytes = json.dumps(request_body).encode("utf-8")

    last_error = None
    for model in GEMINI_MODELS:
        endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={urllib.parse.quote(api_key)}"
        req = urllib.request.Request(
            endpoint,
            data=body_bytes,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                resp_bytes = resp.read()
                data = json.loads(resp_bytes.decode("utf-8"))
                text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                if text:
                    return text
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8", errors="replace")
            print(f"[Server] Gemini API model '{model}' HTTP Error {e.code}: {error_body}")
            last_error = f"API Error {e.code}: {error_body}"
            # If 404, try next model; otherwise raise
            if e.code == 404:
                continue
            raise RuntimeError(last_error)
        except Exception as e:
            print(f"[Server] Gemini request error with '{model}': {e}")
            last_error = str(e)
            continue

    raise RuntimeError(f"All Gemini models failed. Last error: {last_error}")

def validate_and_clean_questions(raw_text, age_group, category, difficulty, count):
    """Parses, validates, deduplicates, and formats generated questions."""
    clean_text = raw_text.strip()
    # Strip markdown code fences if model enclosed JSON
    clean_text = re.sub(r"^```(?:json)?\s*", "", clean_text, flags=re.IGNORECASE)
    clean_text = re.sub(r"\s*```$", "", clean_text)
    clean_text = clean_text.strip()

    parsed = json.loads(clean_text)
    if not isinstance(parsed, list):
        raise ValueError("AI response did not return a JSON array.")

    validated = []
    seen_questions = set()

    for idx, item in enumerate(parsed):
        q_text = str(item.get("question", "")).strip()
        if not q_text or len(q_text) < 5:
            continue

        norm_q = re.sub(r"[^\w\s]", "", q_text.lower()).strip()
        if norm_q in seen_questions:
            continue
        seen_questions.add(norm_q)

        raw_options = item.get("options")
        if not isinstance(raw_options, list) or len(raw_options) != 4:
            continue

        options = [str(opt).strip() for opt in raw_options]
        if any(not opt for opt in options):
            continue
        if len(set(options)) != 4:
            continue

        raw_ans = item.get("answer")
        if isinstance(raw_ans, int) and 0 <= raw_ans <= 3:
            ans = raw_ans
        else:
            ans = 0

        explanation = str(item.get("explanation", "")).strip()
        if not explanation or len(explanation) < 5:
            explanation = f"Correct answer is {options[ans]}."

        cat = str(item.get("category", category if category != "mixed" else "characters")).lower()
        if cat not in ["characters", "stories", "weapons", "places", "relationships", "values"]:
            cat = category if category != "mixed" else "characters"

        validated.append({
            "id": item.get("id") or f"ai_{age_group}_{difficulty}_{idx + 1}_{os.urandom(2).hex()}",
            "question": q_text,
            "options": options,
            "answer": ans,
            "explanation": explanation,
            "category": cat,
            "difficulty": difficulty.lower(),
            "ageGroup": age_group.lower()
        })

        if len(validated) >= count:
            break

    if not validated:
        raise ValueError("No valid questions could be extracted from AI response.")

    return validated


class Handler(http.server.SimpleHTTPRequestHandler):
    session_api_key = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def send_json(self, status_code, payload):
        """Helper to send JSON response with proper headers."""
        response_bytes = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response_bytes)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Gemini-Key")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()
        self.wfile.write(response_bytes)

    def do_OPTIONS(self):
        """Handle preflight CORS requests."""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Gemini-Key")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()

    def do_GET(self):
        """Handle API status or serve static files."""
        if self.path == "/api/ai-status":
            key = get_api_key(self.headers)
            self.send_json(200, {
                "configured": bool(key and len(key) > 5),
                "model": GEMINI_MODELS[0]
            })
            return

        # Fallback to standard static file serving
        super().do_GET()

    def do_POST(self):
        """Handle API requests: key management and AI question generation."""
        if self.path == "/api/set-key":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(body) if body else {}
                key = data.get("apiKey", "")
                save_api_key(key)
                self.send_json(200, {
                    "success": True,
                    "configured": bool(key and len(key) > 5),
                    "message": "API key successfully saved to server." if key else "API key removed."
                })
            except Exception as e:
                self.send_json(400, {"success": False, "error": str(e)})
            return

        if self.path == "/api/generate-questions":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                params = json.loads(body) if body else {}
            except Exception:
                params = {}

            age_group = str(params.get("ageGroup", "young_learners")).lower()
            category = str(params.get("category", "mixed")).lower()
            difficulty = str(params.get("difficulty", "medium")).lower()
            try:
                question_count = int(params.get("questionCount", 10))
            except (ValueError, TypeError):
                question_count = 10

            # Get API key from env, .env, or request header
            key = params.get("apiKey") or get_api_key(self.headers)

            if not key:
                self.send_json(400, {
                    "success": False,
                    "error": "No Gemini API key configured. Please set GEMINI_API_KEY in .env or via AI Settings.",
                    "fallback": True
                })
                return

            try:
                print(f"[Server] Generating AI Quiz: {age_group} | {category} | {difficulty} | {question_count} questions...")
                prompt = build_gemini_prompt(age_group, category, difficulty, question_count)
                raw_response = call_gemini_api(prompt, key)
                questions = validate_and_clean_questions(raw_response, age_group, category, difficulty, question_count)
                print(f"[Server] Successfully generated {len(questions)} verified questions!")

                self.send_json(200, {
                    "success": True,
                    "questions": questions,
                    "count": len(questions),
                    "isAI": True
                })
            except Exception as e:
                print(f"[Server] AI Generation failed: {e}")
                self.send_json(500, {
                    "success": False,
                    "error": str(e),
                    "fallback": True
                })
            return

        self.send_json(404, {"error": "Endpoint not found"})


def run():
    load_env_file()
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"=====================================================")
        print(f" Mahabharata Quiz Educational Web Application")
        print(f" Running at: {url}")
        key = get_api_key()
        if key:
            print(f" AI Mode Status: Ready (Gemini API Key detected)")
        else:
            print(f" AI Mode Status: Waiting for key (set GEMINI_API_KEY in .env)")
        print(f" Press Ctrl+C to stop the server.")
        print(f"=====================================================")

        webbrowser.open(url)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server. Namaste!")
            httpd.server_close()
            sys.exit(0)

if __name__ == "__main__":
    run()
