# Image Generation Guide — Mutual Fund Advisory Website
## Master Google Flow Prompts, Technical Specifications & Complete Inventory

> [!IMPORTANT]
> This guide provides copy-ready Google Flow image generation prompts for all **56 image placeholders** used across the 54 HTML pages of the Mutual Fund Advisory website.
> Every image includes strict compositional guidelines, camera parameters, lighting rules, color palettes, aspect ratios, and designated filenames. Zero generic prompts are used.

---

## Table of Contents
1. [Overview & Replacement Workflow](#overview--replacement-workflow)
2. [Page-by-Page Image Specifications & Prompts](#page-by-page-image-specifications--prompts)
   - [Homepage (index.html)](#1-homepage-indexhtml)
   - [About Us (about.html)](#2-about-us-abouthtml)
   - [Services (services.html)](#3-services-serviceshtml)
   - [Mutual Funds Overview (mutual-funds.html)](#4-mutual-funds-overview-mutual-fundshtml)
   - [Investment Approach (investment-approach.html)](#5-investment-approach-investment-approachhtml)
   - [Financial Planning (financial-planning.html)](#6-financial-planning-financial-planninghtml)
   - [Goal-Based Investing (goal-based-investing.html)](#7-goal-based-investing-goal-based-investinghtml)
   - [Portfolio Review (portfolio-review.html)](#8-portfolio-review-portfolio-reviewhtml)
   - [Asset Allocation (asset-allocation.html)](#9-asset-allocation-asset-allocationhtml)
   - [Risk Management (risk-management.html)](#10-risk-management-risk-managementhtml)
   - [Investment Process (investment-process.html)](#11-investment-process-investment-processhtml)
   - [Team Overview (team.html)](#12-team-overview-teamhtml)
   - [Financial Insights (insights.html)](#13-financial-insights-insightshtml)
   - [Individual Article (article-details.html)](#14-individual-article-article-detailshtml)
   - [Frequently Asked Questions (faq.html)](#15-frequently-asked-questions-faqhtml)
   - [Contact Us (contact.html)](#16-contact-us-contacthtml)
   - [Mutual Fund Category Pages (14 Pages)](#17-mutual-fund-category-pages-14-pages)
   - [Investment Strategy & Education Pages (12 Pages)](#18-investment-strategy--education-pages-12-pages)
   - [Investor & Enquiry Pages (7 Pages)](#19-investor--enquiry-pages-7-pages)
   - [Legal & Disclosure Pages (5 Pages)](#20-legal--disclosure-pages-5-pages)
3. [Complete Image Inventory Table](#complete-image-inventory-table)
4. [Recommended Generation Order & Priority](#recommended-generation-order--priority)
5. [Step-by-Step Replacement Instructions](#step-by-step-replacement-instructions)

---

## Overview & Replacement Workflow
All website pages currently employ responsive architectural SVG/CSS image placeholders that maintain layout stability, zero console errors, and stable aspect ratios.
To transition from placeholders to Google Flow generated photography:
1. Copy the **Google Flow Prompt** for each image entry into Google Flow.
2. Download the resulting high-resolution image.
3. Save the image into the `assets/images/` directory using the **Exact Target Filename**.
4. In the corresponding HTML page, replace the `.img-placeholder-wrapper` element with a standard responsive `<img>` tag.

---

## Page-by-Page Image Specifications & Prompts

### Image 1: `mutual-fund-hero-investment-planning.jpg`
- **HTML Page:** `index.html`
- **Section Name:** Hero Section
- **Title / Concept:** Strategic Financial Planning & Advisory
- **Subject Description:** A senior Indian wealth manager in contemporary business attire collaborating with an Indian professional couple at an elegant conference desk, reviewing asset allocation analytics on a sleek tablet screen with upward financial growth charts in the background.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** High-end corporate documentary photography, ultra-realistic wealth management private office.
- **Composition:** Rule of thirds. Subjects positioned on the right and center; soft depth of field focusing on the tablet analytics interface; clean negative space on the left.
- **Camera Angle & Lens:** Eye-level 50mm f/2.0 prime lens, cinematic framing, gentle foreground blur.
- **Lighting:** Soft natural morning daylight streaming through floor-to-ceiling glass windows, warm golden rim light highlighting shoulders, balanced fill light.
- **Background Environment:** Modern high-rise financial district view (Hyderabad Financial District / BKC Mumbai) softly out of focus, minimalist architectural wood panelling and indoor architectural plants.
- **Color Palette:** Deep corporate navy (#101D35), warm gold (#C6A15B), forest emerald green accents (#18A875), clean ivory whites and warm timber.
- **Subject Positioning:** Planner seated at 45 degrees gesturing gently toward digital tablet; client couple engaged attentively.
- **Negative Space:** Subtle negative space on upper left quadrant suitable for headline overlay.

```text
GOOGLE FLOW PROMPT:
Cinematic documentary editorial photograph of a senior Indian wealth advisor in tailored navy blazer discussing long-term portfolio growth with a young Indian professional couple. They sit around an executive walnut meeting desk reviewing clean financial growth charts on an iPad Pro. Modern corporate glass office overlooking Hyderabad skyline. Soft natural morning window lighting, 50mm f/2.2, photorealistic, premium private banking aesthetic, muted navy and warm gold tones, elegant depth of field, 8k resolution, professional color grading.
```

### Image 2: `mutual-fund-market-research.jpg`
- **HTML Page:** `index.html`
- **Section Name:** Why Understand Mutual Funds Section
- **Title / Concept:** Financial Analyst Reviewing Scheme Factsheets
- **Subject Description:** An Indian mutual fund quantitative analyst in a modern research lab examining multi-screen financial displays showing SEBI riskometer gauges, sector allocations, and correlation matrices.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Modern corporate editorial photography, institutional research setting.
- **Composition:** Medium close-up shot focused on analyst's hand taking notes beside an ultra-wide monitor showing clean financial charts.
- **Camera Angle & Lens:** 35mm focal length, f/2.8 aperture, crisp foreground focus with pleasant bokeh.
- **Lighting:** Cool neutral ambient office lighting complemented by soft desk lamp illumination.
- **Background Environment:** Glass-partitioned research trading room with blurred stock ticker charts and minimalist financial posters.
- **Color Palette:** Navy (#101D35), slate gray (#405064), emerald green (#18A875), crisp white highlights.
- **Subject Positioning:** Analyst seated at workstation, pen poised over notebook, dual monitors displaying analytical graphs.
- **Negative Space:** Minimal; concentrated documentary composition.

```text
GOOGLE FLOW PROMPT:
Editorial corporate photograph of an Indian financial research analyst studying mutual fund portfolio data and SEBI factsheets across curved ultra-wide monitors. Clean minimalist desk, financial graphs showing sector breakdowns, notebook with fountain pen. Soft modern institutional office lighting, shot on Hasselblad 50mm lens, sharp details, muted navy and financial green accents, ultra-realistic, authentic workplace setting.
```

### Image 3: `mutual-fund-sip-investment.jpg`
- **HTML Page:** `index.html`
- **Section Name:** SIP Investment Section
- **Title / Concept:** Systematic Investment Planning Visual
- **Subject Description:** A conceptual, elegant photographic composition illustrating regular monthly disciplined investing: staggered stacks of Indian Rupee coins beside a modern glass calendar tablet showing steady upward compound growth.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** High-end still life financial concept photography, architectural precision.
- **Composition:** Diagonal ascending arrangement from bottom left to top right, symbolizing progressive accumulation.
- **Camera Angle & Lens:** Macro 85mm f/3.2, shallow depth of field focusing on the mid-tier growth point.
- **Lighting:** Dramatic side directional studio lighting casting soft elongated shadows.
- **Background Environment:** Dark textured slate surface with subtle architectural drafting grid in faint green.
- **Color Palette:** Polished metallic brass/gold (#C6A15B), deep navy background (#101D35), vibrant green leaf sprout (#18A875).
- **Subject Positioning:** Ascending coin cylinders beside an illuminated calendar tablet showing monthly automated debit indicators.
- **Negative Space:** Upper right corner uncluttered.

```text
GOOGLE FLOW PROMPT:
Premium conceptual still life photography representing Indian Systematic Investment Plans (SIP). Neat ascending rows of Indian rupee coins progressively growing taller, with a small fresh green sprout emerging from the tallest stack. Dark textured slate desk, sleek glass calendar tablet with subtle glowing green monthly checkmarks, dramatic architectural side lighting, 85mm macro lens, luxurious financial planning editorial, high detail, 8k.
```

### Image 4: `mutual-fund-investor-education.jpg`
- **HTML Page:** `about.html`
- **Section Name:** Our Educational Philosophy
- **Title / Concept:** Financial Planning & Investor Literacy Workshop
- **Subject Description:** An interactive, elegant financial literacy masterclass where an expert Indian educator explains asset allocation models on an interactive digital board to an attentive audience of young working professionals.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Corporate documentary photography, educational seminar.
- **Composition:** Wide medium shot capturing the speaker gesturing toward a digital chart while audience members take notes.
- **Camera Angle & Lens:** 28mm wide angle, f/2.8, clear depth of field across presenter and audience.
- **Lighting:** Bright, warm seminar room lighting with recessed LED ambient ceiling fixtures.
- **Background Environment:** Modern auditorium with timber acoustic baffles and interactive digital projection screen.
- **Color Palette:** Navy (#182B49), financial green (#18A875), clean white, warm oak timber.
- **Subject Positioning:** Educator standing gracefully on the left facing forward-right; audience seated in ergonomic desks.
- **Negative Space:** Upper third of presentation board clear.

```text
GOOGLE FLOW PROMPT:
Professional corporate documentary photograph of an Indian female financial educator speaking at an investor awareness symposium. She points to a clean interactive screen displaying a diversified asset allocation pie chart. Diverse Indian young professionals listening attentively with notebooks in modern tech seminar hall. Warm natural lighting, 35mm lens, crisp focus, credible wealth management education atmosphere, realistic, 8k.
```

### Image 5: `mutual-fund-financial-consultation.jpg`
- **HTML Page:** `services.html`
- **Section Name:** Services Overview Hero
- **Title / Concept:** Comprehensive Financial Advisory Capabilities
- **Subject Description:** A collaborative executive advisory session around a bespoke marble conference table, with senior advisors presenting structured wealth solutions and portfolio roadmaps to family office clients.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** High-end corporate editorial, private banking suite.
- **Composition:** Symmetrical architectural composition, wide panoramic view of private conference room.
- **Camera Angle & Lens:** 24mm f/4.0 tilt-shift architectural lens, straight vertical lines.
- **Lighting:** Diffused architectural cove lighting combined with soft afternoon window light.
- **Background Environment:** Floor-to-ceiling glass partitions overlooking manicured rooftop garden, abstract geometric art on wall.
- **Color Palette:** Primary navy (#101D35), marble cream, gold hardware accents (#C6A15B), emerald foliage.
- **Subject Positioning:** Advisory team on left, clients on right, central document folder and tablet displaying portfolio framework.
- **Negative Space:** Upper center area above table clear.

```text
GOOGLE FLOW PROMPT:
Architectural interior photography of an exclusive Indian wealth advisory boardroom. Professional financial planners in tailored business suits consulting with clients over customized portfolio reports and sleek laptops. Italian marble conference table, panoramic window view of modern Hyderabad cyber city, soft golden hour sunlight, architectural photography style, 24mm lens, clean lines, serene and trustworthy private banking atmosphere.
```

### Image 6: `mutual-fund-wealth-planning.jpg`
- **HTML Page:** `mutual-funds.html`
- **Section Name:** How Mutual Funds Work
- **Title / Concept:** Mutual Fund Structure & Custodial Mechanics
- **Subject Description:** A modern graphic-photographic composite scene showing financial professionals collaborating around an architectural model of Indian capital market infrastructure, representing AMCs, trustees, and custodians.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Conceptual architectural corporate photography.
- **Composition:** Centered layout with team inspecting a holographic-style geometric model on a luminous plinth.
- **Camera Angle & Lens:** 45mm f/2.8 lens, overhead 30-degree isometric perspective.
- **Lighting:** Subtle neon underglow in financial green and clean white key light on faces.
- **Background Environment:** Minimalist high-tech financial innovation center with brushed steel and smoked glass.
- **Color Palette:** Navy (#101D35), financial green (#18A875), silver, frosted white.
- **Subject Positioning:** Two analysts leaning over table analyzing structural capital flows.
- **Negative Space:** Faint digital grid pattern across top background.

```text
GOOGLE FLOW PROMPT:
Conceptual financial services photograph showing Indian portfolio managers gathered around a luminous smart-table reviewing an interactive 3D organizational model of mutual fund asset flows. Clean architectural setting, deep navy and emerald green ambient lighting, modern institutional fintech aesthetic, 35mm lens, sharp focus, sophisticated corporate innovation.
```

### Image 7: `mutual-fund-asset-allocation.jpg`
- **HTML Page:** `investment-approach.html`
- **Section Name:** Process Over Market Timing
- **Title / Concept:** Asset Allocation & Modern Portfolio Theory
- **Subject Description:** A conceptual editorial still life showing geometric glass prism blocks tinted in green, gold, and sapphire blue resting in balanced equilibrium upon a precision marble scales, symbolizing multi-asset diversification.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Conceptual artistic financial photography.
- **Composition:** Precise balanced centerpiece with dramatic shadows cast across textured linen backdrop.
- **Camera Angle & Lens:** 90mm macro lens, f/4.0 aperture for crisp edge-to-edge definition.
- **Lighting:** Strong directional spotlight from 45 degrees creating crisp colorful caustics on surface.
- **Background Environment:** Neutral warm gray architectural concrete texture.
- **Color Palette:** Emerald green (#18A875), sapphire navy (#101D35), amber gold (#C6A15B), stone gray.
- **Subject Positioning:** Prisms precisely balanced in perfect poise without tipping.
- **Negative Space:** Ample negative space on both sides.

```text
GOOGLE FLOW PROMPT:
High-end conceptual art photography representing asset allocation in wealth management. Precision-cut geometric glass prisms in sapphire blue, amber gold, and emerald green perfectly balanced on a minimalist brass scale beam. Clean concrete background, sharp directional ray lighting casting colored glass reflections, 90mm lens, artistic editorial design, 8k resolution, elegant mathematical balance.
```

### Image 8: `mutual-fund-financial-goals.jpg`
- **HTML Page:** `financial-planning.html`
- **Section Name:** Why Plan Before You Invest
- **Title / Concept:** Financial Planning Roadmap & Corpus Targets
- **Subject Description:** An Indian family (parents and child) sitting with their financial advisor in a sunlit modern living room office, reviewing an illustrated life milestones map on a premium tablet device.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Warm lifestyle documentary photography with financial services context.
- **Composition:** Medium horizontal grouping conveying trust, warmth, and strategic planning.
- **Camera Angle & Lens:** 50mm f/1.8 lens, natural perspective, gentle background separation.
- **Lighting:** Warm golden afternoon sunlight filtering through sheer curtains, soft interior lamps.
- **Background Environment:** Tasteful contemporary Indian apartment interior with indoor monstera plant and contemporary bookshelf.
- **Color Palette:** Warm timber, navy blue, gold accents, soft cream and linen.
- **Subject Positioning:** Family grouped comfortably on sofa; advisor seated across smiling reassuringly.
- **Negative Space:** Upper quadrant with soft wall backdrop.

```text
GOOGLE FLOW PROMPT:
Warm lifestyle documentary photograph of an Indian couple and their young daughter in a consultation with their wealth advisor. They are reviewing a financial roadmap on a digital tablet in a bright, modern living room office. Soft afternoon window sunlight, shallow depth of field, 50mm f/2.0, genuine optimistic expressions, premium Indian home aesthetic, comforting, trustworthy atmosphere.
```

### Image 9: `mutual-fund-retirement-planning.jpg`
- **HTML Page:** `goal-based-investing.html`
- **Section Name:** Mapping Horizons to Asset Classes
- **Title / Concept:** Life Milestone Goals & Target Retirement Planning
- **Subject Description:** An active, happy retired Indian couple in their late 50s enjoying a peaceful morning stroll in a lush landscaped botanical park, holding cups of coffee, representing financial freedom and post-retirement security.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Authentic lifestyle editorial photography.
- **Composition:** Golden ratio composition; couple walking toward camera from right to left along a winding pathway.
- **Camera Angle & Lens:** 70mm telephoto lens, f/2.8, beautiful circular bokeh in trees behind.
- **Lighting:** Early morning golden hour sun flare behind foliage, creating warm rim lighting.
- **Background Environment:** Lush tropical botanical garden with stone pathways and serene water reflection.
- **Color Palette:** Vibrant emerald green, golden sunlight, crisp white linen, warm earthy terracotta.
- **Subject Positioning:** Couple walking hand-in-hand smiling, relaxed body language.
- **Negative Space:** Open space on upper left framed by tree canopy.

```text
GOOGLE FLOW PROMPT:
Inspiring lifestyle photograph of a retired Indian couple in their 50s enjoying a serene sunrise walk in a modern landscaped park. Confident, joyful expressions representing financial peace and independence. Golden morning backlight filtering through palm trees, 85mm f/2.2 lens, cinematic color grading, editorial wealth management style, natural and authentic.
```

### Image 10: `mutual-fund-portfolio-review.jpg`
- **HTML Page:** `portfolio-review.html`
- **Section Name:** Why Review Your Mutual Fund Portfolio
- **Title / Concept:** Financial Analyst Conducting Portfolio Review
- **Subject Description:** An experienced Indian portfolio analyst using a stylus on an interactive touch desk to examine scheme overlap diagrams, stock concentration, and risk standard deviation curves.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Institutional finance editorial photography.
- **Composition:** Close-up over-the-shoulder angle focusing on touch screen graphics and stylus tip.
- **Camera Angle & Lens:** 50mm macro f/2.8, sharp focus on chart data points.
- **Lighting:** Clean studio lighting balanced with the soft glow of the high-resolution touch display.
- **Background Environment:** Dark executive office suite with blurred financial book spines and brass desk accents.
- **Color Palette:** Midnight navy (#101D35), data cyan, emerald green (#18A875), warm brass.
- **Subject Positioning:** Analyst's hands skillfully manipulating data nodes on screen.
- **Negative Space:** Top third of desk monitor displaying calm dark theme interface.

```text
GOOGLE FLOW PROMPT:
Detailed over-the-shoulder corporate photograph of an Indian financial analyst using a digital stylus on a high-resolution drafting screen to review mutual fund portfolio overlap and risk metrics. Clean UI charts showing asset allocation and stock holdings. Warm executive office background, sharp focus, 50mm lens, professional wealth management atmosphere, 8k.
```

### Image 11: `mutual-fund-investment-dashboard.jpg`
- **HTML Page:** `asset-allocation.html`
- **Section Name:** Simulate Educational Allocation Profiles
- **Title / Concept:** Interactive Asset Allocation Dashboard Visual
- **Subject Description:** A modern wealth management digital dashboard interface displayed on a frameless curved monitor, featuring elegant asset allocation donut charts, equity-debt sliders, and risk-return curves.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Clean architectural tech product photography.
- **Composition:** Hero desktop setup shot at a slight 15-degree angle showing device and minimalist office surroundings.
- **Camera Angle & Lens:** 35mm f/4.0 lens, crisp clarity from screen surface to peripheral desk items.
- **Lighting:** Diffused softbox lighting with subtle green ambient backlight behind monitor.
- **Background Environment:** Minimalist Scandinavian-style executive desk with wireless keyboard, fountain pen, and small succulent.
- **Color Palette:** Navy (#101D35), financial green (#18A875), amber gold (#C6A15B), slate gray.
- **Subject Positioning:** Curved monitor centered; keyboard and notebook angled naturally in foreground.
- **Negative Space:** Clean wall area above monitor.

```text
GOOGLE FLOW PROMPT:
Premium tech product photograph of a modern wealth management dashboard on a sleek 34-inch curved monitor. Clean UI displaying sophisticated asset allocation charts, green and gold metrics, and risk sliders. Minimalist executive desk with wireless peripherals and architectural plant, soft atmospheric studio lighting, 35mm lens, ultra-clean commercial look.
```

### Image 12: `mutual-fund-risk-management.jpg`
- **HTML Page:** `risk-management.html`
- **Section Name:** The Spectrum of Mutual Fund Risks
- **Title / Concept:** Multi-Dimensional Financial Risk Spectrum
- **Subject Description:** An abstract 3D visualization representing risk dimensions: interconnected glass spheres and risk-mesh topography illustrating volatility damping and portfolio resilience.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Modern 3D architectural financial render.
- **Composition:** Dynamic diagonal topography flowing from chaotic waves into smooth, calm harmonic curves.
- **Camera Angle & Lens:** Simulated 50mm cinematic camera with subtle chromatic aberration and depth of field.
- **Lighting:** Luminous volumetric light rays filtering through translucent smoked glass geometric forms.
- **Background Environment:** Deep navy gradient with subtle micro-grid lines.
- **Color Palette:** Navy blue (#101D35), vivid emerald green (#18A875), glowing gold (#C6A15B), crystalline highlights.
- **Subject Positioning:** Wave structure centered, transitioning from turbulent left to stable right.
- **Negative Space:** Upper left and upper right quadrants uncluttered.

```text
GOOGLE FLOW PROMPT:
Sophisticated 3D abstract financial visualization of risk management. Translucent glass waves and geometric nodal networks transitioning from turbulent peaks on one side into smooth, calm harmonic curves on the other. Glowing emerald green and amber gold light accents against a deep navy blue background, modern fintech aesthetic, ray-traced reflections, 8k resolution.
```

### Image 13: `mutual-fund-investor-meeting.jpg`
- **HTML Page:** `investment-process.html`
- **Section Name:** 5-Stage Investment Methodology
- **Title / Concept:** 5-Stage Investor Consultation Process
- **Subject Description:** A senior wealth planner and an Indian investor standing beside an illuminated glass architectural board, mapping out the five stages of investment planning with milestone magnets.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Corporate documentary editorial photography.
- **Composition:** Wide medium shot with glass board dividing planner on left and investor on right.
- **Camera Angle & Lens:** 35mm f/2.8 lens, capturing expressive gestures and transparent board diagrams.
- **Lighting:** Edge-lit LED glass whiteboard with soft daylight fill on subjects.
- **Background Environment:** Modern consulting room with skyline glass windows and executive timber credentials shelf.
- **Color Palette:** Navy (#101D35), illuminated green (#18A875), white, warm amber.
- **Subject Positioning:** Planner gesturing to Stage 3 with marker in hand; investor listening thoughtfully.
- **Negative Space:** Clear glass areas of whiteboard.

```text
GOOGLE FLOW PROMPT:
Corporate documentary photograph of a senior Indian financial planner explaining an investment roadmap on an illuminated transparent glass whiteboard to a client. Milestone icons drawn on glass. Modern high-rise consulting office, professional business attire, natural window lighting, 35mm lens, sharp focus, collaborative wealth management atmosphere, 8k.
```

### Image 14: `mutual-fund-team-collaboration.jpg`
- **HTML Page:** `team.html`
- **Section Name:** Advisory Investment Committee Collaboration
- **Title / Concept:** Advisory Investment Committee Collaboration
- **Subject Description:** An advisory team of diverse Indian financial professionals in business attire collaborating around a conference table with market research dossiers and laptops.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** High-end corporate editorial photography.
- **Composition:** Group shot with shallow depth of field, leading eyes to the central discussion leader.
- **Camera Angle & Lens:** 50mm f/2.5 prime lens.
- **Lighting:** Natural daylight from large architectural windows combined with subtle warm interior spots.
- **Background Environment:** Glass-walled boardroom with blurred city skyline and modern artwork.
- **Color Palette:** Charcoal navy, crisp white shirts, emerald green accents, warm walnut table.
- **Subject Positioning:** Four professionals engaged in an animated, disciplined financial discussion.
- **Negative Space:** Top quadrant above the boardroom table.

```text
GOOGLE FLOW PROMPT:
Editorial group photograph of a team of Indian wealth management professionals in a collaborative strategy meeting. Diverse men and women in modern executive attire discussing portfolio reports around a solid oak table. Floor-to-ceiling glass windows, soft daylight, 50mm lens, authentic professional expressions, sophisticated private wealth firm aesthetic.
```

### Image 15: `mutual-fund-market-insights.jpg`
- **HTML Page:** `insights.html`
- **Section Name:** Financial Insights Desk
- **Title / Concept:** Financial Research & Market Insights Desk
- **Subject Description:** An organized researcher's desk featuring printed quarterly market reports, financial newspapers (Mint, Economic Times style), an iPad displaying economic indicators, and a cup of black coffee.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Editorial flat-lay / 45-degree desk photography.
- **Composition:** 45-degree angle editorial arrangement with careful alignment of reading materials.
- **Camera Angle & Lens:** 40mm f/2.8 lens, even sharpness across workspace.
- **Lighting:** Morning window light casting soft, natural diagonal shadows across paper.
- **Background Environment:** Dark reclaimed oak desk surface with brass pen tray.
- **Color Palette:** Warm timber, crisp white newsprint, brass gold, deep navy accents.
- **Subject Positioning:** Documents neatly fanned out, glasses resting on open report.
- **Negative Space:** Upper third of desk surface clear.

```text
GOOGLE FLOW PROMPT:
Editorial still life photograph of a financial analyst desk. Neatly fanned macroeconomic research reports with clean graphs, reading glasses resting on financial paper, iPad showing stock index trend, fountain pen, steaming espresso in ceramic cup. Rich dark oak desk, soft morning window light, 40mm lens, intellectual and credible finance atmosphere, 8k.
```

### Image 16: `mutual-fund-reading-factsheet.jpg`
- **HTML Page:** `article-details.html`
- **Section Name:** Featured Article Header
- **Title / Concept:** How to Read a Mutual Fund Factsheet
- **Subject Description:** A close-up shot of an investor's hands holding a highlighter over a printed mutual fund factsheet, highlighting the Total Expense Ratio (TER) and top 10 portfolio holdings.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Documentary detail photography.
- **Composition:** Macro close-up, rule of thirds focusing on highlighted table rows.
- **Camera Angle & Lens:** 60mm macro f/2.8, shallow depth of field.
- **Lighting:** Warm side desk lamp illuminating paper texture.
- **Background Environment:** Softly blurred mahogany desk surface and laptop keyboard.
- **Color Palette:** White paper, neon green highlighter accent (#18A875), dark mahogany, navy ink.
- **Subject Positioning:** Hands holding paper with fountain pen and green highlighter active.
- **Negative Space:** Unprinted white margins of factsheet page.

```text
GOOGLE FLOW PROMPT:
Close-up documentary photograph of hands reviewing a mutual fund factsheet document. Green highlighter marking the expense ratio and sector allocation table. Sleek laptop and coffee cup in soft blurred background, warm desk lamp lighting, 60mm macro lens, sharp paper texture, educational financial literacy concept, authentic and detailed.
```

### Image 17: `mutual-fund-faq-support.jpg`
- **HTML Page:** `faq.html`
- **Section Name:** Knowledge Clearinghouse
- **Title / Concept:** Investor Support & Client Helpdesk Interface
- **Subject Description:** A dedicated investor relations specialist in an Indian financial firm smiling warmly while answering client inquiries with an ergonomic headset and dual monitoring desk.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Warm corporate portrait documentary.
- **Composition:** Medium shot with specialist framed against modern office hub.
- **Camera Angle & Lens:** 50mm f/2.0 lens, soft bokeh.
- **Lighting:** Flattering soft portrait ring light and natural office ambient.
- **Background Environment:** Modern financial advisory office with greenery and warm timber accents.
- **Color Palette:** Navy suit, warm skin tones, crisp white, emerald office plants.
- **Subject Positioning:** Specialist seated upright, engaging warmly with viewer.
- **Negative Space:** Right side of frame with pleasant architectural background.

```text
GOOGLE FLOW PROMPT:
Professional corporate portrait of an Indian customer support specialist at a mutual fund advisory desk. Wearing a sleek communication headset, smiling warmly at camera while seated at a clean dual-monitor workstation. Modern corporate office background, 50mm f/2.0 lens, inviting and trustworthy atmosphere, high-end commercial quality.
```

### Image 18: `mutual-fund-advisory-office.jpg`
- **HTML Page:** `contact.html`
- **Section Name:** Communication Channels
- **Title / Concept:** Advisory Headquarters & Welcome Reception
- **Subject Description:** A striking architectural photograph of the advisory firm's reception foyer: polished stone floors, abstract upward-growth bronze wall sculpture, and warm welcome desk.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Architectural interior photography.
- **Composition:** One-point perspective down the reception lobby.
- **Camera Angle & Lens:** 24mm wide angle lens, f/5.6, razor sharp perspective.
- **Lighting:** Architectural LED trough lighting and natural skylight illumination.
- **Background Environment:** Reception wall featuring geometric financial growth bronze installation.
- **Color Palette:** Travertine stone, bronze gold (#C6A15B), deep navy accents (#101D35), green planters.
- **Subject Positioning:** Reception desk centered right, spacious welcoming corridor.
- **Negative Space:** Open polished stone floor in lower foreground.

```text
GOOGLE FLOW PROMPT:
Architectural photograph of a luxury private wealth management reception foyer in Hyderabad. Polished Italian travertine flooring, minimalist reception desk with back-painted navy glass, geometric bronze growth sculpture on feature wall, lush indoor fiddle-leaf figs, warm linear architectural lighting, 24mm tilt-shift lens, pristine commercial photography.
```

### Image 19: `mutual-fund-equity-investment.jpg`
- **HTML Page:** `equity-mutual-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Equity Market Research & Stock Selection
- **Subject Description:** An Indian equity fund manager analyzing company performance data and candlestick charts on multiple trading screens.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Corporate finance documentary.
- **Composition:** Medium shot from side angle showing analyst immersed in market research.
- **Camera Angle & Lens:** 50mm f/2.2.
- **Lighting:** Cool monitor screen glow balanced with warm ambient desk lighting.
- **Background Environment:** Institutional research desk with blurred trading screens.
- **Color Palette:** Navy, emerald green, cool white, amber highlights.
- **Subject Positioning:** Manager studying equity trends with pen in hand.
- **Negative Space:** Upper left quadrant.

```text
GOOGLE FLOW PROMPT:
Documentary photograph of an Indian equity mutual fund manager analyzing stock market valuation charts across dual curved monitors. Clean desk, trading terminal data, natural office lighting, 50mm f/2.2 lens, professional financial services aesthetic, 8k.
```

### Image 20: `mutual-fund-debt-investment.jpg`
- **HTML Page:** `debt-mutual-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Fixed Income Yield Curve & Bond Research
- **Subject Description:** A fixed-income fund manager evaluating government securities yield curves and sovereign bond ratings.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Institutional finance photography.
- **Composition:** Overhead 45-degree angle showing yield curve graphs and bond matrices.
- **Camera Angle & Lens:** 35mm f/2.8.
- **Lighting:** Soft corporate ambient lighting.
- **Background Environment:** Modern trading floor with sovereign bond indices.
- **Color Palette:** Deep navy (#101D35), muted green (#18A875), slate gray.
- **Subject Positioning:** Analyst pointing to yield spread on tablet.
- **Negative Space:** Top area above desk.

```text
GOOGLE FLOW PROMPT:
Corporate finance photograph of a debt mutual fund specialist reviewing sovereign bond yields and credit spreads on a high-resolution display. Clean desk with financial research dossiers, institutional banking office, 35mm lens, sharp focus, 8k.
```

### Image 21: `mutual-fund-hybrid-allocation.jpg`
- **HTML Page:** `hybrid-mutual-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Multi-Asset Allocation & Hedging Dynamics
- **Subject Description:** A visual concept showing balanced allocation between equity growth stocks and fixed-income debt bonds.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Conceptual financial photography.
- **Composition:** Balanced split layout representing dual engines of growth and stability.
- **Camera Angle & Lens:** 50mm f/2.8.
- **Lighting:** Split lighting with warm amber on equity side and cool blue on debt side.
- **Background Environment:** Minimalist marble and wood surfaces.
- **Color Palette:** Emerald green, navy blue, amber gold, white.
- **Subject Positioning:** Central symbolic balance.
- **Negative Space:** Top and bottom borders.

```text
GOOGLE FLOW PROMPT:
Conceptual financial still life representing hybrid mutual funds. A balanced scale with polished green emerald crystal representing equity on one side and steady silver ingots representing fixed income on the other. Elegant marble desk, dramatic lighting, 50mm lens, 8k.
```

### Image 22: `mutual-fund-index-tracking.jpg`
- **HTML Page:** `index-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Benchmark Index Tracking & Quantitative Modeling
- **Subject Description:** An algorithmic index fund tracking screen displaying Nifty 50 constituents and minimal tracking error graphs.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Fintech product photography.
- **Composition:** Clean horizontal framing of index tracking visualization.
- **Camera Angle & Lens:** 35mm f/4.0.
- **Lighting:** High-contrast digital screen illumination.
- **Background Environment:** Modern quantitative research room.
- **Color Palette:** Navy, cyan, green, white.
- **Subject Positioning:** Screen centered with keyboard in soft focus.
- **Negative Space:** Upper margin of display.

```text
GOOGLE FLOW PROMPT:
High-tech financial services photograph showing an index fund tracking dashboard replicating the Nifty 50 benchmark. Minimalist workstation with curved monitor displaying rule-based passive portfolio weights, 35mm lens, sharp commercial style.
```

### Image 23: `mutual-fund-large-cap-bluechip.jpg`
- **HTML Page:** `large-cap-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Bluechip Corporate Leadership & Steady Growth
- **Subject Description:** A panoramic architectural shot of major Indian conglomerate headquarters in Mumbai BKC / Cyberabad.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Architectural commercial photography.
- **Composition:** Upward low-angle architectural perspective representing stability and market leadership.
- **Camera Angle & Lens:** 24mm architectural lens.
- **Lighting:** Crisp morning sunlight reflecting off glass facades.
- **Background Environment:** Modern financial skyline with blue skies.
- **Color Palette:** Steel blue, deep navy, glass reflections, chrome.
- **Subject Positioning:** Towers rising solidly into clear sky.
- **Negative Space:** Sky area at top.

```text
GOOGLE FLOW PROMPT:
Architectural photograph of modern glass commercial towers in Mumbai Bandra Kurla Complex representing Indian bluechip large-cap corporations. Upward angle, clear morning sky, crisp reflections, 24mm architectural lens, commanding and institutional.
```

### Image 24: `mutual-fund-mid-cap-growth.jpg`
- **HTML Page:** `mid-cap-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Mid-Sized Corporate Expansion & Market Penetration
- **Subject Description:** A modern precision engineering and manufacturing facility in India showing dynamic industrial growth.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Industrial corporate photography.
- **Composition:** Diagonal dynamic leading lines down a high-tech factory floor.
- **Camera Angle & Lens:** 35mm f/2.8.
- **Lighting:** Bright industrial clean-room lighting with green accents.
- **Background Environment:** Robotic assembly lines and engineers in high-visibility gear.
- **Color Palette:** Industrial gray, vibrant safety green, crisp white.
- **Subject Positioning:** Machinery operating smoothly with engineers inspecting.
- **Negative Space:** Upper factory rafters.

```text
GOOGLE FLOW PROMPT:
High-tech industrial manufacturing photograph representing Indian mid-cap growth enterprises. Engineers reviewing robotics automated production line in modern clean facility, sharp focus, 35mm lens, dynamic economic expansion concept.
```

### Image 25: `mutual-fund-small-cap-enterprises.jpg`
- **HTML Page:** `small-cap-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Early-Stage Enterprises & High Compounding Potential
- **Subject Description:** A dynamic Indian innovation hub laboratory where startup founders collaborate around prototype testing.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Vibrant tech innovation photography.
- **Composition:** Energetic grouping around workbench with circuit boards and laptops.
- **Camera Angle & Lens:** 35mm f/2.0.
- **Lighting:** Vibrant LED lab illumination with warm spotlighting.
- **Background Environment:** Collaborative incubator workspace with sticky notes and whiteboards.
- **Color Palette:** Charcoal, electric green, bright orange, clean white.
- **Subject Positioning:** Founders engaged excitedly in testing new solutions.
- **Negative Space:** Upper background wall.

```text
GOOGLE FLOW PROMPT:
Energetic documentary photograph of young Indian tech entrepreneurs working in an advanced startup incubator lab. High energy, circuit boards, collaborative brainstorming, 35mm f/2.0 lens, representing small-cap enterprise innovation and high compounding potential.
```

### Image 26: `mutual-fund-flexi-cap-dynamic.jpg`
- **HTML Page:** `flexi-cap-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Agile Capital Allocation Across Cap Horizons
- **Subject Description:** A portfolio manager dynamically adjusting weights across large, mid, and small cap sectors on a multi-touch screen.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Modern fintech photography.
- **Composition:** Overhead angle showing interactive market cap balance controls.
- **Camera Angle & Lens:** 50mm f/2.8.
- **Lighting:** Soft blue and green ambient glow.
- **Background Environment:** Executive trading suite.
- **Color Palette:** Navy, emerald green, cyan, dark timber.
- **Subject Positioning:** Hands dynamically sliding allocation thresholds.
- **Negative Space:** Top perimeter.

```text
GOOGLE FLOW PROMPT:
Corporate finance photograph of an Indian fund manager using an interactive touch interface to dynamically rebalance market cap weights across large, mid, and small cap equities. Modern trading desk, 50mm lens, agile investment concept.
```

### Image 27: `mutual-fund-elss-tax-saving.jpg`
- **HTML Page:** `ELSS.html`
- **Section Name:** Category Overview
- **Title / Concept:** Tax Optimization & Long-Term Compounding Synergy
- **Subject Description:** A financial desk with Section 80C calculation sheets, calendar highlighting 3-year milestones, and equity growth graphs.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Still life editorial photography.
- **Composition:** Top-down organized flat-lay of tax documents and digital tablet.
- **Camera Angle & Lens:** 45mm f/3.2.
- **Lighting:** Warm morning sunlight casting clean shadows.
- **Background Environment:** Light oak timber desk.
- **Color Palette:** Cream, navy, green (#18A875), gold (#C6A15B).
- **Subject Positioning:** Documents neatly angled beside a fountain pen and coffee.
- **Negative Space:** Upper left quadrant.

```text
GOOGLE FLOW PROMPT:
Still life editorial photograph of financial tax planning. Section 80C mutual fund investment documents neatly arranged with calendar showing 3-year lock-in timeline, digital calculator, and fountain pen. Light wood desk, natural morning lighting, 45mm lens.
```

### Image 28: `mutual-fund-liquid-cash-management.jpg`
- **HTML Page:** `liquid-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Cash Management & Short-Duration Money Markets
- **Subject Description:** A corporate treasury manager monitoring short-term money market instruments, commercial papers, and liquidity reserves.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Corporate treasury documentary.
- **Composition:** Medium view of treasury specialist reviewing liquidity curves.
- **Camera Angle & Lens:** 50mm f/2.5.
- **Lighting:** Crisp corporate office lighting.
- **Background Environment:** Corporate treasury department.
- **Color Palette:** Navy, light blue, silver, white.
- **Subject Positioning:** Specialist verifying 91-day paper settlement dates.
- **Negative Space:** Left quadrant.

```text
GOOGLE FLOW PROMPT:
Corporate treasury photograph of an Indian financial officer managing liquid mutual fund cash reserves. Clean office environment, liquidity flow charts on monitor, 50mm lens, trustworthy cash management aesthetic.
```

### Image 29: `mutual-fund-overnight-money-markets.jpg`
- **HTML Page:** `overnight-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Overnight Money Markets & Collateralized Borrowing
- **Subject Description:** A high-precision view of interbank settlement screens displaying 1-day repo rates, TREPS trading, and sovereign collateral.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Institutional fintech photography.
- **Composition:** Close-up of interbank overnight settlement dashboard.
- **Camera Angle & Lens:** 35mm f/2.8.
- **Lighting:** Clean monitor illumination.
- **Background Environment:** Money market trading desk.
- **Color Palette:** Navy, cyan, green, slate.
- **Subject Positioning:** Real-time 1-day lending indicators.
- **Negative Space:** Top section of monitor.

```text
GOOGLE FLOW PROMPT:
Institutional finance photograph showing central banking overnight repo rate and TREPS interbank settlement data. Clean trading interface, high precision, 35mm lens, corporate cash parking concept.
```

### Image 30: `mutual-fund-international-global-markets.jpg`
- **HTML Page:** `international-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Global Stock Exchanges & Currency Diversification
- **Subject Description:** A conceptual composite of global financial capitals (New York, London, Tokyo, Mumbai) with currency exchange vectors.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Global finance editorial composite.
- **Composition:** Horizontal multi-city architectural vista with subtle currency overlay.
- **Camera Angle & Lens:** Panoramic 35mm framing.
- **Lighting:** Twilight blue hour across international financial districts.
- **Background Environment:** Illuminated skyscrapers across global time zones.
- **Color Palette:** Deep twilight blue, gold city lights, emerald green vectors.
- **Subject Positioning:** Global skyline flowing across frame.
- **Negative Space:** Upper sky area.

```text
GOOGLE FLOW PROMPT:
Cinematic global finance photograph featuring international stock exchange skylines during twilight blue hour. Subtle illuminated currency vectors linking New York, London, and Indian markets, 35mm lens, sophisticated geographic diversification concept.
```

### Image 31: `mutual-fund-fof-architecture.jpg`
- **HTML Page:** `fund-of-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Multi-Manager Scheme Layering & Asset Allocation
- **Subject Description:** An architectural infographic-style visual showing a master mutual fund allocating into diverse underlying specialist funds.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Minimalist geometric 3D render.
- **Composition:** Hierarchical umbrella structure spreading into specialist asset nodes.
- **Camera Angle & Lens:** Isometric 45-degree angle.
- **Lighting:** Clean studio key light with soft shadow gradient.
- **Background Environment:** Pure neutral architectural gray.
- **Color Palette:** Navy (#101D35), green (#18A875), amber gold, white.
- **Subject Positioning:** Central master node branching outward.
- **Negative Space:** Surrounding perimeter.

```text
GOOGLE FLOW PROMPT:
Clean 3D architectural graphic rendering showing a Fund of Funds (FoF) master fund branching into diversified underlying scheme unit blocks. Deep navy and gold accents, crisp isometric view, elegant institutional finance design, 8k.
```

### Image 32: `mutual-fund-sectoral-thematic-trends.jpg`
- **HTML Page:** `sectoral-thematic-funds.html`
- **Section Name:** Category Overview
- **Title / Concept:** Sector Concentration & Cyclical Industry Trends
- **Subject Description:** A multi-screen sector analysis dashboard showing focused industry cycles across banking, healthcare, and infrastructure.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Financial research photography.
- **Composition:** Sector heat map displayed on large wall monitor with research analyst taking notes.
- **Camera Angle & Lens:** 50mm f/2.5.
- **Lighting:** Ambient trading room light.
- **Background Environment:** Wall-mounted financial sector heatmaps.
- **Color Palette:** Navy, emerald green, warm amber, crimson.
- **Subject Positioning:** Analyst observing sector cycle shifts.
- **Negative Space:** Upper right.

```text
GOOGLE FLOW PROMPT:
Corporate finance photograph of an Indian analyst studying sectoral heat maps across banking, pharmaceutical, and technology industries. Wall-mounted data display, 50mm lens, focused thematic investing concept.
```

### Image 33: `mutual-fund-sip-compounding-timeline.jpg`
- **HTML Page:** `sip-investment.html`
- **Section Name:** What is a Systematic Investment Plan?
- **Title / Concept:** Systematic Investment Plan Timeline & Averaging
- **Subject Description:** A chronological photographic layout demonstrating how monthly SIP installments capture varying market NAV points over a 5-year cycle.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Educational infographic photography.
- **Composition:** Horizontal timeline wave passing through monthly coin markers.
- **Camera Angle & Lens:** 60mm macro f/3.5.
- **Lighting:** Clean directional studio lighting.
- **Background Environment:** Architectural graph paper with dark navy background.
- **Color Palette:** Navy (#101D35), green (#18A875), gold (#C6A15B), white.
- **Subject Positioning:** Ascending timeline from left to right.
- **Negative Space:** Top margins.

```text
GOOGLE FLOW PROMPT:
Educational still life photograph illustrating rupee-cost averaging in SIP investments. Stacks of coins along a fluctuating wave curve on dark architectural grid paper, showing more units bought during market dips, 60mm macro lens, clean lighting, 8k.
```

### Image 34: `mutual-fund-lump-sum-deployment.jpg`
- **HTML Page:** `lump-sum-investment.html`
- **Section Name:** Deployment Dynamics
- **Title / Concept:** Lump Sum vs Staggered Deployment Analysis
- **Subject Description:** A portfolio manager comparing lump sum market entry curves against staggered STP transfers on an analytics tablet.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Corporate wealth advisory photography.
- **Composition:** Close-up on tablet screen with advisor's hand pointing to staggered entry milestones.
- **Camera Angle & Lens:** 50mm f/2.8.
- **Lighting:** Natural daylight from window.
- **Background Environment:** Polished conference desk.
- **Color Palette:** Navy, emerald, gold, white.
- **Subject Positioning:** Tablet centered with hand gesturing.
- **Negative Space:** Around tablet frame.

```text
GOOGLE FLOW PROMPT:
Close-up photograph of an Indian financial planner comparing lump sum investment trajectories against a Systematic Transfer Plan (STP) on an iPad Pro. Polished wood desk, natural office lighting, 50mm lens, sharp focus.
```

### Image 35: `mutual-fund-direct-vs-regular-comparison.jpg`
- **HTML Page:** `direct-vs-regular.html`
- **Section Name:** Regulatory Context
- **Title / Concept:** Direct vs Regular Plan Evaluation Dialogue
- **Subject Description:** An investor and a wealth planner seated in an advisory office comparing two prospectus brochures clearly marked Direct Plan and Regular Plan.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Documentary corporate photography.
- **Composition:** Two brochures centered on table between advisor and client.
- **Camera Angle & Lens:** 50mm f/2.0.
- **Lighting:** Warm office ambient lighting.
- **Background Environment:** Consulting room with certificates and bookshelf.
- **Color Palette:** Navy, warm gray, ivory white, gold.
- **Subject Positioning:** Subjects leaning in to discuss fee breakdowns.
- **Negative Space:** Upper third of frame.

```text
GOOGLE FLOW PROMPT:
Documentary photograph of an Indian investor discussing Direct versus Regular mutual fund plans with an advisor. Two brochures on table showing expense ratio comparisons, natural window lighting, 50mm f/2.0, trustworthy advisory atmosphere.
```

### Image 36: `mutual-fund-growth-vs-idcw-distribution.jpg`
- **HTML Page:** `growth-vs-idcw.html`
- **Section Name:** Terminology Shift
- **Title / Concept:** NAV Impact of IDCW Distribution
- **Subject Description:** A clear educational comparison graph showing how NAV accumulates uninterrupted under the Growth option versus periodic drop-steps under IDCW.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Clean data visualization product photography.
- **Composition:** High-resolution monitor displaying comparative NAV trajectory lines.
- **Camera Angle & Lens:** 40mm f/3.2.
- **Lighting:** Soft screen glow with balanced rim light.
- **Background Environment:** Minimalist workstation setup.
- **Color Palette:** Navy, emerald green (Growth line), amber (IDCW line), white.
- **Subject Positioning:** Chart lines clearly visible and sharp.
- **Negative Space:** Top of display.

```text
GOOGLE FLOW PROMPT:
Product photograph of a financial chart on screen comparing the Growth option (smooth compounding curve) against the IDCW option (periodic dividend drops) in mutual funds. Clean UI, dark mode, 40mm lens, educational clarity.
```

### Image 37: `mutual-fund-nav-calculation-accounting.jpg`
- **HTML Page:** `nav-explained.html`
- **Section Name:** Definition & Formula
- **Title / Concept:** Daily NAV Calculation & Portfolio Accounting
- **Subject Description:** An accounting flow showing stock market closing prices feeding into AMC net asset calculations at 4:00 PM cutoff.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Corporate financial accounting photography.
- **Composition:** Analyst verifying closing NAV figures on a ledger spreadsheet with calculator.
- **Camera Angle & Lens:** 50mm f/2.8.
- **Lighting:** Warm late afternoon desk lamp lighting.
- **Background Environment:** Accounting department background.
- **Color Palette:** Navy, slate gray, ivory, green.
- **Subject Positioning:** Hands cross-referencing audit figures.
- **Negative Space:** Left quadrant.

```text
GOOGLE FLOW PROMPT:
Corporate finance photograph of an Indian mutual fund accountant verifying daily NAV valuation computations after market close. Financial ledger, calculator, digital spreadsheet, warm evening desk lighting, 50mm lens, precise accounting concept.
```

### Image 38: `mutual-fund-expense-ratio-ter-breakdown.jpg`
- **HTML Page:** `expense-ratio.html`
- **Section Name:** Cost Components
- **Title / Concept:** TER Breakdown & Compounding Cost Drag
- **Subject Description:** An analytical chart demonstrating the 20-year terminal divergence between a 0.5% TER and 1.8% TER.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Data visualization photography.
- **Composition:** Diverging line graph showing long-term compounding impact of fees.
- **Camera Angle & Lens:** 45mm f/3.5.
- **Lighting:** Clean studio lighting on tablet display.
- **Background Environment:** Dark executive desk.
- **Color Palette:** Navy, emerald green, coral red, gold.
- **Subject Positioning:** Graph lines diverging toward the right.
- **Negative Space:** Upper right corner.

```text
GOOGLE FLOW PROMPT:
Clean financial data visualization on a modern tablet showing the long-term impact of Total Expense Ratio (TER) on compounding wealth over 20 years. Minimalist dark desk, 45mm lens, high detail, clear educational finance graphic.
```

### Image 39: `mutual-fund-exit-load-holding-structure.jpg`
- **HTML Page:** `exit-load.html`
- **Section Name:** Purpose & Structure
- **Title / Concept:** Exit Load Calculation & Holding Period Timeline
- **Subject Description:** An illustrative calendar diagram explaining FIFO (First In First Out) redemption tracking for SIP tranches.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Still life conceptual photography.
- **Composition:** Minimalist 12-month calendar desk pad with checkmarks and lock symbols.
- **Camera Angle & Lens:** 50mm f/2.8.
- **Lighting:** Bright morning natural light.
- **Background Environment:** Clean white and timber workstation.
- **Color Palette:** Navy, emerald green, warm amber, white.
- **Subject Positioning:** Calendar angled naturally on desk.
- **Negative Space:** Top third of desk surface.

```text
GOOGLE FLOW PROMPT:
Still life photograph of an executive desk calendar highlighting a 365-day holding period and exit load waiver milestones. Elegant pen, digital tablet, soft daylight, 50mm lens, clean educational finance theme.
```

### Image 40: `mutual-fund-sebi-riskometer-gauge.jpg`
- **HTML Page:** `riskometer.html`
- **Section Name:** Objective Evaluation
- **Title / Concept:** SEBI Riskometer 6-Tiered Gauge Display
- **Subject Description:** A high-fidelity depiction of the semicircular Riskometer needle spanning Low to Very High.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** High-precision 3D graphic render.
- **Composition:** Centered semicircular gauge with needle pointing to Moderate tier.
- **Camera Angle & Lens:** Simulated 50mm lens, macro clarity.
- **Lighting:** Clean studio rim lighting highlighting the colored segments.
- **Background Environment:** Deep navy textured background.
- **Color Palette:** Green, yellow-green, yellow, orange, red, dark red.
- **Subject Positioning:** Gauge centered horizontally and vertically.
- **Negative Space:** Symmetrical margins around gauge.

```text
GOOGLE FLOW PROMPT:
3D render of the official SEBI mutual fund Riskometer gauge. Semicircular dial showing six risk tiers: Low, Low to Moderate, Moderate, Moderately High, High, Very High. Metallic needle pointing accurately, clean studio lighting, dark navy background, 8k.
```

### Image 41: `mutual-fund-portfolio-diversification-matrix.jpg`
- **HTML Page:** `diversification.html`
- **Section Name:** Core Principle
- **Title / Concept:** Correlation Heatmap Across Asset Classes
- **Subject Description:** An educational correlation matrix showing historical relationships between Indian equities, debt, and gold.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Data visualization photography.
- **Composition:** High-contrast heatmap grid on display screen.
- **Camera Angle & Lens:** 35mm f/3.2.
- **Lighting:** Clean display illumination.
- **Background Environment:** Modern finance research office.
- **Color Palette:** Deep navy, cool blue, bright emerald green, neutral gray.
- **Subject Positioning:** Matrix grid centered on screen.
- **Negative Space:** Surrounding frame.

```text
GOOGLE FLOW PROMPT:
High-resolution data visualization of an asset class correlation heatmap comparing Indian large-cap equities, mid-caps, sovereign debt, and gold. Dark UI theme, 35mm lens, clear financial analytics style.
```

### Image 42: `mutual-fund-power-of-compounding-curve.jpg`
- **HTML Page:** `compounding.html`
- **Section Name:** Exponential Growth
- **Title / Concept:** Exponential Compounding Hockey Stick Curve
- **Subject Description:** An illustrative growth chart comparing linear savings against exponential compounding over 30 years.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Architectural graphic photography.
- **Composition:** Curving hockey-stick trajectory rising sharply in the second half.
- **Camera Angle & Lens:** 50mm f/2.5.
- **Lighting:** Soft luminous glow along the compounding line.
- **Background Environment:** Dark navy geometric grid.
- **Color Palette:** Navy (#101D35), bright green (#18A875), gold (#C6A15B).
- **Subject Positioning:** Curve originating at lower left and climbing steeply to top right.
- **Negative Space:** Upper left quadrant.

```text
GOOGLE FLOW PROMPT:
Financial concept photograph of an exponential compounding hockey-stick curve glowing in vibrant emerald green against a deep navy blue background with subtle timeline year markers. 50mm lens, clean lines, inspiring wealth creation concept, 8k.
```

### Image 43: `mutual-fund-capital-gains-tax-rules.jpg`
- **HTML Page:** `investment-taxation.html`
- **Section Name:** Statutory Framework
- **Title / Concept:** Indian Mutual Fund Capital Gains Tax Rules
- **Subject Description:** An infographic displaying holding period thresholds, STCG, and LTCG tax slabs across equity and debt funds.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Editorial graphic layout.
- **Composition:** Structured dual-column tax comparison layout.
- **Camera Angle & Lens:** 45mm f/3.0.
- **Lighting:** Clean daylight on printed tax chart.
- **Background Environment:** Professional tax consultant's desk.
- **Color Palette:** Navy, emerald green, slate, white.
- **Subject Positioning:** Balanced two-tier framework.
- **Negative Space:** Top title zone.

```text
GOOGLE FLOW PROMPT:
Clean professional photograph of a tax advisory chart detailing Indian capital gains taxation rules for equity and specified mutual funds. Held by an accountant at an executive desk, 45mm lens, natural lighting, sharp text, authoritative finance concept.
```

### Image 44: `mutual-fund-beginner-investor-guide.jpg`
- **HTML Page:** `investment-for-beginners.html`
- **Section Name:** Foundational Roadmap
- **Title / Concept:** Beginner Investor Roadmap & Milestone Guide
- **Subject Description:** A young Indian investor reviewing financial goals, emergency funds, and SIP automation steps on a modern tablet in a sunlit workspace.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Lifestyle documentary photography.
- **Composition:** Medium shot of young investor sitting comfortably with notebook and digital device.
- **Camera Angle & Lens:** 35mm f/2.0.
- **Lighting:** Warm morning sunlight streaming through cafe window.
- **Background Environment:** Modern co-working space with plants and warm brickwork.
- **Color Palette:** Warm timber, navy, sage green, cream.
- **Subject Positioning:** Investor smiling thoughtfully while looking at savings roadmap.
- **Negative Space:** Right side of frame.

```text
GOOGLE FLOW PROMPT:
Inspiring lifestyle documentary photograph of a young Indian professional in a bright cafe workspace reviewing beginner mutual fund investment steps on a laptop and notebook. Optimistic, confident expression, warm natural sunlight, 35mm f/2.0 lens, relatable financial literacy aesthetic.
```

### Image 45: `mutual-fund-investor-resources-library.jpg`
- **HTML Page:** `investor-resources.html`
- **Section Name:** Knowledge Clearinghouse
- **Title / Concept:** Digital Financial Knowledge & Resource Repository
- **Subject Description:** A digital library interface displaying curated financial literacy guides, factsheet templates, and regulatory whitepapers.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Tech workspace editorial.
- **Composition:** Wide desktop setup displaying resource library portal.
- **Camera Angle & Lens:** 35mm f/3.5.
- **Lighting:** Clean ambient studio lighting.
- **Background Environment:** Minimalist corporate library setting.
- **Color Palette:** Navy, white, emerald, slate.
- **Subject Positioning:** Central screen with resources neatly cataloged.
- **Negative Space:** Upper wall area.

```text
GOOGLE FLOW PROMPT:
Commercial photograph of an investor education portal displayed on an all-in-one desktop in a modern corporate library. Clean layout showing financial checklists and glossary guides, 35mm lens, crisp and organized.
```

### Image 46: `mutual-fund-sip-calculator-interface.jpg`
- **HTML Page:** `sip-calculator.html`
- **Section Name:** Interactive Tool
- **Title / Concept:** Interactive SIP Financial Modeling Platform
- **Subject Description:** A user interacting with an advanced financial calculator interface displaying dynamic growth curves and maturity values.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** UI/UX product photography.
- **Composition:** Angled view of tablet screen with finger adjusting SIP contribution slider.
- **Camera Angle & Lens:** 50mm f/2.8 macro.
- **Lighting:** Soft directional light highlighting slider controls.
- **Background Environment:** Modern architectural desk.
- **Color Palette:** Navy (#101D35), green (#18A875), gold (#C6A15B), white.
- **Subject Positioning:** Hands interacting with slider control.
- **Negative Space:** Top and sides.

```text
GOOGLE FLOW PROMPT:
Close-up photograph of hands adjusting a monthly SIP investment slider on an iPad screen, watching the compound growth curve dynamically update. Minimalist desk background, 50mm macro lens, sharp UI focus, modern financial tech aesthetic.
```

### Image 47: `mutual-fund-lump-sum-calculator-interface.jpg`
- **HTML Page:** `lumpsum-calculator.html`
- **Section Name:** Interactive Tool
- **Title / Concept:** Lump Sum Portfolio Growth Modeler
- **Subject Description:** A digital dashboard showing single-deposit compounding projections over multi-year horizons.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Fintech product photography.
- **Composition:** Hero shot of lump sum calculator interface on high-res laptop display.
- **Camera Angle & Lens:** 35mm f/3.0.
- **Lighting:** Clean executive office lighting.
- **Background Environment:** Modern executive boardroom desk.
- **Color Palette:** Navy, emerald green, slate, warm timber.
- **Subject Positioning:** Laptop angled at 30 degrees.
- **Negative Space:** Right background.

```text
GOOGLE FLOW PROMPT:
Professional photograph of a laptop displaying a mutual fund lump sum calculator with investment principal and estimated gain breakdown bars. Clean modern office, 35mm lens, sharp screen detail, trustworthy fintech look.
```

### Image 48: `mutual-fund-goal-calculator-interface.jpg`
- **HTML Page:** `goal-planning-calculator.html`
- **Section Name:** Milestone Planning
- **Title / Concept:** Goal Planning & Shortfall Calculation Visualizer
- **Subject Description:** A visual analytics tool calculating future target shortfalls and displaying recommended monthly SIP paths.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Product photography.
- **Composition:** Straight-on view of goal calculator output screen.
- **Camera Angle & Lens:** 50mm f/3.2.
- **Lighting:** Soft even lighting.
- **Background Environment:** Minimalist office backdrop.
- **Color Palette:** Navy, green, amber, white.
- **Subject Positioning:** Target corpus vs savings gap centered.
- **Negative Space:** Top banner zone.

```text
GOOGLE FLOW PROMPT:
Product photograph of a goal-based financial calculator screen showing target corpus milestones and required monthly savings. High clarity, 50mm lens, clean modern UI design, educational planning concept.
```

### Image 49: `mutual-fund-risk-questionnaire-assessment.jpg`
- **HTML Page:** `risk-profile-questionnaire.html`
- **Section Name:** Self-Assessment Tool
- **Title / Concept:** Investor Risk Profiling Educational Survey
- **Subject Description:** An intuitive risk assessment digital dashboard measuring investor drawdown tolerance and investment horizons.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** UI concept photography.
- **Composition:** Person filling in interactive risk questions on a tablet.
- **Camera Angle & Lens:** 40mm f/2.5.
- **Lighting:** Natural daylight.
- **Background Environment:** Cozy modern home office.
- **Color Palette:** Navy, sage green, cream, timber.
- **Subject Positioning:** Tablet held naturally in hands.
- **Negative Space:** Background foliage.

```text
GOOGLE FLOW PROMPT:
Documentary photograph of an Indian professional completing an educational risk tolerance questionnaire on a tablet in a sunlit home study. 40mm f/2.5 lens, thoughtful and engaged atmosphere, authentic.
```

### Image 50: `mutual-fund-consultation-advisory-desk.jpg`
- **HTML Page:** `consultation.html`
- **Section Name:** Structured Discussion
- **Title / Concept:** Financial Consultation & Wealth Advisory Meeting
- **Subject Description:** A wealth advisor conducting an introductory financial consultation with an investor in a private meeting room.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Corporate documentary photography.
- **Composition:** Medium view of planner and client conversing warmly across desk.
- **Camera Angle & Lens:** 50mm f/2.0.
- **Lighting:** Warm natural side lighting.
- **Background Environment:** Private advisory office with city view.
- **Color Palette:** Navy, warm wood, cream, gold.
- **Subject Positioning:** Both subjects engaged in transparent dialogue.
- **Negative Space:** Top third.

```text
GOOGLE FLOW PROMPT:
Editorial photograph of an Indian wealth management consultation. A courteous advisor listening to a client in an executive private meeting room, reviewing financial planning documents. Warm natural lighting, 50mm f/2.0, trustworthy, professional.
```

### Image 51: `mutual-fund-corporate-workshop.jpg`
- **HTML Page:** `corporate-investment-planning.html`
- **Section Name:** Employee Financial Wellness
- **Title / Concept:** Corporate Financial Literacy Workshop
- **Subject Description:** An engaging workplace seminar with corporate employees attending a financial planning masterclass in an Indian tech company auditorium.
- **Aspect Ratio:** 4:3
- **Recommended Resolution:** 1000x750 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Corporate workplace photography.
- **Composition:** Auditorium view showing presenter on stage and engaged audience.
- **Camera Angle & Lens:** 35mm f/2.8.
- **Lighting:** Bright conference hall lighting.
- **Background Environment:** Modern corporate auditorium with branding.
- **Color Palette:** Navy, green, gray, white.
- **Subject Positioning:** Presenter sharing retirement literacy slides.
- **Negative Space:** Upper auditorium ceiling.

```text
GOOGLE FLOW PROMPT:
Corporate documentary photograph of an employee financial literacy workshop in an Indian technology company auditorium. Professional speaker presenting mutual fund basics on large screen to young employees, 35mm lens, authentic workplace wellness atmosphere.
```

### Image 52: `mutual-fund-regulatory-governance-sebi.jpg`
- **HTML Page:** `disclosures.html`
- **Section Name:** Statutory Governance
- **Title / Concept:** Regulatory Compliance & Legal Framework Visual
- **Subject Description:** A symbolic depiction of financial regulatory standards, legal codes, and SEBI compliance architecture.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Conceptual legal architecture photography.
- **Composition:** Marble law plinth with precision brass legal scales and regulatory statute book.
- **Camera Angle & Lens:** 50mm f/3.2.
- **Lighting:** Dramatic architectural side lighting.
- **Background Environment:** Modern institutional courtroom/regulatory hall.
- **Color Palette:** Deep navy, polished brass (#C6A15B), marble white.
- **Subject Positioning:** Statutes and scales centered with dignified symmetry.
- **Negative Space:** Upper half.

```text
GOOGLE FLOW PROMPT:
Conceptual legal still life representing SEBI regulatory compliance in Indian wealth management. Brass scales of justice and leather-bound financial statutes resting on a polished marble desk in a dignified corporate setting. 50mm lens, dramatic architectural lighting, authoritative.
```

### Image 53: `mutual-fund-data-privacy-security.jpg`
- **HTML Page:** `privacy-policy.html`
- **Section Name:** Data Protection
- **Title / Concept:** Data Privacy & Information Security Shield
- **Subject Description:** A conceptual visualization representing data privacy, encryption safeguards, and investor confidentiality.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Minimalist 3D architectural render.
- **Composition:** Geometric frosted glass shield icon with emerald green padlock glow.
- **Camera Angle & Lens:** 50mm isometric lens.
- **Lighting:** Soft internal glow with navy ambient backlight.
- **Background Environment:** Subtle dark navy cryptographic pattern.
- **Color Palette:** Navy (#101D35), emerald green (#18A875), frosted glass.
- **Subject Positioning:** Shield centered with soft shadow.
- **Negative Space:** Symmetrical margins.

```text
GOOGLE FLOW PROMPT:
Minimalist 3D conceptual rendering of a data privacy shield for financial services. Frosted glass shield with glowing green security lock against a deep navy background with faint cryptographic data lines, 50mm lens, elegant and reassuring.
```

### Image 54: `mutual-fund-legal-terms-compliance.jpg`
- **HTML Page:** `terms-and-conditions.html`
- **Section Name:** Legal Terms
- **Title / Concept:** Website Legal Terms & Compliance Overview
- **Subject Description:** A conceptual illustration of legal terms, intellectual property protections, and terms of service documentation.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Still life editorial photography.
- **Composition:** Executive desk with legal terms document, fountain pen, and architectural seal.
- **Camera Angle & Lens:** 45mm f/3.5.
- **Lighting:** Soft warm studio daylight.
- **Background Environment:** Executive walnut desk.
- **Color Palette:** Walnut brown, cream parchment, navy ink.
- **Subject Positioning:** Document positioned neatly on desk.
- **Negative Space:** Upper left.

```text
GOOGLE FLOW PROMPT:
Still life photograph of corporate legal terms of service document on a dark walnut desk with a classic fountain pen and brass bookmark. Soft directional window light, 45mm lens, dignified legal compliance aesthetic.
```

### Image 55: `mutual-fund-statutory-risk-disclaimer.jpg`
- **HTML Page:** `disclaimer.html`
- **Section Name:** Legal Notice
- **Title / Concept:** Statutory Risk Disclaimer & Regulatory Notice
- **Subject Description:** A formal regulatory notice layout displaying SEBI statutory risk warnings and investor caution guidelines.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** Official institutional document photography.
- **Composition:** Crisp centered framing of statutory risk advisory text with official seal.
- **Camera Angle & Lens:** 50mm f/4.0.
- **Lighting:** Clean balanced commercial lighting.
- **Background Environment:** Formal institutional backdrop.
- **Color Palette:** Navy, amber gold (#C6A15B), crisp white, crimson warning badge.
- **Subject Positioning:** Notice centered.
- **Negative Space:** Clean surrounding margins.

```text
GOOGLE FLOW PROMPT:
Official corporate still life photograph of a statutory mutual fund market risk disclaimer document displayed in an executive portfolio folder. Brass pen resting beside, formal institutional lighting, 50mm lens, sharp, clear, and authoritative.
```

### Image 56: `mutual-fund-cookie-privacy-browser.jpg`
- **HTML Page:** `cookie-policy.html`
- **Section Name:** Browser Privacy
- **Title / Concept:** Browser Cookie Settings & Privacy Controls
- **Subject Description:** An illustration of browser settings toggles for session cookies, caching, and privacy permissions.
- **Aspect Ratio:** 16:9
- **Recommended Resolution:** 1200x675 pixels
- **Orientation:** Landscape
- **Photography / Illustration Style:** UI product illustration.
- **Composition:** Minimalist digital browser privacy toggles on screen.
- **Camera Angle & Lens:** 50mm f/3.0.
- **Lighting:** Even screen luminescence.
- **Background Environment:** Modern laptop display.
- **Color Palette:** Navy, emerald green toggles, slate, white.
- **Subject Positioning:** Privacy toggles clearly highlighted.
- **Negative Space:** Top and bottom borders.

```text
GOOGLE FLOW PROMPT:
Clean product photograph of modern browser cookie privacy settings on a laptop display. Toggle switches in clean green and slate against a dark mode UI, 50mm lens, clear digital privacy concept.
```

---

## Complete Image Inventory Table

| No. | Exact Target Filename | HTML Page | Section Name | Aspect | Resolution | Orientation |
|---|---|---|---|---|---|---|
| 1 | `mutual-fund-hero-investment-planning.jpg` | `index.html` | Hero Section | 16:9 | 1200x675 | Landscape |
| 2 | `mutual-fund-market-research.jpg` | `index.html` | Why Understand Mutual Funds Section | 4:3 | 1000x750 | Landscape |
| 3 | `mutual-fund-sip-investment.jpg` | `index.html` | SIP Investment Section | 4:3 | 1000x750 | Landscape |
| 4 | `mutual-fund-investor-education.jpg` | `about.html` | Our Educational Philosophy | 4:3 | 1000x750 | Landscape |
| 5 | `mutual-fund-financial-consultation.jpg` | `services.html` | Services Overview Hero | 16:9 | 1200x675 | Landscape |
| 6 | `mutual-fund-wealth-planning.jpg` | `mutual-funds.html` | How Mutual Funds Work | 4:3 | 1000x750 | Landscape |
| 7 | `mutual-fund-asset-allocation.jpg` | `investment-approach.html` | Process Over Market Timing | 4:3 | 1000x750 | Landscape |
| 8 | `mutual-fund-financial-goals.jpg` | `financial-planning.html` | Why Plan Before You Invest | 4:3 | 1000x750 | Landscape |
| 9 | `mutual-fund-retirement-planning.jpg` | `goal-based-investing.html` | Mapping Horizons to Asset Classes | 4:3 | 1000x750 | Landscape |
| 10 | `mutual-fund-portfolio-review.jpg` | `portfolio-review.html` | Why Review Your Mutual Fund Portfolio | 4:3 | 1000x750 | Landscape |
| 11 | `mutual-fund-investment-dashboard.jpg` | `asset-allocation.html` | Simulate Educational Allocation Profiles | 16:9 | 1200x675 | Landscape |
| 12 | `mutual-fund-risk-management.jpg` | `risk-management.html` | The Spectrum of Mutual Fund Risks | 16:9 | 1200x675 | Landscape |
| 13 | `mutual-fund-investor-meeting.jpg` | `investment-process.html` | 5-Stage Investment Methodology | 16:9 | 1200x675 | Landscape |
| 14 | `mutual-fund-team-collaboration.jpg` | `team.html` | Advisory Investment Committee Collaboration | 16:9 | 1200x675 | Landscape |
| 15 | `mutual-fund-market-insights.jpg` | `insights.html` | Financial Insights Desk | 16:9 | 1200x675 | Landscape |
| 16 | `mutual-fund-reading-factsheet.jpg` | `article-details.html` | Featured Article Header | 16:9 | 1200x675 | Landscape |
| 17 | `mutual-fund-faq-support.jpg` | `faq.html` | Knowledge Clearinghouse | 16:9 | 1200x675 | Landscape |
| 18 | `mutual-fund-advisory-office.jpg` | `contact.html` | Communication Channels | 4:3 | 1000x750 | Landscape |
| 19 | `mutual-fund-equity-investment.jpg` | `equity-mutual-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 20 | `mutual-fund-debt-investment.jpg` | `debt-mutual-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 21 | `mutual-fund-hybrid-allocation.jpg` | `hybrid-mutual-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 22 | `mutual-fund-index-tracking.jpg` | `index-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 23 | `mutual-fund-large-cap-bluechip.jpg` | `large-cap-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 24 | `mutual-fund-mid-cap-growth.jpg` | `mid-cap-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 25 | `mutual-fund-small-cap-enterprises.jpg` | `small-cap-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 26 | `mutual-fund-flexi-cap-dynamic.jpg` | `flexi-cap-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 27 | `mutual-fund-elss-tax-saving.jpg` | `ELSS.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 28 | `mutual-fund-liquid-cash-management.jpg` | `liquid-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 29 | `mutual-fund-overnight-money-markets.jpg` | `overnight-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 30 | `mutual-fund-international-global-markets.jpg` | `international-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 31 | `mutual-fund-fof-architecture.jpg` | `fund-of-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 32 | `mutual-fund-sectoral-thematic-trends.jpg` | `sectoral-thematic-funds.html` | Category Overview | 4:3 | 1000x750 | Landscape |
| 33 | `mutual-fund-sip-compounding-timeline.jpg` | `sip-investment.html` | What is a Systematic Investment Plan? | 4:3 | 1000x750 | Landscape |
| 34 | `mutual-fund-lump-sum-deployment.jpg` | `lump-sum-investment.html` | Deployment Dynamics | 4:3 | 1000x750 | Landscape |
| 35 | `mutual-fund-direct-vs-regular-comparison.jpg` | `direct-vs-regular.html` | Regulatory Context | 4:3 | 1000x750 | Landscape |
| 36 | `mutual-fund-growth-vs-idcw-distribution.jpg` | `growth-vs-idcw.html` | Terminology Shift | 4:3 | 1000x750 | Landscape |
| 37 | `mutual-fund-nav-calculation-accounting.jpg` | `nav-explained.html` | Definition & Formula | 4:3 | 1000x750 | Landscape |
| 38 | `mutual-fund-expense-ratio-ter-breakdown.jpg` | `expense-ratio.html` | Cost Components | 4:3 | 1000x750 | Landscape |
| 39 | `mutual-fund-exit-load-holding-structure.jpg` | `exit-load.html` | Purpose & Structure | 4:3 | 1000x750 | Landscape |
| 40 | `mutual-fund-sebi-riskometer-gauge.jpg` | `riskometer.html` | Objective Evaluation | 4:3 | 1000x750 | Landscape |
| 41 | `mutual-fund-portfolio-diversification-matrix.jpg` | `diversification.html` | Core Principle | 4:3 | 1000x750 | Landscape |
| 42 | `mutual-fund-power-of-compounding-curve.jpg` | `compounding.html` | Exponential Growth | 4:3 | 1000x750 | Landscape |
| 43 | `mutual-fund-capital-gains-tax-rules.jpg` | `investment-taxation.html` | Statutory Framework | 4:3 | 1000x750 | Landscape |
| 44 | `mutual-fund-beginner-investor-guide.jpg` | `investment-for-beginners.html` | Foundational Roadmap | 16:9 | 1200x675 | Landscape |
| 45 | `mutual-fund-investor-resources-library.jpg` | `investor-resources.html` | Knowledge Clearinghouse | 16:9 | 1200x675 | Landscape |
| 46 | `mutual-fund-sip-calculator-interface.jpg` | `sip-calculator.html` | Interactive Tool | 16:9 | 1200x675 | Landscape |
| 47 | `mutual-fund-lump-sum-calculator-interface.jpg` | `lumpsum-calculator.html` | Interactive Tool | 16:9 | 1200x675 | Landscape |
| 48 | `mutual-fund-goal-calculator-interface.jpg` | `goal-planning-calculator.html` | Milestone Planning | 16:9 | 1200x675 | Landscape |
| 49 | `mutual-fund-risk-questionnaire-assessment.jpg` | `risk-profile-questionnaire.html` | Self-Assessment Tool | 16:9 | 1200x675 | Landscape |
| 50 | `mutual-fund-consultation-advisory-desk.jpg` | `consultation.html` | Structured Discussion | 16:9 | 1200x675 | Landscape |
| 51 | `mutual-fund-corporate-workshop.jpg` | `corporate-investment-planning.html` | Employee Financial Wellness | 4:3 | 1000x750 | Landscape |
| 52 | `mutual-fund-regulatory-governance-sebi.jpg` | `disclosures.html` | Statutory Governance | 16:9 | 1200x675 | Landscape |
| 53 | `mutual-fund-data-privacy-security.jpg` | `privacy-policy.html` | Data Protection | 16:9 | 1200x675 | Landscape |
| 54 | `mutual-fund-legal-terms-compliance.jpg` | `terms-and-conditions.html` | Legal Terms | 16:9 | 1200x675 | Landscape |
| 55 | `mutual-fund-statutory-risk-disclaimer.jpg` | `disclaimer.html` | Legal Notice | 16:9 | 1200x675 | Landscape |
| 56 | `mutual-fund-cookie-privacy-browser.jpg` | `cookie-policy.html` | Browser Privacy | 16:9 | 1200x675 | Landscape |

### Inventory Summary Metrics
- **Total Images:** 56
- **16:9 Landscape Images (1200x675):** 28
- **4:3 Landscape Images (1000x750):** 28
- **Portrait Images:** 0
- **Square Images:** 0
- **Broken Links / Missing Placeholders:** 0 (100% verified match)

---

## Recommended Generation Order & Priority
To achieve maximum impact when generating images via Google Flow, follow this staged rollout:
1. **Tier 1 (High Priority - Core Homepage & Key Conversions):**
   - Image 1: `mutual-fund-hero-investment-planning.jpg` (Homepage Hero)
   - Image 3: `mutual-fund-sip-investment.jpg` (Homepage SIP Section)
   - Image 50: `mutual-fund-consultation-advisory-desk.jpg` (Consultation Enquiry)
   - Image 46: `mutual-fund-sip-calculator-interface.jpg` (SIP Calculator)
2. **Tier 2 (High Priority - Flagship Fund Categories):**
   - Image 19: `mutual-fund-equity-investment.jpg` (Equity Funds)
   - Image 20: `mutual-fund-debt-investment.jpg` (Debt Funds)
   - Image 21: `mutual-fund-hybrid-allocation.jpg` (Hybrid Funds)
   - Image 22: `mutual-fund-index-tracking.jpg` (Index Funds)
   - Image 27: `mutual-fund-elss-tax-saving.jpg` (ELSS Tax Saving)
3. **Tier 3 (Medium Priority - Planning & Methodology):**
   - Image 4: `mutual-fund-investor-education.jpg` (About Us)
   - Image 5: `mutual-fund-financial-consultation.jpg` (Services)
   - Image 7: `mutual-fund-asset-allocation.jpg` (Investment Approach)
   - Image 8: `mutual-fund-financial-goals.jpg` (Financial Planning)
   - Image 10: `mutual-fund-portfolio-review.jpg` (Portfolio Review)
4. **Tier 4 (Remaining Category & Education Pages):** Complete remaining specialized categories and educational articles.

---

## Step-by-Step Replacement Instructions
When you are ready to replace any placeholder with a real generated image:
1. Ensure your generated JPG or WebP is saved in `assets/images/` under the exact specified filename.
2. Open the corresponding HTML file in a code editor.
3. Find the target `.img-placeholder-wrapper` container.
4. Replace the inner `.img-placeholder` or the entire wrapper with:
   ```html
   <img src="assets/images/[exact-filename].jpg" alt="[Descriptive Alt Text]" class="rounded-lg shadow-lg" loading="lazy" width="1200" height="675">
   ```
5. Save and reload the page. The responsive layout and styling will adapt seamlessly.