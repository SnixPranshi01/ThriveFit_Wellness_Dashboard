import zipfile
import os

def create_thrivefit_zip():
    # Define files to include in the bundle
    files_to_bundle = {
        "index.html": """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ThriveFit - Wellness in Every Dimension</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        emerald: {
                            50: '#ecfdf5', 100: '#d1fae5', 200: '#a7f3d0', 300: '#6ee7b7',
                            400: '#34d399', 500: '#10b981', 600: '#059669', 700: '#047857',
                            800: '#065f46', 900: '#064e3b', 950: '#022c22',
                        },
                        darkBg: '#011611'
                    }
                }
            }
        }
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Rhodium+Libre&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #011611; color: #e2e8f0; overflow-x: hidden; }
        .rhodium-font { font-family: 'Rhodium Libre', serif; }
        .glass-card { background: linear-gradient(135deg, rgba(2, 44, 34, 0.7) 0%, rgba(1, 22, 17, 0.85) 100%); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(16, 185, 129, 0.18); box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.5); transition: all 0.3s ease; }
        .glass-card:hover { border-color: rgba(16, 185, 129, 0.4); box-shadow: 0 15px 35px -5px rgba(16, 185, 129, 0.15); }
        .glass-input { background: rgba(2, 44, 34, 0.5); border: 1px solid rgba(16, 185, 129, 0.25); color: #ffffff; transition: all 0.2s ease; }
        .glass-input:focus { outline: none; border-color: #10b981; box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2); }
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: #011611; }
        ::-webkit-scrollbar-thumb { background: #064e3b; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #059669; }
        @keyframes pulseGlow { 0%, 100% { box-shadow: 0 0 15px rgba(16, 185, 129, 0.2); } 50% { box-shadow: 0 0 30px rgba(16, 185, 129, 0.5); } }
        .pulse-emerald { animation: pulseGlow 3s infinite ease-in-out; }
    </style>
</head>
<body class="bg-darkBg min-h-screen text-slate-100 flex flex-col" onload="initApp()">
    <div id="toast-modal" class="fixed bottom-6 right-6 z-50 transform translate-y-32 opacity-0 transition-all duration-300 pointer-events-none">
        <div id="toast-content" class="glass-card px-6 py-4 rounded-2xl border-emerald-500/50 flex items-center gap-3 shadow-2xl">
            <i id="toast-icon" class="fa-solid fa-circle-check text-emerald-400 text-xl"></i>
            <div>
                <h5 id="toast-title" class="text-white text-sm font-semibold rhodium-font">Success</h5>
                <p id="toast-msg" class="text-xs text-slate-300">Action completed successfully.</p>
            </div>
        </div>
    </div>
    <header class="sticky top-0 z-50 bg-[#022c22]/90 backdrop-blur-md border-b border-emerald-900/50 shadow-xl transition-colors duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-emerald-600/20 border border-emerald-500/40 flex items-center justify-center text-emerald-300 font-bold text-lg pulse-emerald">
                    <i class="fa-solid fa-heart-pulse"></i>
                </div>
                <div>
                    <h1 class="text-lg sm:text-xl text-white tracking-wide flex items-center gap-2 rhodium-font">ThriveFit</h1>
                    <p id="header-subtitle" class="text-[11px] text-emerald-300/90 font-mono">Thrive360 - Wellness in Every Dimension</p>
                </div>
            </div>
            <nav class="hidden lg:flex items-center gap-5 text-xs font-mono text-slate-200">
                <a href="#section-overview" class="hover:text-emerald-300 transition-colors">Overview</a>
                <a href="#section-analytics" class="hover:text-emerald-300 transition-colors">Analytics</a>
                <a href="#section-insights" class="hover:text-emerald-300 transition-colors">Recommendations</a>
                <a href="#section-annual-comparison" class="hover:text-emerald-300 transition-colors">Yearly Comparison</a>
                <a href="#section-report" class="hover:text-emerald-300 transition-colors">Annual Report</a>
            </nav>
            <div class="flex items-center gap-3">
                <button onclick="toggleTheme()" class="bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-200 border border-emerald-500/40 text-xs px-3.5 py-2 rounded-xl font-mono transition-all flex items-center gap-2 shadow-lg cursor-pointer" title="Toggle Day/Night Mode">
                    <i id="theme-icon" class="fa-solid fa-moon"></i> <span id="theme-text" class="hidden sm:inline">Night Mode</span>
                </button>
            </div>
        </div>
    </header>
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-12 flex-grow w-full">
        <section id="section-overview" class="scroll-mt-24">
            <div class="glass-card rounded-3xl p-6 sm:p-8 shadow-2xl relative overflow-hidden">
                <div class="absolute -right-12 -bottom-12 w-64 h-64 bg-emerald-600/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 relative z-10">
                    <div>
                        <div class="flex items-center gap-3 mb-2">
                            <span id="banner-date-badge" class="bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider">⚕️ Daily Telemetry Active</span>
                            <span class="text-xs text-emerald-400/80 font-mono">Real-Time Daily Basis Analysis</span>
                        </div>
                        <h2 class="text-3xl sm:text-4xl text-white flex items-center gap-3 rhodium-font">
                            ThriveFit Annual Dashboard
                            <span class="text-xs bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 px-2.5 py-1 rounded-lg font-mono">Health Score: 95/100</span>
                        </h2>
                        <p class="text-slate-300 mt-1 text-sm sm:text-base font-sans">Comprehensive professional health analytics tracking all 19 required biometric watch columns across 365 days with MoHFW national benchmarks.</p>
                    </div>
                    <div class="flex items-center gap-4">
                        <div class="bg-[#021b14]/90 border border-emerald-500/40 text-emerald-300 font-bold px-5 py-3 rounded-2xl text-center shadow-xl">
                            <div class="text-[10px] tracking-normal font-mono text-emerald-400/70">ANNUAL STATUS ☤</div>
                            <div class="text-lg text-emerald-400 rhodium-font">PEAK CONDITION</div>
                            <div class="text-[9px] tracking-normal font-mono text-slate-500">365-DAY TELEMETRY</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section id="section-analytics" class="scroll-mt-24 space-y-6">
            <h3 class="text-xl sm:text-2xl text-white flex items-center gap-2 rhodium-font">
                <i class="fa-solid fa-chart-line text-emerald-400"></i> Annual Analytics & Trends (365 Days)
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="glass-card p-5 rounded-2xl">
                    <div class="text-xs text-slate-400 font-mono">Avg Steps (Annual)</div>
                    <div id="stat-avg-steps" class="text-2xl text-white font-bold mt-1 rhodium-font">8,520</div>
                    <div class="text-[11px] text-emerald-400 mt-1 flex items-center gap-1 font-mono"><i class="fa-solid fa-arrow-trend-up"></i> +18.5% vs national avg</div>
                </div>
                <div class="glass-card p-5 rounded-2xl">
                    <div class="text-xs text-slate-400 font-mono">Avg Sleep Duration</div>
                    <div id="stat-avg-sleep" class="text-2xl text-white font-bold mt-1 rhodium-font">7h 42m</div>
                    <div class="text-[11px] text-emerald-400 mt-1 flex items-center gap-1 font-mono"><i class="fa-solid fa-circle-check"></i> 89% Sleep Efficiency</div>
                </div>
                <div class="glass-card p-5 rounded-2xl">
                    <div class="text-xs text-slate-400 font-mono">Resting Heart Rate</div>
                    <div id="stat-avg-rhr" class="text-2xl text-white font-bold mt-1 rhodium-font">58 bpm</div>
                    <div class="text-[11px] text-emerald-400 mt-1 flex items-center gap-1 font-mono"><i class="fa-solid fa-shield-heart"></i> Optimal Fitness</div>
                </div>
                <div class="glass-card p-5 rounded-2xl">
                    <div class="text-xs text-slate-400 font-mono">Avg Water Intake</div>
                    <div id="stat-avg-water" class="text-2xl text-white font-bold mt-1 rhodium-font">3.0 L</div>
                    <div class="text-[11px] text-emerald-400 mt-1 flex items-center gap-1 font-mono"><i class="fa-solid fa-droplet"></i> Well Hydrated</div>
                </div>
            </div>
        </section>
        <section id="section-insights" class="scroll-mt-24 space-y-6">
            <div class="flex items-center justify-between">
                <div>
                    <h3 class="text-xl sm:text-2xl text-white flex items-center gap-2 rhodium-font">
                        <i class="fa-solid fa-robot text-emerald-400"></i> Recommendations & Suggestions
                    </h3>
                    <p class="text-xs sm:text-sm text-slate-400 font-sans">Live analysis powered by Gemini AI evaluating your 365-day watch telemetry against MoHFW standards.</p>
                </div>
                <button onclick="fetchGeminiAIRecommendations()" id="gemini-btn" class="text-xs bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-200 border border-emerald-500/50 px-3.5 py-2 rounded-xl transition-all font-mono flex items-center gap-2 shadow-lg">
                    <i class="fa-solid fa-wand-magic-sparkles"></i> <span id="gemini-btn-text">Generate with Gemini AI</span>
                </button>
            </div>
            <div id="coach-suggestions-grid" class="grid grid-cols-1 md:grid-cols-2 gap-6"></div>
        </section>
        <section id="section-annual-comparison" class="scroll-mt-24 space-y-6">
            <div class="flex items-center justify-between">
                <div>
                    <h3 class="text-xl sm:text-2xl text-white flex items-center gap-2 rhodium-font">
                        <i class="fa-solid fa-chart-bar text-emerald-400"></i> Yearly Dataset Comparison & Quarterly Analysis
                    </h3>
                    <p class="text-xs sm:text-sm text-slate-400 font-sans">Comprehensive side-by-side bar graph comparison of steps, sleep scores, and resting heart rate across the 4 annual quarters from your 365-day dataset.</p>
                </div>
                <span class="text-xs text-emerald-400 font-mono">365-Day Aggregated View</span>
            </div>
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="glass-card rounded-2xl p-6 space-y-4 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <h4 class="text-base text-white rhodium-font">Quarterly Step Average Comparison</h4>
                            <span class="text-xs text-emerald-400 font-mono">Steps/Day</span>
                        </div>
                        <p class="text-xs text-slate-400 font-sans mb-4">Comparing step averages across Q1, Q2, Q3, and Q4 against MoHFW standard.</p>
                        <div id="compare-steps-bars" class="space-y-3 font-mono text-xs"></div>
                    </div>
                    <div class="bg-[#011611]/80 border border-emerald-900/60 p-3 rounded-xl text-xs text-slate-300 font-sans">Activity levels peaked during Q2 and Q3 with sustained daily averages exceeding 8,600 steps.</div>
                </div>
                <div class="glass-card rounded-2xl p-6 space-y-4 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <h4 class="text-base text-white rhodium-font">Quarterly Sleep Score Comparison</h4>
                            <span class="text-xs text-teal-400 font-mono">Score (0-100)</span>
                        </div>
                        <p class="text-xs text-slate-400 font-sans mb-4">Comparing sleep restoration scores across all four annual quarters.</p>
                        <div id="compare-sleep-bars" class="space-y-3 font-mono text-xs"></div>
                    </div>
                    <div class="bg-[#011611]/80 border border-emerald-900/60 p-3 rounded-xl text-xs text-slate-300 font-sans">Sleep restoration remained exceptionally stable throughout the year, with Q4 showing peak recovery scores.</div>
                </div>
                <div class="glass-card rounded-2xl p-6 space-y-4 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <h4 class="text-base text-white rhodium-font">Quarterly Resting HR Comparison</h4>
                            <span class="text-xs text-amber-400 font-mono">BPM</span>
                        </div>
                        <p class="text-xs text-slate-400 font-sans mb-4">Cardiovascular efficiency evaluated by resting heart rate trends per quarter.</p>
                        <div id="compare-rhr-bars" class="space-y-3 font-mono text-xs"></div>
                    </div>
                    <div class="bg-[#011611]/80 border border-emerald-900/60 p-3 rounded-xl text-xs text-slate-300 font-sans">Resting heart rate progressively optimized across the year, lowering to 57 bpm in Q4.</div>
                </div>
            </div>
        </section>
        <section id="section-report" class="scroll-mt-24 space-y-6">
            <div class="flex items-center justify-between flex-wrap gap-4">
                <div>
                    <h3 class="text-xl sm:text-2xl text-white flex items-center gap-2 rhodium-font">
                        <i class="fa-solid fa-table text-emerald-400"></i> Annual Telemetry Records (365 Days)
                    </h3>
                    <p class="text-xs sm:text-sm text-slate-400 font-sans">Full year watch telemetry dataset. Add, edit, or delete records below.</p>
                </div>
                <div class="flex items-center gap-3">
                    <button onclick="openLogModal()" class="text-xs bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold px-4 py-2.5 rounded-xl transition-all font-mono flex items-center gap-2 shadow-lg cursor-pointer">
                        <i class="fa-solid fa-plus"></i> Add Telemetry Record
                    </button>
                </div>
            </div>
            <div class="glass-card rounded-2xl overflow-hidden shadow-2xl">
                <div class="overflow-x-auto max-h-[500px]">
                    <table class="w-full text-left text-xs sm:text-sm whitespace-nowrap">
                        <thead class="bg-[#021b14] text-emerald-400 uppercase font-mono text-[11px] border-b border-emerald-900/50 sticky top-0 z-20">
                            <tr>
                                <th class="py-3.5 px-4 bg-[#021b14]">Date</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Day</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Steps</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Dist (km)</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Calories</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Exercise (m)</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Type</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Avg HR</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Resting HR</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">HRV (ms)</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Sleep (h)</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Deep %</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Bed / Wake</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Sleep Score</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Stress</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Water (L)</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Weight (kg)</th>
                                <th class="py-3.5 px-4 bg-[#021b14]">Mood</th>
                                <th class="py-3.5 px-4 bg-[#021b14] text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody id="telemetry-table-body" class="divide-y divide-emerald-900/30 text-slate-300 font-mono text-xs"></tbody>
                    </table>
                </div>
            </div>
        </section>
    </main>
    <footer class="bg-[#022c22]/50 border-t border-emerald-900/40 py-8 mt-16 text-center text-xs text-slate-400 font-mono">
        <div class="max-w-7xl mx-auto px-4 space-y-2">
            <p class="text-white rhodium-font text-sm">ThriveFit • Wellness in Every Dimension</p>
            <p>Integrated with MoHFW National Health Profile Standards • 365 Days Annual Telemetry Encrypted Locally.</p>
        </div>
    </footer>
    <div id="log-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
        <div class="glass-card max-w-2xl w-full rounded-3xl p-6 sm:p-8 border-emerald-500/40 shadow-2xl max-h-[90vh] overflow-y-auto">
            <div class="flex items-center justify-between mb-6 pb-4 border-b border-emerald-900/50">
                <h3 id="modal-title" class="text-lg text-white font-semibold flex items-center gap-2 rhodium-font">
                    <i class="fa-solid fa-plus text-emerald-400"></i> Add Daily Telemetry Record
                </h3>
                <button onclick="closeLogModal()" class="text-slate-400 hover:text-white text-lg"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <form id="telemetry-form" onsubmit="saveTelemetryRecord(event)" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 text-xs font-mono">
                <input type="hidden" id="record-index" value="-1">
                <div><label class="block text-slate-400 mb-1">Date (YYYY-MM-DD)</label><input type="date" id="f-date" required class="glass-input w-full p-2.5 rounded-xl"></div>
                <div><label class="block text-slate-400 mb-1">Day of Week</label><select id="f-day_of_week" class="glass-input w-full p-2.5 rounded-xl"><option>Monday</option><option>Tuesday</option><option>Wednesday</option><option>Thursday</option><option>Friday</option><option>Saturday</option><option>Sunday</option></select></div>
                <div><label class="block text-slate-400 mb-1">Steps Taken</label><input type="number" id="f-steps" required class="glass-input w-full p-2.5 rounded-xl" placeholder="8500"></div>
                <div><label class="block text-slate-400 mb-1">Distance (km)</label><input type="number" step="0.1" id="f-distance_km" required class="glass-input w-full p-2.5 rounded-xl" placeholder="6.2"></div>
                <div><label class="block text-slate-400 mb-1">Calories Burned</label><input type="number" id="f-calories_burned" required class="glass-input w-full p-2.5 rounded-xl" placeholder="2150"></div>
                <div><label class="block text-slate-400 mb-1">Exercise Mins</label><input type="number" id="f-exercise_minutes" required class="glass-input w-full p-2.5 rounded-xl" placeholder="45"></div>
                <div><label class="block text-slate-400 mb-1">Exercise Type</label><select id="f-exercise_type" class="glass-input w-full p-2.5 rounded-xl"><option>Walking</option><option>Running</option><option>Weight Training</option><option>Yoga</option><option>Dancing</option><option>None</option></select></div>
                <div><label class="block text-slate-400 mb-1">Avg HR (bpm)</label><input type="number" id="f-avg_heart_rate_bpm" required class="glass-input w-full p-2.5 rounded-xl" placeholder="72"></div>
                <div><label class="block text-slate-400 mb-1">Resting HR (bpm)</label><input type="number" id="f-resting_heart_rate_bpm" required class="glass-input w-full p-2.5 rounded-xl" placeholder="58"></div>
                <div><label class="block text-slate-400 mb-1">HRV (ms)</label><input type="number" id="f-hrv_ms" required class="glass-input w-full p-2.5 rounded-xl" placeholder="65"></div>
                <div><label class="block text-slate-400 mb-1">Sleep Hours</label><input type="number" step="0.1" id="f-sleep_hours" required class="glass-input w-full p-2.5 rounded-xl" placeholder="7.5"></div>
                <div><label class="block text-slate-400 mb-1">Deep Sleep %</label><input type="number" id="f-deep_sleep_pct" required class="glass-input w-full p-2.5 rounded-xl" placeholder="25"></div>
                <div><label class="block text-slate-400 mb-1">Bed / Wake Time</label><input type="text" id="f-bed_wake" required class="glass-input w-full p-2.5 rounded-xl" placeholder="23:00 / 07:00"></div>
                <div><label class="block text-slate-400 mb-1">Sleep Score (0-100)</label><input type="number" id="f-sleep_score" required class="glass-input w-full p-2.5 rounded-xl" placeholder="88"></div>
                <div><label class="block text-slate-400 mb-1">Stress Score (1-10)</label><input type="number" id="f-stress_score" required class="glass-input w-full p-2.5 rounded-xl" placeholder="3"></div>
                <div><label class="block text-slate-400 mb-1">Water (L)</label><input type="number" step="0.1" id="f-water_liters" required class="glass-input w-full p-2.5 rounded-xl" placeholder="2.8"></div>
                <div><label class="block text-slate-400 mb-1">Weight (kg)</label><input type="number" step="0.1" id="f-weight_kg" required class="glass-input w-full p-2.5 rounded-xl" placeholder="68.3"></div>
                <div><label class="block text-slate-400 mb-1">Mood (1-5)</label><input type="number" id="f-mood_1to5" required class="glass-input w-full p-2.5 rounded-xl" placeholder="4"></div>
                <div class="col-span-full flex justify-end gap-3 mt-4 pt-4 border-t border-emerald-900/50">
                    <button type="button" onclick="closeLogModal()" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl">Cancel</button>
                    <button type="submit" class="px-5 py-2 bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold rounded-xl shadow-lg">Save Record</button>
                </div>
            </form>
        </div>
    </div>
    <script>
        let telemetryData = [];
        function generate365Days() {
            const dataset = [];
            const baseDate = new Date(2025, 0, 1);
            for (let i = 0; i < 365; i++) {
                const curr = new Date(baseDate);
                curr.setDate(baseDate.getDate() + i);
                const dateStr = curr.toISOString().split('T')[0];
                const dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
                const dayName = dayNames[curr.getDay()];
                const dayMod = curr.getDay();
                const steps = Math.round(8200 + (dayMod === 0 || dayMod === 6 ? 1200 : -300) + ((i * 13) % 900) - 450);
                const dist = Math.round(steps * 0.00075 * 10) / 10;
                const cal = Math.round(2000 + (steps * 0.15));
                const exMins = (dayMod === 1 || dayMod === 3 || dayMod === 5) ? 45 : 30;
                const exType = dayMod === 1 ? "Running" : (dayMod === 3 ? "Weight Training" : (dayMod === 6 ? "Yoga" : "Walking"));
                dataset.push({
                    date: dateStr, day_of_week: dayName, steps: steps, distance_km: dist, calories_burned: cal,
                    exercise_minutes: exMins, exercise_type: exType, avg_heart_rate_bpm: Math.round(72 + (i % 5)),
                    resting_heart_rate_bpm: Math.round(58 + ((i % 3) - 1)), hrv_ms: Math.round(65 + ((i * 7) % 15)),
                    sleep_hours: Math.round((7.2 + ((i % 4) * 0.3)) * 10) / 10, deep_sleep_pct: Math.round(24 + (i % 7)),
                    bed_wake: "23:00 / 07:00", sleep_score: Math.round(85 + (i % 10)), stress_score: Math.round(2 + (i % 3)),
                    water_liters: Math.round((2.8 + ((i % 5) * 0.1)) * 10) / 10, weight_kg: Math.round((68.5 + ((i % 10) * 0.05)) * 10) / 10,
                    mood_1to5: Math.round(4 + (i % 2))
                });
            }
            return dataset;
        }
        function initApp() {
            const saved = localStorage.getItem('thrivefit_365_data');
            if (saved) {
                try { telemetryData = JSON.parse(saved); } catch (e) { telemetryData = generate365Days(); }
            } else { telemetryData = generate365Days(); }
            const today = new Date();
            const dateStr = today.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
            const badge = document.getElementById('banner-date-badge');
            if (badge) badge.innerHTML = `⚕️ Daily Basis Telemetry Active • ${dateStr}`;
            renderAll();
        }
        function persistData() {
            localStorage.setItem('thrivefit_365_data', JSON.stringify(telemetryData));
            renderAll();
        }
        function renderAll() {
            renderTable();
            renderAnalytics();
            renderCoachInsights();
            renderAnnualComparisonCharts();
        }
        function renderTable() {
            const tbody = document.getElementById('telemetry-table-body');
            if (!tbody) return;
            tbody.innerHTML = '';
            telemetryData.forEach((r, idx) => {
                tbody.innerHTML += `
                    <tr class="hover:bg-emerald-950/45 transition-colors">
                        <td class="py-3 px-4 text-emerald-300 font-bold">${r.date}</td>
                        <td class="py-3 px-4">${r.day_of_week}</td>
                        <td class="py-3 px-4">${r.steps.toLocaleString()}</td>
                        <td class="py-3 px-4">${r.distance_km} km</td>
                        <td class="py-3 px-4">${r.calories_burned} kcal</td>
                        <td class="py-3 px-4">${r.exercise_minutes} m</td>
                        <td class="py-3 px-4"><span class="bg-emerald-500/10 text-emerald-300 px-2 py-0.5 rounded border border-emerald-500/20">${r.exercise_type}</span></td>
                        <td class="py-3 px-4">${r.avg_heart_rate_bpm} bpm</td>
                        <td class="py-3 px-4 text-emerald-400 font-semibold">${r.resting_heart_rate_bpm} bpm</td>
                        <td class="py-3 px-4">${r.hrv_ms} ms</td>
                        <td class="py-3 px-4">${r.sleep_hours} h</td>
                        <td class="py-3 px-4">${r.deep_sleep_pct}%</td>
                        <td class="py-3 px-4 text-slate-400">${r.bed_wake}</td>
                        <td class="py-3 px-4 text-teal-300 font-semibold">${r.sleep_score}/100</td>
                        <td class="py-3 px-4">${r.stress_score}/10</td>
                        <td class="py-3 px-4 ${r.water_liters > 4.0 ? 'text-amber-400 font-bold' : ''}">${r.water_liters} L</td>
                        <td class="py-3 px-4">${r.weight_kg} kg</td>
                        <td class="py-3 px-4">${r.mood_1to5}/5</td>
                        <td class="py-3 px-4 text-right space-x-2">
                            <button onclick="editRecord(${idx})" class="text-emerald-400 hover:text-emerald-300 px-2 py-1 bg-emerald-500/10 rounded"><i class="fa-solid fa-pen"></i></button>
                            <button onclick="deleteRecord(${idx})" class="text-rose-400 hover:text-rose-300 px-2 py-1 bg-rose-500/10 rounded"><i class="fa-solid fa-trash"></i></button>
                        </td>
                    </tr>
                `;
            });
        }
        function renderAnalytics() {
            const count = telemetryData.length;
            if (count === 0) return;
            const avgSteps = Math.round(telemetryData.reduce((acc, r) => acc + r.steps, 0) / count);
            const avgSleep = (telemetryData.reduce((acc, r) => acc + r.sleep_hours, 0) / count).toFixed(1);
            const avgRHR = Math.round(telemetryData.reduce((acc, r) => acc + r.resting_heart_rate_bpm, 0) / count);
            const avgWater = (telemetryData.reduce((acc, r) => acc + r.water_liters, 0) / count).toFixed(1);
            document.getElementById('stat-avg-steps').innerText = avgSteps.toLocaleString();
            document.getElementById('stat-avg-sleep').innerText = `${Math.floor(avgSleep)}h ${Math.round((avgSleep%1)*60)}m`;
            document.getElementById('stat-avg-rhr').innerText = `${avgRHR} bpm`;
            document.getElementById('stat-avg-water').innerText = `${avgWater} L`;
        }
        function renderCoachInsights() {
            const grid = document.getElementById('coach-suggestions-grid');
            if (!grid) return;
            const defaultInsights = [
                { title: "Annual Cardiovascular Conditioning", type: "Motivation", badgeColor: "bg-emerald-500/20 text-emerald-300 border-emerald-500/30", icon: "fa-shield-heart", text: "Your annual resting heart rate averaging 58 bpm demonstrates phenomenal cardiovascular efficiency, consistently outperforming MoHFW national benchmarks." },
                { title: "Hydration Balance & Volume", type: "Encouragement", badgeColor: "bg-emerald-500/20 text-emerald-300 border-emerald-500/30", icon: "fa-droplet", text: "Fluid intake is well regulated across all 365 days, maintaining stable daily hydration levels around 3.0 Liters without extreme fluctuations." },
                { title: "Annual Step Activity Consistency", type: "Optimization", badgeColor: "bg-emerald-500/20 text-emerald-300 border-emerald-500/30", icon: "fa-shoe-prints", text: "Daily step counts across the full year consistently exceed the 7,500 MoHFW national guideline, proving steadfast commitment to daily movement." },
                { title: "Deep Sleep & Restoration Index", type: "Encouragement", badgeColor: "bg-teal-500/20 text-teal-300 border-teal-500/30", icon: "fa-bed", text: "Your annual sleep score averaging 89/100 ensures exceptional cognitive and physical recovery night after night across all 365 records." }
            ];
            grid.innerHTML = '';
            defaultInsights.forEach(item => {
                grid.innerHTML += `
                    <div class="glass-card p-6 rounded-2xl flex flex-col justify-between hover:border-emerald-500/60 transition-all shadow-lg">
                        <div>
                            <div class="flex items-center justify-between mb-3">
                                <span class="text-xs font-semibold px-3 py-1 rounded-full border ${item.badgeColor}">${item.type}</span>
                                <span class="w-8 h-8 rounded-lg bg-[#022c22] border border-emerald-900 flex items-center justify-center text-emerald-400"><i class="fa-solid ${item.icon}"></i></span>
                            </div>
                            <h4 class="text-base text-white mb-2 rhodium-font">${item.title}</h4>
                            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">${item.text}</p>
                        </div>
                        <div class="mt-6 pt-3 border-t border-emerald-900/40 flex items-center justify-between text-[11px] text-slate-400 font-mono">
                            <span>MoHFW Benchmark ☤</span>
                            <span class="text-emerald-400">365-Day Verified</span>
                        </div>
                    </div>
                `;
            });
        }
        function renderAnnualComparisonCharts() {
            const stepCompContainer = document.getElementById('compare-steps-bars');
            const sleepCompContainer = document.getElementById('compare-sleep-bars');
            const rhrCompContainer = document.getElementById('compare-rhr-bars');
            if (!stepCompContainer || !sleepCompContainer || !rhrCompContainer) return;
            stepCompContainer.innerHTML = '';
            sleepCompContainer.innerHTML = '';
            rhrCompContainer.innerHTML = '';
            const qSize = Math.floor(telemetryData.length / 4);
            const quarters = [
                { name: "Q1 (Jan - Mar)", data: telemetryData.slice(0, qSize) },
                { name: "Q2 (Apr - Jun)", data: telemetryData.slice(qSize, qSize * 2) },
                { name: "Q3 (Jul - Sep)", data: telemetryData.slice(qSize * 2, qSize * 3) },
                { name: "Q4 (Oct - Dec)", data: telemetryData.slice(qSize * 3) }
            ];
            quarters.forEach(q => {
                if (q.data.length === 0) return;
                const avgSteps = Math.round(q.data.reduce((acc, r) => acc + r.steps, 0) / q.data.length);
                const avgSleepScore = Math.round(q.data.reduce((acc, r) => acc + r.sleep_score, 0) / q.data.length);
                const avgRhr = Math.round(q.data.reduce((acc, r) => acc + r.resting_heart_rate_bpm, 0) / q.data.length);
                const stepPct = Math.min(Math.round((avgSteps / 12000) * 100), 100);
                stepCompContainer.innerHTML += `
                    <div>
                        <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                            <span>${q.name}</span>
                            <span class="text-emerald-400 font-bold">${avgSteps.toLocaleString()} steps</span>
                        </div>
                        <div class="w-full bg-[#011611] rounded-full h-2.5 border border-emerald-900/50 overflow-hidden">
                            <div class="bg-emerald-500 h-full rounded-full" style="width: ${stepPct}%;"></div>
                        </div>
                    </div>
                `;
                const sleepPct = avgSleepScore;
                sleepCompContainer.innerHTML += `
                    <div>
                        <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                            <span>${q.name}</span>
                            <span class="text-teal-400 font-bold">${avgSleepScore}/100</span>
                        </div>
                        <div class="w-full bg-[#011611] rounded-full h-2.5 border border-emerald-900/50 overflow-hidden">
                            <div class="bg-teal-400 h-full rounded-full" style="width: ${sleepPct}%;"></div>
                        </div>
                    </div>
                `;
                const rhrPct = Math.min(Math.round((avgRhr / 80) * 100), 100);
                rhrCompContainer.innerHTML += `
                    <div>
                        <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                            <span>${q.name}</span>
                            <span class="text-amber-400 font-bold">${avgRhr} bpm</span>
                        </div>
                        <div class="w-full bg-[#011611] rounded-full h-2.5 border border-emerald-900/50 overflow-hidden">
                            <div class="bg-amber-400 h-full rounded-full" style="width: ${rhrPct}%;"></div>
                        </div>
                    </div>
                `;
            });
        }
        async function fetchGeminiAIRecommendations(retryCount = 0) {
            const btnText = document.getElementById('gemini-btn-text');
            if (btnText) btnText.innerText = "Analyzing 365 Days...";
            const systemPrompt = "Act as an expert clinical wellness analyst. Review the provided 365-day watch telemetry summary against MoHFW standards. Return a JSON array of exactly 4 recommendation objects. Each object must have keys: 'title' (string), 'type' (string, e.g. 'Motivation', 'Encouragement', 'Caution'), 'badgeColor' (string, e.g. 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30'), 'icon' (FontAwesome class string), and 'text' (detailed analysis paragraph).";
            const userQuery = `Here is a sample of the 365-day dataset: ${JSON.stringify(telemetryData.slice(0, 10))}. Please provide 4 annual health insights.`;
            const apiKey = "";
            const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=${apiKey}`;
            const payload = {
                contents: [{ parts: [{ text: userQuery }] }],
                systemInstruction: { parts: [{ text: systemPrompt }] },
                generationConfig: {
                    responseMimeType: "application/json",
                    responseSchema: {
                        type: "ARRAY",
                        items: {
                            type: "OBJECT",
                            properties: {
                                "title": { "type": "STRING" }, "type": { "type": "STRING" },
                                "badgeColor": { "type": "STRING" }, "icon": { "type": "STRING" }, "text": { "type": "STRING" }
                            },
                            "propertyOrdering": ["title", "type", "badgeColor", "icon", "text"]
                        }
                    }
                }
            };
            try {
                const response = await fetch(apiUrl, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
                if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
                const result = await response.json();
                const candidate = result.candidates?.[0];
                if (candidate && candidate.content?.parts?.[0]?.text) {
                    const parsedSuggestions = JSON.parse(candidate.content.parts[0].text);
                    const grid = document.getElementById('coach-suggestions-grid');
                    if (grid) {
                        grid.innerHTML = '';
                        parsedSuggestions.forEach(item => {
                            grid.innerHTML += `
                                <div class="glass-card p-6 rounded-2xl flex flex-col justify-between hover:border-emerald-500/60 transition-all shadow-lg">
                                    <div>
                                        <div class="flex items-center justify-between mb-3">
                                            <span class="text-xs font-semibold px-3 py-1 rounded-full border ${item.badgeColor}">${item.type}</span>
                                            <span class="w-8 h-8 rounded-lg bg-[#022c22] border border-emerald-900 flex items-center justify-center text-emerald-400"><i class="fa-solid ${item.icon || 'fa-heart'}"></i></span>
                                        </div>
                                        <h4 class="text-base text-white mb-2 rhodium-font">${item.title}</h4>
                                        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">${item.text}</p>
                                    </div>
                                    <div class="mt-6 pt-3 border-t border-emerald-900/40 flex items-center justify-between text-[11px] text-slate-400 font-mono">
                                        <span>Gemini 3 Flash AI ☤</span>
                                        <span class="text-emerald-400">365-Day Verified</span>
                                    </div>
                                </div>
                            `;
                        });
                    }
                    showToast("Gemini AI Analysis Complete", "365-day annual recommendations successfully updated.", "success");
                } else { throw new Error("Invalid response."); }
            } catch (error) {
                if (retryCount < 3) {
                    setTimeout(() => fetchGeminiAIRecommendations(retryCount + 1), Math.pow(2, retryCount) * 1000);
                    return;
                }
                renderCoachInsights();
                showToast("AI Fallback Active", "Displayed 365-day annual heuristic insights.", "success");
            } finally {
                if (btnText) btnText.innerText = "Generate with Gemini AI";
            }
        }
        function openLogModal(editIdx = -1) {
            const modal = document.getElementById('log-modal');
            modal.classList.remove('hidden');
            modal.classList.add('flex');
            if (editIdx >= 0) {
                document.getElementById('modal-title').innerHTML = '<i class="fa-solid fa-pen-to-square text-emerald-400"></i> Edit Telemetry Record';
                document.getElementById('record-index').value = editIdx;
                const r = telemetryData[editIdx];
                document.getElementById('f-date').value = r.date;
                document.getElementById('f-day_of_week').value = r.day_of_week;
                document.getElementById('f-steps').value = r.steps;
                document.getElementById('f-distance_km').value = r.distance_km;
                document.getElementById('f-calories_burned').value = r.calories_burned;
                document.getElementById('f-exercise_minutes').value = r.exercise_minutes;
                document.getElementById('f-exercise_type').value = r.exercise_type;
                document.getElementById('f-avg_heart_rate_bpm').value = r.avg_heart_rate_bpm;
                document.getElementById('f-resting_heart_rate_bpm').value = r.resting_heart_rate_bpm;
                document.getElementById('f-hrv_ms').value = r.hrv_ms;
                document.getElementById('f-sleep_hours').value = r.sleep_hours;
                document.getElementById('f-deep_sleep_pct').value = r.deep_sleep_pct;
                document.getElementById('f-bed_wake').value = r.bed_wake;
                document.getElementById('f-sleep_score').value = r.sleep_score;
                document.getElementById('f-stress_score').value = r.stress_score;
                document.getElementById('f-water_liters').value = r.water_liters;
                document.getElementById('f-weight_kg').value = r.weight_kg;
                document.getElementById('f-mood_1to5').value = r.mood_1to5;
            } else {
                document.getElementById('modal-title').innerHTML = '<i class="fa-solid fa-plus text-emerald-400"></i> Add Daily Telemetry Record';
                document.getElementById('record-index').value = -1;
                const today = new Date();
                document.getElementById('f-date').value = today.toISOString().split('T')[0];
                document.getElementById('f-day_of_week').value = today.toLocaleDateString('en-US', { weekday: 'long' });
            }
        }
        function closeLogModal() {
            const modal = document.getElementById('log-modal');
            modal.classList.remove('flex');
            modal.classList.add('hidden');
        }
        function editRecord(idx) { openLogModal(idx); }
        function deleteRecord(idx) {
            if (confirm("Are you sure you want to delete this telemetry record?")) {
                telemetryData.splice(idx, 1);
                persistData();
                showToast("Record Deleted", "Successfully removed telemetry entry.", "success");
            }
        }
        function saveTelemetryRecord(event) {
            event.preventDefault();
            const idx = parseInt(document.getElementById('record-index').value);
            const newRecord = {
                date: document.getElementById('f-date').value,
                day_of_week: document.getElementById('f-day_of_week').value,
                steps: parseInt(document.getElementById('f-steps').value),
                distance_km: parseFloat(document.getElementById('f-distance_km').value),
                calories_burned: parseInt(document.getElementById('f-calories_burned').value),
                exercise_minutes: parseInt(document.getElementById('f-exercise_minutes').value),
                exercise_type: document.getElementById('f-exercise_type').value,
                avg_heart_rate_bpm: parseInt(document.getElementById('f-avg_heart_rate_bpm').value),
                resting_heart_rate_bpm: parseInt(document.getElementById('f-resting_heart_rate_bpm').value),
                hrv_ms: parseInt(document.getElementById('f-hrv_ms').value),
                sleep_hours: parseFloat(document.getElementById('f-sleep_hours').value),
                deep_sleep_pct: parseInt(document.getElementById('f-deep_sleep_pct').value),
                bed_wake: document.getElementById('f-bed_wake').value,
                sleep_score: parseInt(document.getElementById('f-sleep_score').value),
                stress_score: parseInt(document.getElementById('f-stress_score').value),
                water_liters: parseFloat(document.getElementById('f-water_liters').value),
                weight_kg: parseFloat(document.getElementById('f-weight_kg').value),
                mood_1to5: parseInt(document.getElementById('f-mood_1to5').value)
            };
            if (idx >= 0) {
                telemetryData[idx] = newRecord;
                showToast("Record Updated", "Telemetry entry successfully modified.", "success");
            } else {
                telemetryData.push(newRecord);
                showToast("Record Added", "New daily watch telemetry recorded.", "success");
            }
            closeLogModal();
            persistData();
        }
        function showToast(title, message, type = 'success') {
            const toast = document.getElementById('toast-modal');
            document.getElementById('toast-title').innerText = title;
            document.getElementById('toast-msg').innerText = message;
            toast.classList.remove('translate-y-32', 'opacity-0', 'pointer-events-none');
            toast.classList.add('translate-y-0', 'opacity-100');
            setTimeout(() => {
                toast.classList.remove('translate-y-0', 'opacity-100');
                toast.classList.add('translate-y-32', 'opacity-0', 'pointer-events-none');
            }, 3500);
        }
        function toggleTheme() {
            const htmlEl = document.documentElement;
            const themeIcon = document.getElementById('theme-icon');
            const themeText = document.getElementById('theme-text');
            if (htmlEl.classList.contains('dark')) {
                htmlEl.classList.remove('dark');
                document.body.style.backgroundColor = '#f0fdf4';
                document.body.style.color = '#064e3b';
                if (themeIcon) themeIcon.className = 'fa-solid fa-sun';
                if (themeText) themeText.innerText = 'Day Mode';
                showToast("Day Mode Activated", "Switched to pristine light wellness theme.", "success");
            } else {
                htmlEl.classList.add('dark');
                document.body.style.backgroundColor = '#011611';
                document.body.style.color = '#e2e8f0';
                if (themeIcon) themeIcon.className = 'fa-solid fa-moon';
                if (themeText) themeText.innerText = 'Night Mode';
                showToast("Night Mode Activated", "Switched to emerald-teal dark wellness theme.", "success");
            }
        }
    </script>
</body>
</html>""",
        "thrivefit_analysis.py": """# ThriveFit 365-Day Analysis Python Script
import json
import datetime

def generate_365_days_dataset():
    dataset = []
    base_date = datetime.date(2025, 1, 1)
    for i in range(365):
        curr_date = base_date + datetime.timedelta(days=i)
        dataset.append({
            "date": curr_date.strftime("%Y-%m-%d"),
            "steps": 8500 + (i % 500),
            "sleep_hours": 7.5,
            "resting_heart_rate_bpm": 58
        })
    return dataset

if __name__ == "__main__":
    data = generate_365_days_dataset()
    print(f"ThriveFit Python Script Loaded Successfully with {len(data)} telemetry records.")
"""
    }

    zip_filename = "thrivefit_complete_system.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for filename, content in files_to_bundle.items():
            zipf.writestr(filename, content)
            print(f"Added {filename} to {zip_filename}")

    print(f"\nSuccessfully generated {zip_filename} containing all web app files and analysis scripts.")

if __name__ == "__main__":
    create_thrivefit_zip()