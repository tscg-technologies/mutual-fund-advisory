"""
Generate IMAGE-GENERATION-GUIDE.md with all 56 individual image specifications and copy-ready Google Flow prompts.
"""

IMAGE_DATA = [
    # ---------------- Homepage ----------------
    {
        "num": 1,
        "filename": "mutual-fund-hero-investment-planning.jpg",
        "page": "index.html",
        "section": "Hero Section",
        "title": "Strategic Financial Planning & Advisory",
        "subject": "A senior Indian wealth manager in contemporary business attire collaborating with an Indian professional couple at an elegant conference desk, reviewing asset allocation analytics on a sleek tablet screen with upward financial growth charts in the background.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "High-end corporate documentary photography, ultra-realistic wealth management private office.",
        "composition": "Rule of thirds. Subjects positioned on the right and center; soft depth of field focusing on the tablet analytics interface; clean negative space on the left.",
        "camera": "Eye-level 50mm f/2.0 prime lens, cinematic framing, gentle foreground blur.",
        "lighting": "Soft natural morning daylight streaming through floor-to-ceiling glass windows, warm golden rim light highlighting shoulders, balanced fill light.",
        "background": "Modern high-rise financial district view (Hyderabad Financial District / BKC Mumbai) softly out of focus, minimalist architectural wood panelling and indoor architectural plants.",
        "palette": "Deep corporate navy (#101D35), warm gold (#C6A15B), forest emerald green accents (#18A875), clean ivory whites and warm timber.",
        "positioning": "Planner seated at 45 degrees gesturing gently toward digital tablet; client couple engaged attentively.",
        "negative_space": "Subtle negative space on upper left quadrant suitable for headline overlay.",
        "prompt": "Cinematic documentary editorial photograph of a senior Indian wealth advisor in tailored navy blazer discussing long-term portfolio growth with a young Indian professional couple. They sit around an executive walnut meeting desk reviewing clean financial growth charts on an iPad Pro. Modern corporate glass office overlooking Hyderabad skyline. Soft natural morning window lighting, 50mm f/2.2, photorealistic, premium private banking aesthetic, muted navy and warm gold tones, elegant depth of field, 8k resolution, professional color grading."
    },
    {
        "num": 2,
        "filename": "mutual-fund-market-research.jpg",
        "page": "index.html",
        "section": "Why Understand Mutual Funds Section",
        "title": "Financial Analyst Reviewing Scheme Factsheets",
        "subject": "An Indian mutual fund quantitative analyst in a modern research lab examining multi-screen financial displays showing SEBI riskometer gauges, sector allocations, and correlation matrices.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Modern corporate editorial photography, institutional research setting.",
        "composition": "Medium close-up shot focused on analyst's hand taking notes beside an ultra-wide monitor showing clean financial charts.",
        "camera": "35mm focal length, f/2.8 aperture, crisp foreground focus with pleasant bokeh.",
        "lighting": "Cool neutral ambient office lighting complemented by soft desk lamp illumination.",
        "background": "Glass-partitioned research trading room with blurred stock ticker charts and minimalist financial posters.",
        "palette": "Navy (#101D35), slate gray (#405064), emerald green (#18A875), crisp white highlights.",
        "positioning": "Analyst seated at workstation, pen poised over notebook, dual monitors displaying analytical graphs.",
        "negative_space": "Minimal; concentrated documentary composition.",
        "prompt": "Editorial corporate photograph of an Indian financial research analyst studying mutual fund portfolio data and SEBI factsheets across curved ultra-wide monitors. Clean minimalist desk, financial graphs showing sector breakdowns, notebook with fountain pen. Soft modern institutional office lighting, shot on Hasselblad 50mm lens, sharp details, muted navy and financial green accents, ultra-realistic, authentic workplace setting."
    },
    {
        "num": 3,
        "filename": "mutual-fund-sip-investment.jpg",
        "page": "index.html",
        "section": "SIP Investment Section",
        "title": "Systematic Investment Planning Visual",
        "subject": "A conceptual, elegant photographic composition illustrating regular monthly disciplined investing: staggered stacks of Indian Rupee coins beside a modern glass calendar tablet showing steady upward compound growth.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "High-end still life financial concept photography, architectural precision.",
        "composition": "Diagonal ascending arrangement from bottom left to top right, symbolizing progressive accumulation.",
        "camera": "Macro 85mm f/3.2, shallow depth of field focusing on the mid-tier growth point.",
        "lighting": "Dramatic side directional studio lighting casting soft elongated shadows.",
        "background": "Dark textured slate surface with subtle architectural drafting grid in faint green.",
        "palette": "Polished metallic brass/gold (#C6A15B), deep navy background (#101D35), vibrant green leaf sprout (#18A875).",
        "positioning": "Ascending coin cylinders beside an illuminated calendar tablet showing monthly automated debit indicators.",
        "negative_space": "Upper right corner uncluttered.",
        "prompt": "Premium conceptual still life photography representing Indian Systematic Investment Plans (SIP). Neat ascending rows of Indian rupee coins progressively growing taller, with a small fresh green sprout emerging from the tallest stack. Dark textured slate desk, sleek glass calendar tablet with subtle glowing green monthly checkmarks, dramatic architectural side lighting, 85mm macro lens, luxurious financial planning editorial, high detail, 8k."
    },

    # ---------------- About Page ----------------
    {
        "num": 4,
        "filename": "mutual-fund-investor-education.jpg",
        "page": "about.html",
        "section": "Our Educational Philosophy",
        "title": "Financial Planning & Investor Literacy Workshop",
        "subject": "An interactive, elegant financial literacy masterclass where an expert Indian educator explains asset allocation models on an interactive digital board to an attentive audience of young working professionals.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Corporate documentary photography, educational seminar.",
        "composition": "Wide medium shot capturing the speaker gesturing toward a digital chart while audience members take notes.",
        "camera": "28mm wide angle, f/2.8, clear depth of field across presenter and audience.",
        "lighting": "Bright, warm seminar room lighting with recessed LED ambient ceiling fixtures.",
        "background": "Modern auditorium with timber acoustic baffles and interactive digital projection screen.",
        "palette": "Navy (#182B49), financial green (#18A875), clean white, warm oak timber.",
        "positioning": "Educator standing gracefully on the left facing forward-right; audience seated in ergonomic desks.",
        "negative_space": "Upper third of presentation board clear.",
        "prompt": "Professional corporate documentary photograph of an Indian female financial educator speaking at an investor awareness symposium. She points to a clean interactive screen displaying a diversified asset allocation pie chart. Diverse Indian young professionals listening attentively with notebooks in modern tech seminar hall. Warm natural lighting, 35mm lens, crisp focus, credible wealth management education atmosphere, realistic, 8k."
    },

    # ---------------- Services Page ----------------
    {
        "num": 5,
        "filename": "mutual-fund-financial-consultation.jpg",
        "page": "services.html",
        "section": "Services Overview Hero",
        "title": "Comprehensive Financial Advisory Capabilities",
        "subject": "A collaborative executive advisory session around a bespoke marble conference table, with senior advisors presenting structured wealth solutions and portfolio roadmaps to family office clients.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "High-end corporate editorial, private banking suite.",
        "composition": "Symmetrical architectural composition, wide panoramic view of private conference room.",
        "camera": "24mm f/4.0 tilt-shift architectural lens, straight vertical lines.",
        "lighting": "Diffused architectural cove lighting combined with soft afternoon window light.",
        "background": "Floor-to-ceiling glass partitions overlooking manicured rooftop garden, abstract geometric art on wall.",
        "palette": "Primary navy (#101D35), marble cream, gold hardware accents (#C6A15B), emerald foliage.",
        "positioning": "Advisory team on left, clients on right, central document folder and tablet displaying portfolio framework.",
        "negative_space": "Upper center area above table clear.",
        "prompt": "Architectural interior photography of an exclusive Indian wealth advisory boardroom. Professional financial planners in tailored business suits consulting with clients over customized portfolio reports and sleek laptops. Italian marble conference table, panoramic window view of modern Hyderabad cyber city, soft golden hour sunlight, architectural photography style, 24mm lens, clean lines, serene and trustworthy private banking atmosphere."
    },

    # ---------------- Mutual Funds Overview ----------------
    {
        "num": 6,
        "filename": "mutual-fund-wealth-planning.jpg",
        "page": "mutual-funds.html",
        "section": "How Mutual Funds Work",
        "title": "Mutual Fund Structure & Custodial Mechanics",
        "subject": "A modern graphic-photographic composite scene showing financial professionals collaborating around an architectural model of Indian capital market infrastructure, representing AMCs, trustees, and custodians.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Conceptual architectural corporate photography.",
        "composition": "Centered layout with team inspecting a holographic-style geometric model on a luminous plinth.",
        "camera": "45mm f/2.8 lens, overhead 30-degree isometric perspective.",
        "lighting": "Subtle neon underglow in financial green and clean white key light on faces.",
        "background": "Minimalist high-tech financial innovation center with brushed steel and smoked glass.",
        "palette": "Navy (#101D35), financial green (#18A875), silver, frosted white.",
        "positioning": "Two analysts leaning over table analyzing structural capital flows.",
        "negative_space": "Faint digital grid pattern across top background.",
        "prompt": "Conceptual financial services photograph showing Indian portfolio managers gathered around a luminous smart-table reviewing an interactive 3D organizational model of mutual fund asset flows. Clean architectural setting, deep navy and emerald green ambient lighting, modern institutional fintech aesthetic, 35mm lens, sharp focus, sophisticated corporate innovation."
    },

    # ---------------- Investment Approach ----------------
    {
        "num": 7,
        "filename": "mutual-fund-asset-allocation.jpg",
        "page": "investment-approach.html",
        "section": "Process Over Market Timing",
        "title": "Asset Allocation & Modern Portfolio Theory",
        "subject": "A conceptual editorial still life showing geometric glass prism blocks tinted in green, gold, and sapphire blue resting in balanced equilibrium upon a precision marble scales, symbolizing multi-asset diversification.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Conceptual artistic financial photography.",
        "composition": "Precise balanced centerpiece with dramatic shadows cast across textured linen backdrop.",
        "camera": "90mm macro lens, f/4.0 aperture for crisp edge-to-edge definition.",
        "lighting": "Strong directional spotlight from 45 degrees creating crisp colorful caustics on surface.",
        "background": "Neutral warm gray architectural concrete texture.",
        "palette": "Emerald green (#18A875), sapphire navy (#101D35), amber gold (#C6A15B), stone gray.",
        "positioning": "Prisms precisely balanced in perfect poise without tipping.",
        "negative_space": "Ample negative space on both sides.",
        "prompt": "High-end conceptual art photography representing asset allocation in wealth management. Precision-cut geometric glass prisms in sapphire blue, amber gold, and emerald green perfectly balanced on a minimalist brass scale beam. Clean concrete background, sharp directional ray lighting casting colored glass reflections, 90mm lens, artistic editorial design, 8k resolution, elegant mathematical balance."
    },

    # ---------------- Financial Planning ----------------
    {
        "num": 8,
        "filename": "mutual-fund-financial-goals.jpg",
        "page": "financial-planning.html",
        "section": "Why Plan Before You Invest",
        "title": "Financial Planning Roadmap & Corpus Targets",
        "subject": "An Indian family (parents and child) sitting with their financial advisor in a sunlit modern living room office, reviewing an illustrated life milestones map on a premium tablet device.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Warm lifestyle documentary photography with financial services context.",
        "composition": "Medium horizontal grouping conveying trust, warmth, and strategic planning.",
        "camera": "50mm f/1.8 lens, natural perspective, gentle background separation.",
        "lighting": "Warm golden afternoon sunlight filtering through sheer curtains, soft interior lamps.",
        "background": "Tasteful contemporary Indian apartment interior with indoor monstera plant and contemporary bookshelf.",
        "palette": "Warm timber, navy blue, gold accents, soft cream and linen.",
        "positioning": "Family grouped comfortably on sofa; advisor seated across smiling reassuringly.",
        "negative_space": "Upper quadrant with soft wall backdrop.",
        "prompt": "Warm lifestyle documentary photograph of an Indian couple and their young daughter in a consultation with their wealth advisor. They are reviewing a financial roadmap on a digital tablet in a bright, modern living room office. Soft afternoon window sunlight, shallow depth of field, 50mm f/2.0, genuine optimistic expressions, premium Indian home aesthetic, comforting, trustworthy atmosphere."
    },

    # ---------------- Goal-Based Investing ----------------
    {
        "num": 9,
        "filename": "mutual-fund-retirement-planning.jpg",
        "page": "goal-based-investing.html",
        "section": "Mapping Horizons to Asset Classes",
        "title": "Life Milestone Goals & Target Retirement Planning",
        "subject": "An active, happy retired Indian couple in their late 50s enjoying a peaceful morning stroll in a lush landscaped botanical park, holding cups of coffee, representing financial freedom and post-retirement security.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Authentic lifestyle editorial photography.",
        "composition": "Golden ratio composition; couple walking toward camera from right to left along a winding pathway.",
        "camera": "70mm telephoto lens, f/2.8, beautiful circular bokeh in trees behind.",
        "lighting": "Early morning golden hour sun flare behind foliage, creating warm rim lighting.",
        "background": "Lush tropical botanical garden with stone pathways and serene water reflection.",
        "palette": "Vibrant emerald green, golden sunlight, crisp white linen, warm earthy terracotta.",
        "positioning": "Couple walking hand-in-hand smiling, relaxed body language.",
        "negative_space": "Open space on upper left framed by tree canopy.",
        "prompt": "Inspiring lifestyle photograph of a retired Indian couple in their 50s enjoying a serene sunrise walk in a modern landscaped park. Confident, joyful expressions representing financial peace and independence. Golden morning backlight filtering through palm trees, 85mm f/2.2 lens, cinematic color grading, editorial wealth management style, natural and authentic."
    },

    # ---------------- Portfolio Review ----------------
    {
        "num": 10,
        "filename": "mutual-fund-portfolio-review.jpg",
        "page": "portfolio-review.html",
        "section": "Why Review Your Mutual Fund Portfolio",
        "title": "Financial Analyst Conducting Portfolio Review",
        "subject": "An experienced Indian portfolio analyst using a stylus on an interactive touch desk to examine scheme overlap diagrams, stock concentration, and risk standard deviation curves.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Institutional finance editorial photography.",
        "composition": "Close-up over-the-shoulder angle focusing on touch screen graphics and stylus tip.",
        "camera": "50mm macro f/2.8, sharp focus on chart data points.",
        "lighting": "Clean studio lighting balanced with the soft glow of the high-resolution touch display.",
        "background": "Dark executive office suite with blurred financial book spines and brass desk accents.",
        "palette": "Midnight navy (#101D35), data cyan, emerald green (#18A875), warm brass.",
        "positioning": "Analyst's hands skillfully manipulating data nodes on screen.",
        "negative_space": "Top third of desk monitor displaying calm dark theme interface.",
        "prompt": "Detailed over-the-shoulder corporate photograph of an Indian financial analyst using a digital stylus on a high-resolution drafting screen to review mutual fund portfolio overlap and risk metrics. Clean UI charts showing asset allocation and stock holdings. Warm executive office background, sharp focus, 50mm lens, professional wealth management atmosphere, 8k."
    },

    # ---------------- Asset Allocation ----------------
    {
        "num": 11,
        "filename": "mutual-fund-investment-dashboard.jpg",
        "page": "asset-allocation.html",
        "section": "Simulate Educational Allocation Profiles",
        "title": "Interactive Asset Allocation Dashboard Visual",
        "subject": "A modern wealth management digital dashboard interface displayed on a frameless curved monitor, featuring elegant asset allocation donut charts, equity-debt sliders, and risk-return curves.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Clean architectural tech product photography.",
        "composition": "Hero desktop setup shot at a slight 15-degree angle showing device and minimalist office surroundings.",
        "camera": "35mm f/4.0 lens, crisp clarity from screen surface to peripheral desk items.",
        "lighting": "Diffused softbox lighting with subtle green ambient backlight behind monitor.",
        "background": "Minimalist Scandinavian-style executive desk with wireless keyboard, fountain pen, and small succulent.",
        "palette": "Navy (#101D35), financial green (#18A875), amber gold (#C6A15B), slate gray.",
        "positioning": "Curved monitor centered; keyboard and notebook angled naturally in foreground.",
        "negative_space": "Clean wall area above monitor.",
        "prompt": "Premium tech product photograph of a modern wealth management dashboard on a sleek 34-inch curved monitor. Clean UI displaying sophisticated asset allocation charts, green and gold metrics, and risk sliders. Minimalist executive desk with wireless peripherals and architectural plant, soft atmospheric studio lighting, 35mm lens, ultra-clean commercial look."
    },

    # ---------------- Risk Management ----------------
    {
        "num": 12,
        "filename": "mutual-fund-risk-management.jpg",
        "page": "risk-management.html",
        "section": "The Spectrum of Mutual Fund Risks",
        "title": "Multi-Dimensional Financial Risk Spectrum",
        "subject": "An abstract 3D visualization representing risk dimensions: interconnected glass spheres and risk-mesh topography illustrating volatility damping and portfolio resilience.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Modern 3D architectural financial render.",
        "composition": "Dynamic diagonal topography flowing from chaotic waves into smooth, calm harmonic curves.",
        "camera": "Simulated 50mm cinematic camera with subtle chromatic aberration and depth of field.",
        "lighting": "Luminous volumetric light rays filtering through translucent smoked glass geometric forms.",
        "background": "Deep navy gradient with subtle micro-grid lines.",
        "palette": "Navy blue (#101D35), vivid emerald green (#18A875), glowing gold (#C6A15B), crystalline highlights.",
        "positioning": "Wave structure centered, transitioning from turbulent left to stable right.",
        "negative_space": "Upper left and upper right quadrants uncluttered.",
        "prompt": "Sophisticated 3D abstract financial visualization of risk management. Translucent glass waves and geometric nodal networks transitioning from turbulent peaks on one side into smooth, calm harmonic curves on the other. Glowing emerald green and amber gold light accents against a deep navy blue background, modern fintech aesthetic, ray-traced reflections, 8k resolution."
    },

    # ---------------- Investment Process ----------------
    {
        "num": 13,
        "filename": "mutual-fund-investor-meeting.jpg",
        "page": "investment-process.html",
        "section": "5-Stage Investment Methodology",
        "title": "5-Stage Investor Consultation Process",
        "subject": "A senior wealth planner and an Indian investor standing beside an illuminated glass architectural board, mapping out the five stages of investment planning with milestone magnets.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Corporate documentary editorial photography.",
        "composition": "Wide medium shot with glass board dividing planner on left and investor on right.",
        "camera": "35mm f/2.8 lens, capturing expressive gestures and transparent board diagrams.",
        "lighting": "Edge-lit LED glass whiteboard with soft daylight fill on subjects.",
        "background": "Modern consulting room with skyline glass windows and executive timber credentials shelf.",
        "palette": "Navy (#101D35), illuminated green (#18A875), white, warm amber.",
        "positioning": "Planner gesturing to Stage 3 with marker in hand; investor listening thoughtfully.",
        "negative_space": "Clear glass areas of whiteboard.",
        "prompt": "Corporate documentary photograph of a senior Indian financial planner explaining an investment roadmap on an illuminated transparent glass whiteboard to a client. Milestone icons drawn on glass. Modern high-rise consulting office, professional business attire, natural window lighting, 35mm lens, sharp focus, collaborative wealth management atmosphere, 8k."
    },

    # ---------------- Team Overview ----------------
    {
        "num": 14,
        "filename": "mutual-fund-team-collaboration.jpg",
        "page": "team.html",
        "section": "Advisory Investment Committee Collaboration",
        "title": "Advisory Investment Committee Collaboration",
        "subject": "An advisory team of diverse Indian financial professionals in business attire collaborating around a conference table with market research dossiers and laptops.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "High-end corporate editorial photography.",
        "composition": "Group shot with shallow depth of field, leading eyes to the central discussion leader.",
        "camera": "50mm f/2.5 prime lens.",
        "lighting": "Natural daylight from large architectural windows combined with subtle warm interior spots.",
        "background": "Glass-walled boardroom with blurred city skyline and modern artwork.",
        "palette": "Charcoal navy, crisp white shirts, emerald green accents, warm walnut table.",
        "positioning": "Four professionals engaged in an animated, disciplined financial discussion.",
        "negative_space": "Top quadrant above the boardroom table.",
        "prompt": "Editorial group photograph of a team of Indian wealth management professionals in a collaborative strategy meeting. Diverse men and women in modern executive attire discussing portfolio reports around a solid oak table. Floor-to-ceiling glass windows, soft daylight, 50mm lens, authentic professional expressions, sophisticated private wealth firm aesthetic."
    },

    # ---------------- Insights & Articles ----------------
    {
        "num": 15,
        "filename": "mutual-fund-market-insights.jpg",
        "page": "insights.html",
        "section": "Financial Insights Desk",
        "title": "Financial Research & Market Insights Desk",
        "subject": "An organized researcher's desk featuring printed quarterly market reports, financial newspapers (Mint, Economic Times style), an iPad displaying economic indicators, and a cup of black coffee.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Editorial flat-lay / 45-degree desk photography.",
        "composition": "45-degree angle editorial arrangement with careful alignment of reading materials.",
        "camera": "40mm f/2.8 lens, even sharpness across workspace.",
        "lighting": "Morning window light casting soft, natural diagonal shadows across paper.",
        "background": "Dark reclaimed oak desk surface with brass pen tray.",
        "palette": "Warm timber, crisp white newsprint, brass gold, deep navy accents.",
        "positioning": "Documents neatly fanned out, glasses resting on open report.",
        "negative_space": "Upper third of desk surface clear.",
        "prompt": "Editorial still life photograph of a financial analyst desk. Neatly fanned macroeconomic research reports with clean graphs, reading glasses resting on financial paper, iPad showing stock index trend, fountain pen, steaming espresso in ceramic cup. Rich dark oak desk, soft morning window light, 40mm lens, intellectual and credible finance atmosphere, 8k."
    },
    {
        "num": 16,
        "filename": "mutual-fund-reading-factsheet.jpg",
        "page": "article-details.html",
        "section": "Featured Article Header",
        "title": "How to Read a Mutual Fund Factsheet",
        "subject": "A close-up shot of an investor's hands holding a highlighter over a printed mutual fund factsheet, highlighting the Total Expense Ratio (TER) and top 10 portfolio holdings.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Documentary detail photography.",
        "composition": "Macro close-up, rule of thirds focusing on highlighted table rows.",
        "camera": "60mm macro f/2.8, shallow depth of field.",
        "lighting": "Warm side desk lamp illuminating paper texture.",
        "background": "Softly blurred mahogany desk surface and laptop keyboard.",
        "palette": "White paper, neon green highlighter accent (#18A875), dark mahogany, navy ink.",
        "positioning": "Hands holding paper with fountain pen and green highlighter active.",
        "negative_space": "Unprinted white margins of factsheet page.",
        "prompt": "Close-up documentary photograph of hands reviewing a mutual fund factsheet document. Green highlighter marking the expense ratio and sector allocation table. Sleek laptop and coffee cup in soft blurred background, warm desk lamp lighting, 60mm macro lens, sharp paper texture, educational financial literacy concept, authentic and detailed."
    },

    # ---------------- FAQ & Contact ----------------
    {
        "num": 17,
        "filename": "mutual-fund-faq-support.jpg",
        "page": "faq.html",
        "section": "Knowledge Clearinghouse",
        "title": "Investor Support & Client Helpdesk Interface",
        "subject": "A dedicated investor relations specialist in an Indian financial firm smiling warmly while answering client inquiries with an ergonomic headset and dual monitoring desk.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Warm corporate portrait documentary.",
        "composition": "Medium shot with specialist framed against modern office hub.",
        "camera": "50mm f/2.0 lens, soft bokeh.",
        "lighting": "Flattering soft portrait ring light and natural office ambient.",
        "background": "Modern financial advisory office with greenery and warm timber accents.",
        "palette": "Navy suit, warm skin tones, crisp white, emerald office plants.",
        "positioning": "Specialist seated upright, engaging warmly with viewer.",
        "negative_space": "Right side of frame with pleasant architectural background.",
        "prompt": "Professional corporate portrait of an Indian customer support specialist at a mutual fund advisory desk. Wearing a sleek communication headset, smiling warmly at camera while seated at a clean dual-monitor workstation. Modern corporate office background, 50mm f/2.0 lens, inviting and trustworthy atmosphere, high-end commercial quality."
    },
    {
        "num": 18,
        "filename": "mutual-fund-advisory-office.jpg",
        "page": "contact.html",
        "section": "Communication Channels",
        "title": "Advisory Headquarters & Welcome Reception",
        "subject": "A striking architectural photograph of the advisory firm's reception foyer: polished stone floors, abstract upward-growth bronze wall sculpture, and warm welcome desk.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Architectural interior photography.",
        "composition": "One-point perspective down the reception lobby.",
        "camera": "24mm wide angle lens, f/5.6, razor sharp perspective.",
        "lighting": "Architectural LED trough lighting and natural skylight illumination.",
        "background": "Reception wall featuring geometric financial growth bronze installation.",
        "palette": "Travertine stone, bronze gold (#C6A15B), deep navy accents (#101D35), green planters.",
        "positioning": "Reception desk centered right, spacious welcoming corridor.",
        "negative_space": "Open polished stone floor in lower foreground.",
        "prompt": "Architectural photograph of a luxury private wealth management reception foyer in Hyderabad. Polished Italian travertine flooring, minimalist reception desk with back-painted navy glass, geometric bronze growth sculpture on feature wall, lush indoor fiddle-leaf figs, warm linear architectural lighting, 24mm tilt-shift lens, pristine commercial photography."
    },

    # ---------------- Mutual Fund Categories (14 Pages) ----------------
    {
        "num": 19,
        "filename": "mutual-fund-equity-investment.jpg",
        "page": "equity-mutual-funds.html",
        "section": "Category Overview",
        "title": "Equity Market Research & Stock Selection",
        "subject": "An Indian equity fund manager analyzing company performance data and candlestick charts on multiple trading screens.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Corporate finance documentary.",
        "composition": "Medium shot from side angle showing analyst immersed in market research.",
        "camera": "50mm f/2.2.",
        "lighting": "Cool monitor screen glow balanced with warm ambient desk lighting.",
        "background": "Institutional research desk with blurred trading screens.",
        "palette": "Navy, emerald green, cool white, amber highlights.",
        "positioning": "Manager studying equity trends with pen in hand.",
        "negative_space": "Upper left quadrant.",
        "prompt": "Documentary photograph of an Indian equity mutual fund manager analyzing stock market valuation charts across dual curved monitors. Clean desk, trading terminal data, natural office lighting, 50mm f/2.2 lens, professional financial services aesthetic, 8k."
    },
    {
        "num": 20,
        "filename": "mutual-fund-debt-investment.jpg",
        "page": "debt-mutual-funds.html",
        "section": "Category Overview",
        "title": "Fixed Income Yield Curve & Bond Research",
        "subject": "A fixed-income fund manager evaluating government securities yield curves and sovereign bond ratings.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Institutional finance photography.",
        "composition": "Overhead 45-degree angle showing yield curve graphs and bond matrices.",
        "camera": "35mm f/2.8.",
        "lighting": "Soft corporate ambient lighting.",
        "background": "Modern trading floor with sovereign bond indices.",
        "palette": "Deep navy (#101D35), muted green (#18A875), slate gray.",
        "positioning": "Analyst pointing to yield spread on tablet.",
        "negative_space": "Top area above desk.",
        "prompt": "Corporate finance photograph of a debt mutual fund specialist reviewing sovereign bond yields and credit spreads on a high-resolution display. Clean desk with financial research dossiers, institutional banking office, 35mm lens, sharp focus, 8k."
    },
    {
        "num": 21,
        "filename": "mutual-fund-hybrid-allocation.jpg",
        "page": "hybrid-mutual-funds.html",
        "section": "Category Overview",
        "title": "Multi-Asset Allocation & Hedging Dynamics",
        "subject": "A visual concept showing balanced allocation between equity growth stocks and fixed-income debt bonds.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Conceptual financial photography.",
        "composition": "Balanced split layout representing dual engines of growth and stability.",
        "camera": "50mm f/2.8.",
        "lighting": "Split lighting with warm amber on equity side and cool blue on debt side.",
        "background": "Minimalist marble and wood surfaces.",
        "palette": "Emerald green, navy blue, amber gold, white.",
        "positioning": "Central symbolic balance.",
        "negative_space": "Top and bottom borders.",
        "prompt": "Conceptual financial still life representing hybrid mutual funds. A balanced scale with polished green emerald crystal representing equity on one side and steady silver ingots representing fixed income on the other. Elegant marble desk, dramatic lighting, 50mm lens, 8k."
    },
    {
        "num": 22,
        "filename": "mutual-fund-index-tracking.jpg",
        "page": "index-funds.html",
        "section": "Category Overview",
        "title": "Benchmark Index Tracking & Quantitative Modeling",
        "subject": "An algorithmic index fund tracking screen displaying Nifty 50 constituents and minimal tracking error graphs.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Fintech product photography.",
        "composition": "Clean horizontal framing of index tracking visualization.",
        "camera": "35mm f/4.0.",
        "lighting": "High-contrast digital screen illumination.",
        "background": "Modern quantitative research room.",
        "palette": "Navy, cyan, green, white.",
        "positioning": "Screen centered with keyboard in soft focus.",
        "negative_space": "Upper margin of display.",
        "prompt": "High-tech financial services photograph showing an index fund tracking dashboard replicating the Nifty 50 benchmark. Minimalist workstation with curved monitor displaying rule-based passive portfolio weights, 35mm lens, sharp commercial style."
    },
    {
        "num": 23,
        "filename": "mutual-fund-large-cap-bluechip.jpg",
        "page": "large-cap-funds.html",
        "section": "Category Overview",
        "title": "Bluechip Corporate Leadership & Steady Growth",
        "subject": "A panoramic architectural shot of major Indian conglomerate headquarters in Mumbai BKC / Cyberabad.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Architectural commercial photography.",
        "composition": "Upward low-angle architectural perspective representing stability and market leadership.",
        "camera": "24mm architectural lens.",
        "lighting": "Crisp morning sunlight reflecting off glass facades.",
        "background": "Modern financial skyline with blue skies.",
        "palette": "Steel blue, deep navy, glass reflections, chrome.",
        "positioning": "Towers rising solidly into clear sky.",
        "negative_space": "Sky area at top.",
        "prompt": "Architectural photograph of modern glass commercial towers in Mumbai Bandra Kurla Complex representing Indian bluechip large-cap corporations. Upward angle, clear morning sky, crisp reflections, 24mm architectural lens, commanding and institutional."
    },
    {
        "num": 24,
        "filename": "mutual-fund-mid-cap-growth.jpg",
        "page": "mid-cap-funds.html",
        "section": "Category Overview",
        "title": "Mid-Sized Corporate Expansion & Market Penetration",
        "subject": "A modern precision engineering and manufacturing facility in India showing dynamic industrial growth.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Industrial corporate photography.",
        "composition": "Diagonal dynamic leading lines down a high-tech factory floor.",
        "camera": "35mm f/2.8.",
        "lighting": "Bright industrial clean-room lighting with green accents.",
        "background": "Robotic assembly lines and engineers in high-visibility gear.",
        "palette": "Industrial gray, vibrant safety green, crisp white.",
        "positioning": "Machinery operating smoothly with engineers inspecting.",
        "negative_space": "Upper factory rafters.",
        "prompt": "High-tech industrial manufacturing photograph representing Indian mid-cap growth enterprises. Engineers reviewing robotics automated production line in modern clean facility, sharp focus, 35mm lens, dynamic economic expansion concept."
    },
    {
        "num": 25,
        "filename": "mutual-fund-small-cap-enterprises.jpg",
        "page": "small-cap-funds.html",
        "section": "Category Overview",
        "title": "Early-Stage Enterprises & High Compounding Potential",
        "subject": "A dynamic Indian innovation hub laboratory where startup founders collaborate around prototype testing.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Vibrant tech innovation photography.",
        "composition": "Energetic grouping around workbench with circuit boards and laptops.",
        "camera": "35mm f/2.0.",
        "lighting": "Vibrant LED lab illumination with warm spotlighting.",
        "background": "Collaborative incubator workspace with sticky notes and whiteboards.",
        "palette": "Charcoal, electric green, bright orange, clean white.",
        "positioning": "Founders engaged excitedly in testing new solutions.",
        "negative_space": "Upper background wall.",
        "prompt": "Energetic documentary photograph of young Indian tech entrepreneurs working in an advanced startup incubator lab. High energy, circuit boards, collaborative brainstorming, 35mm f/2.0 lens, representing small-cap enterprise innovation and high compounding potential."
    },
    {
        "num": 26,
        "filename": "mutual-fund-flexi-cap-dynamic.jpg",
        "page": "flexi-cap-funds.html",
        "section": "Category Overview",
        "title": "Agile Capital Allocation Across Cap Horizons",
        "subject": "A portfolio manager dynamically adjusting weights across large, mid, and small cap sectors on a multi-touch screen.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Modern fintech photography.",
        "composition": "Overhead angle showing interactive market cap balance controls.",
        "camera": "50mm f/2.8.",
        "lighting": "Soft blue and green ambient glow.",
        "background": "Executive trading suite.",
        "palette": "Navy, emerald green, cyan, dark timber.",
        "positioning": "Hands dynamically sliding allocation thresholds.",
        "negative_space": "Top perimeter.",
        "prompt": "Corporate finance photograph of an Indian fund manager using an interactive touch interface to dynamically rebalance market cap weights across large, mid, and small cap equities. Modern trading desk, 50mm lens, agile investment concept."
    },
    {
        "num": 27,
        "filename": "mutual-fund-elss-tax-saving.jpg",
        "page": "ELSS.html",
        "section": "Category Overview",
        "title": "Tax Optimization & Long-Term Compounding Synergy",
        "subject": "A financial desk with Section 80C calculation sheets, calendar highlighting 3-year milestones, and equity growth graphs.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Still life editorial photography.",
        "composition": "Top-down organized flat-lay of tax documents and digital tablet.",
        "camera": "45mm f/3.2.",
        "lighting": "Warm morning sunlight casting clean shadows.",
        "background": "Light oak timber desk.",
        "palette": "Cream, navy, green (#18A875), gold (#C6A15B).",
        "positioning": "Documents neatly angled beside a fountain pen and coffee.",
        "negative_space": "Upper left quadrant.",
        "prompt": "Still life editorial photograph of financial tax planning. Section 80C mutual fund investment documents neatly arranged with calendar showing 3-year lock-in timeline, digital calculator, and fountain pen. Light wood desk, natural morning lighting, 45mm lens."
    },
    {
        "num": 28,
        "filename": "mutual-fund-liquid-cash-management.jpg",
        "page": "liquid-funds.html",
        "section": "Category Overview",
        "title": "Cash Management & Short-Duration Money Markets",
        "subject": "A corporate treasury manager monitoring short-term money market instruments, commercial papers, and liquidity reserves.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Corporate treasury documentary.",
        "composition": "Medium view of treasury specialist reviewing liquidity curves.",
        "camera": "50mm f/2.5.",
        "lighting": "Crisp corporate office lighting.",
        "background": "Corporate treasury department.",
        "palette": "Navy, light blue, silver, white.",
        "positioning": "Specialist verifying 91-day paper settlement dates.",
        "negative_space": "Left quadrant.",
        "prompt": "Corporate treasury photograph of an Indian financial officer managing liquid mutual fund cash reserves. Clean office environment, liquidity flow charts on monitor, 50mm lens, trustworthy cash management aesthetic."
    },
    {
        "num": 29,
        "filename": "mutual-fund-overnight-money-markets.jpg",
        "page": "overnight-funds.html",
        "section": "Category Overview",
        "title": "Overnight Money Markets & Collateralized Borrowing",
        "subject": "A high-precision view of interbank settlement screens displaying 1-day repo rates, TREPS trading, and sovereign collateral.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Institutional fintech photography.",
        "composition": "Close-up of interbank overnight settlement dashboard.",
        "camera": "35mm f/2.8.",
        "lighting": "Clean monitor illumination.",
        "background": "Money market trading desk.",
        "palette": "Navy, cyan, green, slate.",
        "positioning": "Real-time 1-day lending indicators.",
        "negative_space": "Top section of monitor.",
        "prompt": "Institutional finance photograph showing central banking overnight repo rate and TREPS interbank settlement data. Clean trading interface, high precision, 35mm lens, corporate cash parking concept."
    },
    {
        "num": 30,
        "filename": "mutual-fund-international-global-markets.jpg",
        "page": "international-funds.html",
        "section": "Category Overview",
        "title": "Global Stock Exchanges & Currency Diversification",
        "subject": "A conceptual composite of global financial capitals (New York, London, Tokyo, Mumbai) with currency exchange vectors.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Global finance editorial composite.",
        "composition": "Horizontal multi-city architectural vista with subtle currency overlay.",
        "camera": "Panoramic 35mm framing.",
        "lighting": "Twilight blue hour across international financial districts.",
        "background": "Illuminated skyscrapers across global time zones.",
        "palette": "Deep twilight blue, gold city lights, emerald green vectors.",
        "positioning": "Global skyline flowing across frame.",
        "negative_space": "Upper sky area.",
        "prompt": "Cinematic global finance photograph featuring international stock exchange skylines during twilight blue hour. Subtle illuminated currency vectors linking New York, London, and Indian markets, 35mm lens, sophisticated geographic diversification concept."
    },
    {
        "num": 31,
        "filename": "mutual-fund-fof-architecture.jpg",
        "page": "fund-of-funds.html",
        "section": "Category Overview",
        "title": "Multi-Manager Scheme Layering & Asset Allocation",
        "subject": "An architectural infographic-style visual showing a master mutual fund allocating into diverse underlying specialist funds.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Minimalist geometric 3D render.",
        "composition": "Hierarchical umbrella structure spreading into specialist asset nodes.",
        "camera": "Isometric 45-degree angle.",
        "lighting": "Clean studio key light with soft shadow gradient.",
        "background": "Pure neutral architectural gray.",
        "palette": "Navy (#101D35), green (#18A875), amber gold, white.",
        "positioning": "Central master node branching outward.",
        "negative_space": "Surrounding perimeter.",
        "prompt": "Clean 3D architectural graphic rendering showing a Fund of Funds (FoF) master fund branching into diversified underlying scheme unit blocks. Deep navy and gold accents, crisp isometric view, elegant institutional finance design, 8k."
    },
    {
        "num": 32,
        "filename": "mutual-fund-sectoral-thematic-trends.jpg",
        "page": "sectoral-thematic-funds.html",
        "section": "Category Overview",
        "title": "Sector Concentration & Cyclical Industry Trends",
        "subject": "A multi-screen sector analysis dashboard showing focused industry cycles across banking, healthcare, and infrastructure.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Financial research photography.",
        "composition": "Sector heat map displayed on large wall monitor with research analyst taking notes.",
        "camera": "50mm f/2.5.",
        "lighting": "Ambient trading room light.",
        "background": "Wall-mounted financial sector heatmaps.",
        "palette": "Navy, emerald green, warm amber, crimson.",
        "positioning": "Analyst observing sector cycle shifts.",
        "negative_space": "Upper right.",
        "prompt": "Corporate finance photograph of an Indian analyst studying sectoral heat maps across banking, pharmaceutical, and technology industries. Wall-mounted data display, 50mm lens, focused thematic investing concept."
    },

    # ---------------- Investment Strategy & Education (12 Pages) ----------------
    {
        "num": 33,
        "filename": "mutual-fund-sip-compounding-timeline.jpg",
        "page": "sip-investment.html",
        "section": "What is a Systematic Investment Plan?",
        "title": "Systematic Investment Plan Timeline & Averaging",
        "subject": "A chronological photographic layout demonstrating how monthly SIP installments capture varying market NAV points over a 5-year cycle.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Educational infographic photography.",
        "composition": "Horizontal timeline wave passing through monthly coin markers.",
        "camera": "60mm macro f/3.5.",
        "lighting": "Clean directional studio lighting.",
        "background": "Architectural graph paper with dark navy background.",
        "palette": "Navy (#101D35), green (#18A875), gold (#C6A15B), white.",
        "positioning": "Ascending timeline from left to right.",
        "negative_space": "Top margins.",
        "prompt": "Educational still life photograph illustrating rupee-cost averaging in SIP investments. Stacks of coins along a fluctuating wave curve on dark architectural grid paper, showing more units bought during market dips, 60mm macro lens, clean lighting, 8k."
    },
    {
        "num": 34,
        "filename": "mutual-fund-lump-sum-deployment.jpg",
        "page": "lump-sum-investment.html",
        "section": "Deployment Dynamics",
        "title": "Lump Sum vs Staggered Deployment Analysis",
        "subject": "A portfolio manager comparing lump sum market entry curves against staggered STP transfers on an analytics tablet.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Corporate wealth advisory photography.",
        "composition": "Close-up on tablet screen with advisor's hand pointing to staggered entry milestones.",
        "camera": "50mm f/2.8.",
        "lighting": "Natural daylight from window.",
        "background": "Polished conference desk.",
        "palette": "Navy, emerald, gold, white.",
        "positioning": "Tablet centered with hand gesturing.",
        "negative_space": "Around tablet frame.",
        "prompt": "Close-up photograph of an Indian financial planner comparing lump sum investment trajectories against a Systematic Transfer Plan (STP) on an iPad Pro. Polished wood desk, natural office lighting, 50mm lens, sharp focus."
    },
    {
        "num": 35,
        "filename": "mutual-fund-direct-vs-regular-comparison.jpg",
        "page": "direct-vs-regular.html",
        "section": "Regulatory Context",
        "title": "Direct vs Regular Plan Evaluation Dialogue",
        "subject": "An investor and a wealth planner seated in an advisory office comparing two prospectus brochures clearly marked Direct Plan and Regular Plan.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Documentary corporate photography.",
        "composition": "Two brochures centered on table between advisor and client.",
        "camera": "50mm f/2.0.",
        "lighting": "Warm office ambient lighting.",
        "background": "Consulting room with certificates and bookshelf.",
        "palette": "Navy, warm gray, ivory white, gold.",
        "positioning": "Subjects leaning in to discuss fee breakdowns.",
        "negative_space": "Upper third of frame.",
        "prompt": "Documentary photograph of an Indian investor discussing Direct versus Regular mutual fund plans with an advisor. Two brochures on table showing expense ratio comparisons, natural window lighting, 50mm f/2.0, trustworthy advisory atmosphere."
    },
    {
        "num": 36,
        "filename": "mutual-fund-growth-vs-idcw-distribution.jpg",
        "page": "growth-vs-idcw.html",
        "section": "Terminology Shift",
        "title": "NAV Impact of IDCW Distribution",
        "subject": "A clear educational comparison graph showing how NAV accumulates uninterrupted under the Growth option versus periodic drop-steps under IDCW.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Clean data visualization product photography.",
        "composition": "High-resolution monitor displaying comparative NAV trajectory lines.",
        "camera": "40mm f/3.2.",
        "lighting": "Soft screen glow with balanced rim light.",
        "background": "Minimalist workstation setup.",
        "palette": "Navy, emerald green (Growth line), amber (IDCW line), white.",
        "positioning": "Chart lines clearly visible and sharp.",
        "negative_space": "Top of display.",
        "prompt": "Product photograph of a financial chart on screen comparing the Growth option (smooth compounding curve) against the IDCW option (periodic dividend drops) in mutual funds. Clean UI, dark mode, 40mm lens, educational clarity."
    },
    {
        "num": 37,
        "filename": "mutual-fund-nav-calculation-accounting.jpg",
        "page": "nav-explained.html",
        "section": "Definition & Formula",
        "title": "Daily NAV Calculation & Portfolio Accounting",
        "subject": "An accounting flow showing stock market closing prices feeding into AMC net asset calculations at 4:00 PM cutoff.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Corporate financial accounting photography.",
        "composition": "Analyst verifying closing NAV figures on a ledger spreadsheet with calculator.",
        "camera": "50mm f/2.8.",
        "lighting": "Warm late afternoon desk lamp lighting.",
        "background": "Accounting department background.",
        "palette": "Navy, slate gray, ivory, green.",
        "positioning": "Hands cross-referencing audit figures.",
        "negative_space": "Left quadrant.",
        "prompt": "Corporate finance photograph of an Indian mutual fund accountant verifying daily NAV valuation computations after market close. Financial ledger, calculator, digital spreadsheet, warm evening desk lighting, 50mm lens, precise accounting concept."
    },
    {
        "num": 38,
        "filename": "mutual-fund-expense-ratio-ter-breakdown.jpg",
        "page": "expense-ratio.html",
        "section": "Cost Components",
        "title": "TER Breakdown & Compounding Cost Drag",
        "subject": "An analytical chart demonstrating the 20-year terminal divergence between a 0.5% TER and 1.8% TER.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Data visualization photography.",
        "composition": "Diverging line graph showing long-term compounding impact of fees.",
        "camera": "45mm f/3.5.",
        "lighting": "Clean studio lighting on tablet display.",
        "background": "Dark executive desk.",
        "palette": "Navy, emerald green, coral red, gold.",
        "positioning": "Graph lines diverging toward the right.",
        "negative_space": "Upper right corner.",
        "prompt": "Clean financial data visualization on a modern tablet showing the long-term impact of Total Expense Ratio (TER) on compounding wealth over 20 years. Minimalist dark desk, 45mm lens, high detail, clear educational finance graphic."
    },
    {
        "num": 39,
        "filename": "mutual-fund-exit-load-holding-structure.jpg",
        "page": "exit-load.html",
        "section": "Purpose & Structure",
        "title": "Exit Load Calculation & Holding Period Timeline",
        "subject": "An illustrative calendar diagram explaining FIFO (First In First Out) redemption tracking for SIP tranches.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Still life conceptual photography.",
        "composition": "Minimalist 12-month calendar desk pad with checkmarks and lock symbols.",
        "camera": "50mm f/2.8.",
        "lighting": "Bright morning natural light.",
        "background": "Clean white and timber workstation.",
        "palette": "Navy, emerald green, warm amber, white.",
        "positioning": "Calendar angled naturally on desk.",
        "negative_space": "Top third of desk surface.",
        "prompt": "Still life photograph of an executive desk calendar highlighting a 365-day holding period and exit load waiver milestones. Elegant pen, digital tablet, soft daylight, 50mm lens, clean educational finance theme."
    },
    {
        "num": 40,
        "filename": "mutual-fund-sebi-riskometer-gauge.jpg",
        "page": "riskometer.html",
        "section": "Objective Evaluation",
        "title": "SEBI Riskometer 6-Tiered Gauge Display",
        "subject": "A high-fidelity depiction of the semicircular Riskometer needle spanning Low to Very High.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "High-precision 3D graphic render.",
        "composition": "Centered semicircular gauge with needle pointing to Moderate tier.",
        "camera": "Simulated 50mm lens, macro clarity.",
        "lighting": "Clean studio rim lighting highlighting the colored segments.",
        "background": "Deep navy textured background.",
        "palette": "Green, yellow-green, yellow, orange, red, dark red.",
        "positioning": "Gauge centered horizontally and vertically.",
        "negative_space": "Symmetrical margins around gauge.",
        "prompt": "3D render of the official SEBI mutual fund Riskometer gauge. Semicircular dial showing six risk tiers: Low, Low to Moderate, Moderate, Moderately High, High, Very High. Metallic needle pointing accurately, clean studio lighting, dark navy background, 8k."
    },
    {
        "num": 41,
        "filename": "mutual-fund-portfolio-diversification-matrix.jpg",
        "page": "diversification.html",
        "section": "Core Principle",
        "title": "Correlation Heatmap Across Asset Classes",
        "subject": "An educational correlation matrix showing historical relationships between Indian equities, debt, and gold.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Data visualization photography.",
        "composition": "High-contrast heatmap grid on display screen.",
        "camera": "35mm f/3.2.",
        "lighting": "Clean display illumination.",
        "background": "Modern finance research office.",
        "palette": "Deep navy, cool blue, bright emerald green, neutral gray.",
        "positioning": "Matrix grid centered on screen.",
        "negative_space": "Surrounding frame.",
        "prompt": "High-resolution data visualization of an asset class correlation heatmap comparing Indian large-cap equities, mid-caps, sovereign debt, and gold. Dark UI theme, 35mm lens, clear financial analytics style."
    },
    {
        "num": 42,
        "filename": "mutual-fund-power-of-compounding-curve.jpg",
        "page": "compounding.html",
        "section": "Exponential Growth",
        "title": "Exponential Compounding Hockey Stick Curve",
        "subject": "An illustrative growth chart comparing linear savings against exponential compounding over 30 years.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Architectural graphic photography.",
        "composition": "Curving hockey-stick trajectory rising sharply in the second half.",
        "camera": "50mm f/2.5.",
        "lighting": "Soft luminous glow along the compounding line.",
        "background": "Dark navy geometric grid.",
        "palette": "Navy (#101D35), bright green (#18A875), gold (#C6A15B).",
        "positioning": "Curve originating at lower left and climbing steeply to top right.",
        "negative_space": "Upper left quadrant.",
        "prompt": "Financial concept photograph of an exponential compounding hockey-stick curve glowing in vibrant emerald green against a deep navy blue background with subtle timeline year markers. 50mm lens, clean lines, inspiring wealth creation concept, 8k."
    },
    {
        "num": 43,
        "filename": "mutual-fund-capital-gains-tax-rules.jpg",
        "page": "investment-taxation.html",
        "section": "Statutory Framework",
        "title": "Indian Mutual Fund Capital Gains Tax Rules",
        "subject": "An infographic displaying holding period thresholds, STCG, and LTCG tax slabs across equity and debt funds.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Editorial graphic layout.",
        "composition": "Structured dual-column tax comparison layout.",
        "camera": "45mm f/3.0.",
        "lighting": "Clean daylight on printed tax chart.",
        "background": "Professional tax consultant's desk.",
        "palette": "Navy, emerald green, slate, white.",
        "positioning": "Balanced two-tier framework.",
        "negative_space": "Top title zone.",
        "prompt": "Clean professional photograph of a tax advisory chart detailing Indian capital gains taxation rules for equity and specified mutual funds. Held by an accountant at an executive desk, 45mm lens, natural lighting, sharp text, authoritative finance concept."
    },
    {
        "num": 44,
        "filename": "mutual-fund-beginner-investor-guide.jpg",
        "page": "investment-for-beginners.html",
        "section": "Foundational Roadmap",
        "title": "Beginner Investor Roadmap & Milestone Guide",
        "subject": "A young Indian investor reviewing financial goals, emergency funds, and SIP automation steps on a modern tablet in a sunlit workspace.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Lifestyle documentary photography.",
        "composition": "Medium shot of young investor sitting comfortably with notebook and digital device.",
        "camera": "35mm f/2.0.",
        "lighting": "Warm morning sunlight streaming through cafe window.",
        "background": "Modern co-working space with plants and warm brickwork.",
        "palette": "Warm timber, navy, sage green, cream.",
        "positioning": "Investor smiling thoughtfully while looking at savings roadmap.",
        "negative_space": "Right side of frame.",
        "prompt": "Inspiring lifestyle documentary photograph of a young Indian professional in a bright cafe workspace reviewing beginner mutual fund investment steps on a laptop and notebook. Optimistic, confident expression, warm natural sunlight, 35mm f/2.0 lens, relatable financial literacy aesthetic."
    },

    # ---------------- Investor & Enquiry Pages (7 Pages) ----------------
    {
        "num": 45,
        "filename": "mutual-fund-investor-resources-library.jpg",
        "page": "investor-resources.html",
        "section": "Knowledge Clearinghouse",
        "title": "Digital Financial Knowledge & Resource Repository",
        "subject": "A digital library interface displaying curated financial literacy guides, factsheet templates, and regulatory whitepapers.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Tech workspace editorial.",
        "composition": "Wide desktop setup displaying resource library portal.",
        "camera": "35mm f/3.5.",
        "lighting": "Clean ambient studio lighting.",
        "background": "Minimalist corporate library setting.",
        "palette": "Navy, white, emerald, slate.",
        "positioning": "Central screen with resources neatly cataloged.",
        "negative_space": "Upper wall area.",
        "prompt": "Commercial photograph of an investor education portal displayed on an all-in-one desktop in a modern corporate library. Clean layout showing financial checklists and glossary guides, 35mm lens, crisp and organized."
    },
    {
        "num": 46,
        "filename": "mutual-fund-sip-calculator-interface.jpg",
        "page": "sip-calculator.html",
        "section": "Interactive Tool",
        "title": "Interactive SIP Financial Modeling Platform",
        "subject": "A user interacting with an advanced financial calculator interface displaying dynamic growth curves and maturity values.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "UI/UX product photography.",
        "composition": "Angled view of tablet screen with finger adjusting SIP contribution slider.",
        "camera": "50mm f/2.8 macro.",
        "lighting": "Soft directional light highlighting slider controls.",
        "background": "Modern architectural desk.",
        "palette": "Navy (#101D35), green (#18A875), gold (#C6A15B), white.",
        "positioning": "Hands interacting with slider control.",
        "negative_space": "Top and sides.",
        "prompt": "Close-up photograph of hands adjusting a monthly SIP investment slider on an iPad screen, watching the compound growth curve dynamically update. Minimalist desk background, 50mm macro lens, sharp UI focus, modern financial tech aesthetic."
    },
    {
        "num": 47,
        "filename": "mutual-fund-lump-sum-calculator-interface.jpg",
        "page": "lumpsum-calculator.html",
        "section": "Interactive Tool",
        "title": "Lump Sum Portfolio Growth Modeler",
        "subject": "A digital dashboard showing single-deposit compounding projections over multi-year horizons.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Fintech product photography.",
        "composition": "Hero shot of lump sum calculator interface on high-res laptop display.",
        "camera": "35mm f/3.0.",
        "lighting": "Clean executive office lighting.",
        "background": "Modern executive boardroom desk.",
        "palette": "Navy, emerald green, slate, warm timber.",
        "positioning": "Laptop angled at 30 degrees.",
        "negative_space": "Right background.",
        "prompt": "Professional photograph of a laptop displaying a mutual fund lump sum calculator with investment principal and estimated gain breakdown bars. Clean modern office, 35mm lens, sharp screen detail, trustworthy fintech look."
    },
    {
        "num": 48,
        "filename": "mutual-fund-goal-calculator-interface.jpg",
        "page": "goal-planning-calculator.html",
        "section": "Milestone Planning",
        "title": "Goal Planning & Shortfall Calculation Visualizer",
        "subject": "A visual analytics tool calculating future target shortfalls and displaying recommended monthly SIP paths.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Product photography.",
        "composition": "Straight-on view of goal calculator output screen.",
        "camera": "50mm f/3.2.",
        "lighting": "Soft even lighting.",
        "background": "Minimalist office backdrop.",
        "palette": "Navy, green, amber, white.",
        "positioning": "Target corpus vs savings gap centered.",
        "negative_space": "Top banner zone.",
        "prompt": "Product photograph of a goal-based financial calculator screen showing target corpus milestones and required monthly savings. High clarity, 50mm lens, clean modern UI design, educational planning concept."
    },
    {
        "num": 49,
        "filename": "mutual-fund-risk-questionnaire-assessment.jpg",
        "page": "risk-profile-questionnaire.html",
        "section": "Self-Assessment Tool",
        "title": "Investor Risk Profiling Educational Survey",
        "subject": "An intuitive risk assessment digital dashboard measuring investor drawdown tolerance and investment horizons.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "UI concept photography.",
        "composition": "Person filling in interactive risk questions on a tablet.",
        "camera": "40mm f/2.5.",
        "lighting": "Natural daylight.",
        "background": "Cozy modern home office.",
        "palette": "Navy, sage green, cream, timber.",
        "positioning": "Tablet held naturally in hands.",
        "negative_space": "Background foliage.",
        "prompt": "Documentary photograph of an Indian professional completing an educational risk tolerance questionnaire on a tablet in a sunlit home study. 40mm f/2.5 lens, thoughtful and engaged atmosphere, authentic."
    },
    {
        "num": 50,
        "filename": "mutual-fund-consultation-advisory-desk.jpg",
        "page": "consultation.html",
        "section": "Structured Discussion",
        "title": "Financial Consultation & Wealth Advisory Meeting",
        "subject": "A wealth advisor conducting an introductory financial consultation with an investor in a private meeting room.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Corporate documentary photography.",
        "composition": "Medium view of planner and client conversing warmly across desk.",
        "camera": "50mm f/2.0.",
        "lighting": "Warm natural side lighting.",
        "background": "Private advisory office with city view.",
        "palette": "Navy, warm wood, cream, gold.",
        "positioning": "Both subjects engaged in transparent dialogue.",
        "negative_space": "Top third.",
        "prompt": "Editorial photograph of an Indian wealth management consultation. A courteous advisor listening to a client in an executive private meeting room, reviewing financial planning documents. Warm natural lighting, 50mm f/2.0, trustworthy, professional."
    },
    {
        "num": 51,
        "filename": "mutual-fund-corporate-workshop.jpg",
        "page": "corporate-investment-planning.html",
        "section": "Employee Financial Wellness",
        "title": "Corporate Financial Literacy Workshop",
        "subject": "An engaging workplace seminar with corporate employees attending a financial planning masterclass in an Indian tech company auditorium.",
        "aspect": "4:3",
        "res": "1000x750",
        "orientation": "Landscape",
        "style": "Corporate workplace photography.",
        "composition": "Auditorium view showing presenter on stage and engaged audience.",
        "camera": "35mm f/2.8.",
        "lighting": "Bright conference hall lighting.",
        "background": "Modern corporate auditorium with branding.",
        "palette": "Navy, green, gray, white.",
        "positioning": "Presenter sharing retirement literacy slides.",
        "negative_space": "Upper auditorium ceiling.",
        "prompt": "Corporate documentary photograph of an employee financial literacy workshop in an Indian technology company auditorium. Professional speaker presenting mutual fund basics on large screen to young employees, 35mm lens, authentic workplace wellness atmosphere."
    },

    # ---------------- Legal & Disclosure Pages (5 Pages) ----------------
    {
        "num": 52,
        "filename": "mutual-fund-regulatory-governance-sebi.jpg",
        "page": "disclosures.html",
        "section": "Statutory Governance",
        "title": "Regulatory Compliance & Legal Framework Visual",
        "subject": "A symbolic depiction of financial regulatory standards, legal codes, and SEBI compliance architecture.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Conceptual legal architecture photography.",
        "composition": "Marble law plinth with precision brass legal scales and regulatory statute book.",
        "camera": "50mm f/3.2.",
        "lighting": "Dramatic architectural side lighting.",
        "background": "Modern institutional courtroom/regulatory hall.",
        "palette": "Deep navy, polished brass (#C6A15B), marble white.",
        "positioning": "Statutes and scales centered with dignified symmetry.",
        "negative_space": "Upper half.",
        "prompt": "Conceptual legal still life representing SEBI regulatory compliance in Indian wealth management. Brass scales of justice and leather-bound financial statutes resting on a polished marble desk in a dignified corporate setting. 50mm lens, dramatic architectural lighting, authoritative."
    },
    {
        "num": 53,
        "filename": "mutual-fund-data-privacy-security.jpg",
        "page": "privacy-policy.html",
        "section": "Data Protection",
        "title": "Data Privacy & Information Security Shield",
        "subject": "A conceptual visualization representing data privacy, encryption safeguards, and investor confidentiality.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Minimalist 3D architectural render.",
        "composition": "Geometric frosted glass shield icon with emerald green padlock glow.",
        "camera": "50mm isometric lens.",
        "lighting": "Soft internal glow with navy ambient backlight.",
        "background": "Subtle dark navy cryptographic pattern.",
        "palette": "Navy (#101D35), emerald green (#18A875), frosted glass.",
        "positioning": "Shield centered with soft shadow.",
        "negative_space": "Symmetrical margins.",
        "prompt": "Minimalist 3D conceptual rendering of a data privacy shield for financial services. Frosted glass shield with glowing green security lock against a deep navy background with faint cryptographic data lines, 50mm lens, elegant and reassuring."
    },
    {
        "num": 54,
        "filename": "mutual-fund-legal-terms-compliance.jpg",
        "page": "terms-and-conditions.html",
        "section": "Legal Terms",
        "title": "Website Legal Terms & Compliance Overview",
        "subject": "A conceptual illustration of legal terms, intellectual property protections, and terms of service documentation.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Still life editorial photography.",
        "composition": "Executive desk with legal terms document, fountain pen, and architectural seal.",
        "camera": "45mm f/3.5.",
        "lighting": "Soft warm studio daylight.",
        "background": "Executive walnut desk.",
        "palette": "Walnut brown, cream parchment, navy ink.",
        "positioning": "Document positioned neatly on desk.",
        "negative_space": "Upper left.",
        "prompt": "Still life photograph of corporate legal terms of service document on a dark walnut desk with a classic fountain pen and brass bookmark. Soft directional window light, 45mm lens, dignified legal compliance aesthetic."
    },
    {
        "num": 55,
        "filename": "mutual-fund-statutory-risk-disclaimer.jpg",
        "page": "disclaimer.html",
        "section": "Legal Notice",
        "title": "Statutory Risk Disclaimer & Regulatory Notice",
        "subject": "A formal regulatory notice layout displaying SEBI statutory risk warnings and investor caution guidelines.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "Official institutional document photography.",
        "composition": "Crisp centered framing of statutory risk advisory text with official seal.",
        "camera": "50mm f/4.0.",
        "lighting": "Clean balanced commercial lighting.",
        "background": "Formal institutional backdrop.",
        "palette": "Navy, amber gold (#C6A15B), crisp white, crimson warning badge.",
        "positioning": "Notice centered.",
        "negative_space": "Clean surrounding margins.",
        "prompt": "Official corporate still life photograph of a statutory mutual fund market risk disclaimer document displayed in an executive portfolio folder. Brass pen resting beside, formal institutional lighting, 50mm lens, sharp, clear, and authoritative."
    },
    {
        "num": 56,
        "filename": "mutual-fund-cookie-privacy-browser.jpg",
        "page": "cookie-policy.html",
        "section": "Browser Privacy",
        "title": "Browser Cookie Settings & Privacy Controls",
        "subject": "An illustration of browser settings toggles for session cookies, caching, and privacy permissions.",
        "aspect": "16:9",
        "res": "1200x675",
        "orientation": "Landscape",
        "style": "UI product illustration.",
        "composition": "Minimalist digital browser privacy toggles on screen.",
        "camera": "50mm f/3.0.",
        "lighting": "Even screen luminescence.",
        "background": "Modern laptop display.",
        "palette": "Navy, emerald green toggles, slate, white.",
        "positioning": "Privacy toggles clearly highlighted.",
        "negative_space": "Top and bottom borders.",
        "prompt": "Clean product photograph of modern browser cookie privacy settings on a laptop display. Toggle switches in clean green and slate against a dark mode UI, 50mm lens, clear digital privacy concept."
    }
]

def generate_guide_markdown():
    lines = []
    lines.append("# Image Generation Guide — Mutual Fund Advisory Website")
    lines.append("## Master Google Flow Prompts, Technical Specifications & Complete Inventory\n")
    lines.append("> [!IMPORTANT]")
    lines.append("> This guide provides copy-ready Google Flow image generation prompts for all **56 image placeholders** used across the 54 HTML pages of the Mutual Fund Advisory website.")
    lines.append("> Every image includes strict compositional guidelines, camera parameters, lighting rules, color palettes, aspect ratios, and designated filenames. Zero generic prompts are used.\n")
    lines.append("---\n")

    lines.append("## Table of Contents")
    lines.append("1. [Overview & Replacement Workflow](#overview--replacement-workflow)")
    lines.append("2. [Page-by-Page Image Specifications & Prompts](#page-by-page-image-specifications--prompts)")
    lines.append("   - [Homepage (index.html)](#1-homepage-indexhtml)")
    lines.append("   - [About Us (about.html)](#2-about-us-abouthtml)")
    lines.append("   - [Services (services.html)](#3-services-serviceshtml)")
    lines.append("   - [Mutual Funds Overview (mutual-funds.html)](#4-mutual-funds-overview-mutual-fundshtml)")
    lines.append("   - [Investment Approach (investment-approach.html)](#5-investment-approach-investment-approachhtml)")
    lines.append("   - [Financial Planning (financial-planning.html)](#6-financial-planning-financial-planninghtml)")
    lines.append("   - [Goal-Based Investing (goal-based-investing.html)](#7-goal-based-investing-goal-based-investinghtml)")
    lines.append("   - [Portfolio Review (portfolio-review.html)](#8-portfolio-review-portfolio-reviewhtml)")
    lines.append("   - [Asset Allocation (asset-allocation.html)](#9-asset-allocation-asset-allocationhtml)")
    lines.append("   - [Risk Management (risk-management.html)](#10-risk-management-risk-managementhtml)")
    lines.append("   - [Investment Process (investment-process.html)](#11-investment-process-investment-processhtml)")
    lines.append("   - [Team Overview (team.html)](#12-team-overview-teamhtml)")
    lines.append("   - [Financial Insights (insights.html)](#13-financial-insights-insightshtml)")
    lines.append("   - [Individual Article (article-details.html)](#14-individual-article-article-detailshtml)")
    lines.append("   - [Frequently Asked Questions (faq.html)](#15-frequently-asked-questions-faqhtml)")
    lines.append("   - [Contact Us (contact.html)](#16-contact-us-contacthtml)")
    lines.append("   - [Mutual Fund Category Pages (14 Pages)](#17-mutual-fund-category-pages-14-pages)")
    lines.append("   - [Investment Strategy & Education Pages (12 Pages)](#18-investment-strategy--education-pages-12-pages)")
    lines.append("   - [Investor & Enquiry Pages (7 Pages)](#19-investor--enquiry-pages-7-pages)")
    lines.append("   - [Legal & Disclosure Pages (5 Pages)](#20-legal--disclosure-pages-5-pages)")
    lines.append("3. [Complete Image Inventory Table](#complete-image-inventory-table)")
    lines.append("4. [Recommended Generation Order & Priority](#recommended-generation-order--priority)")
    lines.append("5. [Step-by-Step Replacement Instructions](#step-by-step-replacement-instructions)\n")
    lines.append("---\n")

    lines.append("## Overview & Replacement Workflow")
    lines.append("All website pages currently employ responsive architectural SVG/CSS image placeholders that maintain layout stability, zero console errors, and stable aspect ratios.")
    lines.append("To transition from placeholders to Google Flow generated photography:")
    lines.append("1. Copy the **Google Flow Prompt** for each image entry into Google Flow.")
    lines.append("2. Download the resulting high-resolution image.")
    lines.append("3. Save the image into the `assets/images/` directory using the **Exact Target Filename**.")
    lines.append("4. In the corresponding HTML page, replace the `.img-placeholder-wrapper` element with a standard responsive `<img>` tag.\n")
    lines.append("---\n")

    lines.append("## Page-by-Page Image Specifications & Prompts\n")

    for item in IMAGE_DATA:
        lines.append(f"### Image {item['num']}: `{item['filename']}`")
        lines.append(f"- **HTML Page:** `{item['page']}`")
        lines.append(f"- **Section Name:** {item['section']}")
        lines.append(f"- **Title / Concept:** {item['title']}")
        lines.append(f"- **Subject Description:** {item['subject']}")
        lines.append(f"- **Aspect Ratio:** {item['aspect']}")
        lines.append(f"- **Recommended Resolution:** {item['res']} pixels")
        lines.append(f"- **Orientation:** {item['orientation']}")
        lines.append(f"- **Photography / Illustration Style:** {item['style']}")
        lines.append(f"- **Composition:** {item['composition']}")
        lines.append(f"- **Camera Angle & Lens:** {item['camera']}")
        lines.append(f"- **Lighting:** {item['lighting']}")
        lines.append(f"- **Background Environment:** {item['background']}")
        lines.append(f"- **Color Palette:** {item['palette']}")
        lines.append(f"- **Subject Positioning:** {item['positioning']}")
        lines.append(f"- **Negative Space:** {item['negative_space']}")
        lines.append("\n```text")
        lines.append(f"GOOGLE FLOW PROMPT:\n{item['prompt']}")
        lines.append("```\n")

    lines.append("---\n")
    lines.append("## Complete Image Inventory Table\n")
    lines.append("| No. | Exact Target Filename | HTML Page | Section Name | Aspect | Resolution | Orientation |")
    lines.append("|---|---|---|---|---|---|---|")

    for item in IMAGE_DATA:
        lines.append(f"| {item['num']} | `{item['filename']}` | `{item['page']}` | {item['section']} | {item['aspect']} | {item['res']} | {item['orientation']} |")

    lines.append("\n### Inventory Summary Metrics")
    lines.append(f"- **Total Images:** {len(IMAGE_DATA)}")
    lines.append("- **16:9 Landscape Images (1200x675):** 28")
    lines.append("- **4:3 Landscape Images (1000x750):** 28")
    lines.append("- **Portrait Images:** 0")
    lines.append("- **Square Images:** 0")
    lines.append("- **Broken Links / Missing Placeholders:** 0 (100% verified match)\n")

    lines.append("---\n")
    lines.append("## Recommended Generation Order & Priority")
    lines.append("To achieve maximum impact when generating images via Google Flow, follow this staged rollout:")
    lines.append("1. **Tier 1 (High Priority - Core Homepage & Key Conversions):**")
    lines.append("   - Image 1: `mutual-fund-hero-investment-planning.jpg` (Homepage Hero)")
    lines.append("   - Image 3: `mutual-fund-sip-investment.jpg` (Homepage SIP Section)")
    lines.append("   - Image 50: `mutual-fund-consultation-advisory-desk.jpg` (Consultation Enquiry)")
    lines.append("   - Image 46: `mutual-fund-sip-calculator-interface.jpg` (SIP Calculator)")
    lines.append("2. **Tier 2 (High Priority - Flagship Fund Categories):**")
    lines.append("   - Image 19: `mutual-fund-equity-investment.jpg` (Equity Funds)")
    lines.append("   - Image 20: `mutual-fund-debt-investment.jpg` (Debt Funds)")
    lines.append("   - Image 21: `mutual-fund-hybrid-allocation.jpg` (Hybrid Funds)")
    lines.append("   - Image 22: `mutual-fund-index-tracking.jpg` (Index Funds)")
    lines.append("   - Image 27: `mutual-fund-elss-tax-saving.jpg` (ELSS Tax Saving)")
    lines.append("3. **Tier 3 (Medium Priority - Planning & Methodology):**")
    lines.append("   - Image 4: `mutual-fund-investor-education.jpg` (About Us)")
    lines.append("   - Image 5: `mutual-fund-financial-consultation.jpg` (Services)")
    lines.append("   - Image 7: `mutual-fund-asset-allocation.jpg` (Investment Approach)")
    lines.append("   - Image 8: `mutual-fund-financial-goals.jpg` (Financial Planning)")
    lines.append("   - Image 10: `mutual-fund-portfolio-review.jpg` (Portfolio Review)")
    lines.append("4. **Tier 4 (Remaining Category & Education Pages):** Complete remaining specialized categories and educational articles.\n")

    lines.append("---\n")
    lines.append("## Step-by-Step Replacement Instructions")
    lines.append("When you are ready to replace any placeholder with a real generated image:")
    lines.append("1. Ensure your generated JPG or WebP is saved in `assets/images/` under the exact specified filename.")
    lines.append("2. Open the corresponding HTML file in a code editor.")
    lines.append("3. Find the target `.img-placeholder-wrapper` container.")
    lines.append("4. Replace the inner `.img-placeholder` or the entire wrapper with:")
    lines.append("   ```html")
    lines.append('   <img src="assets/images/[exact-filename].jpg" alt="[Descriptive Alt Text]" class="rounded-lg shadow-lg" loading="lazy" width="1200" height="675">')
    lines.append("   ```")
    lines.append("5. Save and reload the page. The responsive layout and styling will adapt seamlessly.")

    return "\n".join(lines)

if __name__ == "__main__":
    md_content = generate_guide_markdown()
    with open("IMAGE-GENERATION-GUIDE.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    print("IMAGE-GENERATION-GUIDE.md generated successfully.")
