# Mutual Fund Advisory — Wealth Management & Investor Education Platform

A premium, modern, fully responsive, multi-page static website engineered for a generic **Mutual Fund Advisory Business** operating in the Indian financial services market. Built entirely with **semantic HTML5, modern CSS3, and vanilla JavaScript**, adhering strictly to zero-dependency static architecture and zero external framework constraints.

---

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Important Business Model Selection Guide](#important-business-model-selection-guide)
   - [Model A: SEBI-Registered Investment Adviser (RIA)](#model-a-sebi-registered-investment-adviser-ria)
   - [Model B: AMFI-Registered Mutual Fund Distributor (MFD)](#model-b-amfi-registered-mutual-fund-distributor-mfd)
   - [Model C: Investor Education Platform (Default Demonstration Mode)](#model-c-investor-education-platform-default-demonstration-mode)
   - [Regulatory Compliance & Launch Checklist](#regulatory-compliance--launch-checklist)
3. [Technology Stack & Architectural Standards](#technology-stack--architectural-standards)
4. [Complete Website Sitemap (54 Pages)](#complete-website-sitemap-54-pages)
5. [Directory Structure](#directory-structure)
6. [Interactive Components & Features](#interactive-components--features)
   - [Financial Calculators](#financial-calculators)
   - [Risk Education Questionnaire](#risk-education-questionnaire)
   - [Interactive Asset Allocation Switcher](#interactive-asset-allocation-switcher)
   - [Three-Step Consultation Enquiry Form](#three-step-consultation-enquiry-form)
   - [FAQ Accordion & Navigation](#faq-accordion--navigation)
7. [Hostinger Static Hosting Deployment Guide](#hostinger-static-hosting-deployment-guide)
   - [Prerequisites](#prerequisites)
   - [Method 1: Hostinger File Manager Upload](#method-1-hostinger-file-manager-upload)
   - [Method 2: FTP / SFTP Deployment](#method-2-ftp--sftp-deployment)
   - [Method 3: Git Deployment via Hostinger Git Tool](#method-3-git-deployment-via-hostinger-git-tool)
   - [Apache .htaccess Configuration (Caching, Gzip, Security Headers)](#apache-htaccess-configuration)
   - [SSL/TLS & Domain Activation](#ssltls--domain-activation)
8. [Image Asset Workflow & Google Flow Generation](#image-asset-workflow--google-flow-generation)
9. [Regulatory Safeguards & Disclaimer Standard](#regulatory-safeguards--disclaimer-standard)
10. [Local Development & Maintenance](#local-development--maintenance)

---

## Executive Summary

The **Mutual Fund Advisory** platform is designed to provide investors with structured mutual fund education, goal-based financial planning concepts, systematic investment discipline (SIP), risk profiling methodologies, and transparent disclosures. 

### Core Design Philosophy:
* **Editorial & Institutional Aesthetics**: Deep navy palette (`#101D35`, `#182B49`), wealth green (`#18A875`, `#087B59`), and subtle gold accents (`#C6A15B`) reminiscent of premier private wealth management and institutional asset management portals.
* **Rigorous Regulatory Demarcation**: Complete separation between general financial education and personalized, regulated investment advice.
* **Zero Fabricated Credentials**: Does not display artificial SEBI registration numbers, AMFI ARN IDs, EUINs, NISM certifications, inflated AUM metrics, or fabricated testimonials.
* **100% Client-Side / Zero Dependencies**: Operates without React, Vue, Angular, Bootstrap, Tailwind, jQuery, Node.js, PHP, or external CDNs. Compatible with any standard static web server or CDN.

---

## Important Business Model Selection Guide

> [!WARNING]
> **REGULATORY NOTICE FOR DEPLOYMENT IN INDIA**  
> Under Securities and Exchange Board of India (SEBI) and Association of Mutual Funds in India (AMFI) regulations, an entity cannot blur the distinction between **fee-only investment advisory** and **commission-based distribution**. 
> Before publishing this website for an actual commercial entity, the organization **MUST** select its appropriate operational business model below and update the brand identity, registration credentials, disclosures, and fee schedules accordingly.

The codebase is delivered in **Model C (Neutral Investor Education Platform)** by default. When adapting this template for commercial launch, update `disclosures.html`, the header/footer identity badges, and page copy based on the chosen model:

### Model A: SEBI-Registered Investment Adviser (RIA)
* **Regulatory Framework**: SEBI (Investment Advisers) Regulations, 2013 (as amended).
* **Core Function**: Fiduciary, fee-only personalized financial planning and investment advice. RIAs act exclusively in the best interest of the client and cannot receive distribution commissions or brokerage from asset management companies (AMCs).
* **Required Disclaimers & Updates**:
  1. Display valid **SEBI Registration Number** (e.g., `INA0000XXXXX`), registration validity, BASL membership number, and registered principal office address in the header/footer and `disclosures.html`.
  2. Maintain a strict **Fee Disclosure Schedule** explaining the fee structure (Fixed Fee or Percentage of AUA capped by SEBI regulations).
  3. Clearly state that investment recommendations are made for direct plans of mutual fund schemes where no distributor commission is paid.
  4. Display the SEBI Complaints Redress System (**SCORES**) and Online Dispute Resolution (**ODR**) portal links prominently.
  5. Include the mandatory statutory notice: *"Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI, membership of BASL and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors."*

### Model B: AMFI-Registered Mutual Fund Distributor (MFD)
* **Regulatory Framework**: AMFI Code of Conduct and SEBI circulars governing Mutual Fund Distributors.
* **Core Function**: Distribution of mutual fund schemes to investors and transaction facilitation. MFDs earn trail commissions from Asset Management Companies (AMCs) on regular plans.
* **Required Disclaimers & Updates**:
  1. Change header badge and all service descriptions to **"AMFI-Registered Mutual Fund Distributor"**.
  2. Clearly state that the entity acts as a distributor and **not** as a SEBI-registered Investment Adviser. The firm does not charge advisory fees from investors; commissions are received directly from AMCs for schemes distributed.
  3. Display valid **AMFI Registration Number (ARN)**, ARN validity period, and EUIN (Employee Unique Identification Number) on all marketing collateral and website footers.
  4. Provide a full **Scheme-Wise Commission Disclosure** (or link to standard commission matrix) as mandated by SEBI circular SEBI/IMD/CIR No. 4/168230/09.
  5. Include statutory notice: *"Mutual Fund investments are subject to market risks, read all scheme related documents carefully."*

### Model C: Investor Education Platform (Default Demonstration Mode)
* **Regulatory Framework**: General educational content under financial literacy guidelines.
* **Core Function**: Explaining mutual fund concepts, mathematical calculations (SIP/Lumpsum), category mechanics, taxation, and risk factors without endorsing specific AMCs, recommending specific schemes, or collecting money.
* **Current Implementation**:
  1. Generic identity: **"MUTUAL FUND ADVISORY — Investor Education & Demonstration"**.
  2. Explicit statements that no personalized advisory, distribution, or portfolio management is conducted.
  3. Consultation form acts as a demo enquiry workflow for investor education sessions, corporate workshops, or generic information requests.

### Regulatory Compliance & Launch Checklist
Prior to public domain launch:
- [ ] Confirm entity legal status (RIA vs. MFD vs. Educational Portal).
- [ ] Insert verified SEBI Registration Number or AMFI ARN in `disclosures.html` and footer.
- [ ] Verify grievance redressal contact officer details, phone numbers, and escalation matrix.
- [ ] Replace demo office address (`Financial District, BKC / Nariman Point, Mumbai`) with registered business premises.
- [ ] Review all marketing claims with a qualified compliance officer or legal counsel.
- [ ] Verify that no scheme promises guaranteed returns or principal protection.

---

## Technology Stack & Architectural Standards

| Layer | Implementation | Notes |
| :--- | :--- | :--- |
| **Markup** | HTML5 Semantic Architecture | Strict `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`. Fully accessible ARIA attributes. |
| **Styling** | Vanilla CSS3 (3 modular stylesheets) | `style.css` (Base design system, typography, components), `responsive.css` (Breakpoints 1200px, 992px, 768px, 480px), `animations.css` (Keyframes & transitions). |
| **Scripting** | Vanilla ES6+ JavaScript | `main.js`, `navigation.js`, `calculators.js`, `portfolio.js`, `forms.js`, `faq.js`. Zero external dependencies. |
| **Data & Storage** | Local In-Memory & Client-Side Storage | No backend database required. Client-side form validation and calculations. |
| **SEO & Crawlers** | Complete `sitemap.xml` & `robots.txt` | Fully mapped canonical URLs, Open Graph / Twitter Card meta tags on all 54 pages. |
| **Performance** | Zero external fonts or blocking CDNs | System font stack (`Segoe UI`, `SF Pro Display`, `Inter`, `system-ui`), zero render-blocking framework scripts. |

---

## Complete Website Sitemap (54 Pages)

All 54 pages exist as dedicated, standalone HTML files in the root folder with 100% active internal linking (0 broken links):

### 1. Core Corporate & Advisory Pages (16 Pages)
1. `index.html` — Homepage with hero, quick navigation, category overview, SIP education, process, calculators, and riskometer.
2. `about.html` — Mission, vision, core principles, investor-first fiduciary philosophy, and leadership governance.
3. `services.html` — Comprehensive overview of mutual fund guidance, goal planning, portfolio reviews, and corporate workshops.
4. `mutual-funds.html` — Master overview of mutual fund structures, SEBI classification framework, and investment concepts.
5. `investment-approach.html` — Fiduciary, disciplined, long-term, asset-allocation-first investment philosophy.
6. `financial-planning.html` — Comprehensive 6-step financial planning methodology and lifecycle goal management.
7. `goal-based-investing.html` — Aligning investment horizons to life goals (retirement, higher education, home acquisition).
8. `portfolio-review.html` — Objective health check framework for evaluating existing mutual fund holdings.
9. `asset-allocation.html` — Interactive strategic asset allocation across equity, debt, gold, and cash.
10. `risk-management.html` — Understanding volatility, drawdown risk, inflation risk, liquidity risk, and risk mitigation.
11. `investment-process.html` — Transparent 5-stage educational roadmap from goal discovery to periodic rebalancing.
12. `team.html` — Overview of advisory leadership, research desk, compliance team, and client support values.
13. `insights.html` — Financial insights hub, market education articles, research commentaries, and investor guides.
14. `article-details.html` — Deep-dive educational article on building a resilient long-term mutual fund portfolio.
15. `faq.html` — Searchable, accordion-driven database of 18+ high-frequency mutual fund investor questions.
16. `contact.html` — Contact touchpoints, Mumbai office address, investor support hours, and consultation enquiry form.

### 2. SEBI Mutual Fund Category Pages (14 Pages)
17. `equity-mutual-funds.html` — Growth-oriented equity schemes, market-cap classifications, and risk profiles.
18. `debt-mutual-funds.html` — Fixed income schemes, duration management, credit quality, and accrual strategies.
19. `hybrid-mutual-funds.html` — Balanced advantage, aggressive hybrid, multi-asset, and equity savings schemes.
20. `index-funds.html` — Low-cost passive investing, benchmark replication, tracking error, and index mechanics.
21. `large-cap-funds.html` — Top 100 bluechip enterprises, corporate stability, and steady capital compounding.
22. `mid-cap-funds.html` — Companies ranked 101st to 250th, emerging sector leaders, and growth potential.
23. `small-cap-funds.html` — Companies ranked 251st onwards, high return potential, volatility, and long investment horizons.
24. `flexi-cap-funds.html` — Dynamic unconstrained market-cap allocation across large, mid, and small-cap stocks.
25. `ELSS.html` — Equity Linked Savings Schemes, Section 80C tax deduction, 3-year mandatory lock-in period.
26. `liquid-funds.html` — Debt instruments with maturity up to 91 days, high liquidity, and emergency cash management.
27. `overnight-funds.html` — 1-day maturity money market securities, virtually zero interest rate and credit risk.
28. `international-funds.html` — Geographic diversification, overseas feeder funds, and global market exposure.
29. `fund-of-funds.html` — Multi-manager strategies, multi-asset FoFs, and domestic/international underlying schemes.
30. `sectoral-thematic-funds.html` — High-conviction sector/theme exposure (banking, tech, pharma, manufacturing, ESG).

### 3. Investment Strategy & Education Pages (12 Pages)
31. `sip-investment.html` — Systematic Investment Plans, rupee-cost averaging, compounding timelines, and discipline.
32. `lump-sum-investment.html` — Lump sum deployment, market timing pitfalls, and systematic transfer plans (STP).
33. `direct-vs-regular.html` — Comprehensive breakdown of Direct Plans vs. Regular Plans, expense ratios, and commission impact.
34. `growth-vs-idcw.html` — Growth Option vs. Income Distribution cum Capital Withdrawal (IDCW), compounding, and tax mechanics.
35. `nav-explained.html` — Net Asset Value (NAV) formula, unit allocation, pricing cutoff timings, and common misconceptions.
36. `expense-ratio.html` — Total Expense Ratio (TER), management fees, registrar costs, and long-term net yield impact.
37. `exit-load.html` — Redemption charges, holding period thresholds, and liquidity management.
38. `riskometer.html` — Official SEBI 6-tier Riskometer gauge (Low, Low to Moderate, Moderate, Moderately High, High, Very High).
39. `diversification.html` — Correlation matrix, multi-asset benefits, avoiding portfolio overlap, and over-diversification pitfalls.
40. `compounding.html` — Mathematical power of compounding, time horizon vs. capital contribution, and rule of 72.
41. `investment-taxation.html` — Post-Finance Act mutual fund taxation rules, LTCG, STCG, indexation removal, and slab rates.
42. `investment-for-beginners.html` — Step-by-step primer for first-time investors (KYC, goal selection, fund picking, avoiding panic).

### 4. Investor Tools & Enquiry Pages (7 Pages)
43. `investor-resources.html` — Central repository for educational downloads, factsheet guides, compliance checklists, and tools.
44. `sip-calculator.html` — Interactive client-side monthly SIP investment calculator with dynamic visual breakdown.
45. `lumpsum-calculator.html` — Interactive lump sum future value growth calculator with compound interest formula.
46. `goal-planning-calculator.html` — Goal target calculator computing required monthly SIP for targeted future corpus.
47. `risk-profile-questionnaire.html` — 5-question educational risk assessment profiling Conservative, Moderate, or Aggressive posture.
48. `consultation.html` — 3-step interactive consultation enquiry form with instant feedback and field validation.
49. `corporate-investment-planning.html` — Institutional treasury cash management, corporate SIPs, and employee financial literacy.

### 5. Regulatory, Compliance & Legal Pages (5 Pages)
50. `disclosures.html` — Comprehensive regulatory disclosures, business model declaration, grievance mechanism, and SEBI circular references.
51. `privacy-policy.html` — Data protection policy under Digital Personal Data Protection Act (DPDPA), cookie notice, and data security.
52. `terms-and-conditions.html` — Website usage terms, intellectual property, disclaimer of warranty, and limitation of liability.
53. `disclaimer.html` — Statutory mutual fund risk disclaimers, no-guarantee notices, and professional advice notices.
54. `cookie-policy.html` — Transparent explanation of essential session cookies, analytical cookies, and user privacy preferences.

---

## Directory Structure

```
Mutual Fund Advisory/
│
├── index.html                               # Homepage
├── about.html                               # About Us
├── services.html                            # Services
├── mutual-funds.html                        # Mutual Funds Master Hub
├── investment-approach.html                 # Investment Approach
├── financial-planning.html                  # Financial Planning
├── goal-based-investing.html                # Goal-Based Investing
├── portfolio-review.html                    # Portfolio Review
├── asset-allocation.html                    # Asset Allocation & Switcher
├── risk-management.html                     # Risk Management
├── investment-process.html                  # Investment Planning Process
├── team.html                                # Team Overview
├── insights.html                            # Financial Insights Hub
├── article-details.html                     # Deep-dive Educational Article
├── faq.html                                 # Interactive FAQs
├── contact.html                             # Contact & Enquiry
│
├── equity-mutual-funds.html                 # Category: Equity Funds
├── debt-mutual-funds.html                   # Category: Debt Funds
├── hybrid-mutual-funds.html                 # Category: Hybrid Funds
├── index-funds.html                         # Category: Index Funds
├── large-cap-funds.html                     # Category: Large Cap Funds
├── mid-cap-funds.html                       # Category: Mid Cap Funds
├── small-cap-funds.html                     # Category: Small Cap Funds
├── flexi-cap-funds.html                     # Category: Flexi Cap Funds
├── ELSS.html                                # Category: Tax-Saving ELSS
├── liquid-funds.html                        # Category: Liquid Funds
├── overnight-funds.html                     # Category: Overnight Funds
├── international-funds.html                 # Category: International Funds
├── fund-of-funds.html                       # Category: Fund of Funds
├── sectoral-thematic-funds.html             # Category: Sectoral & Thematic
│
├── sip-investment.html                      # Strategy: SIP Investment
├── lump-sum-investment.html                 # Strategy: Lump Sum Investment
├── direct-vs-regular.html                   # Strategy: Direct vs. Regular
├── growth-vs-idcw.html                      # Strategy: Growth vs. IDCW
├── nav-explained.html                       # Strategy: Understanding NAV
├── expense-ratio.html                       # Strategy: Expense Ratio (TER)
├── exit-load.html                           # Strategy: Understanding Exit Load
├── riskometer.html                          # Strategy: SEBI Riskometer
├── diversification.html                     # Strategy: Diversification
├── compounding.html                         # Strategy: Power of Compounding
├── investment-taxation.html                 # Strategy: Mutual Fund Taxation
├── investment-for-beginners.html            # Strategy: Beginner's Guide
│
├── investor-resources.html                  # Resources & Downloads Hub
├── sip-calculator.html                      # Interactive SIP Calculator
├── lumpsum-calculator.html                  # Interactive Lump Sum Calculator
├── goal-planning-calculator.html            # Interactive Goal Calculator
├── risk-profile-questionnaire.html          # Interactive Risk Questionnaire
├── consultation.html                        # 3-Step Consultation Enquiry
├── corporate-investment-planning.html       # Corporate Financial Literacy
│
├── disclosures.html                         # Regulatory Disclosures & Model Guide
├── privacy-policy.html                      # Privacy Policy (DPDPA Compliant)
├── terms-and-conditions.html                # Terms of Use
├── disclaimer.html                          # Statutory Financial Disclaimers
├── cookie-policy.html                       # Cookie & Privacy Policy
│
├── sitemap.xml                              # XML Sitemap covering all 54 pages
├── robots.txt                               # Search engine crawler directives
├── IMAGE-GENERATION-GUIDE.md                # 56 Google Flow Prompts & specs
├── README.md                                # Master documentation & deployment guide
│
└── assets/
    ├── css/
    │   ├── style.css                        # Design system, variables, layouts, components
    │   ├── responsive.css                   # Breakpoints (1200px, 992px, 768px, 480px)
    │   └── animations.css                   # Keyframe animations, reveal classes, reduced motion
    ├── js/
    │   ├── main.js                          # Sticky header, scroll reveal, back to top
    │   ├── navigation.js                    # Mobile drawer, dropdown accordions, keyboard trap
    │   ├── calculators.js                   # SIP, Lump Sum, Goal formulas & input sync
    │   ├── portfolio.js                     # Dynamic asset allocation model visualizer
    │   ├── forms.js                         # 3-step consultation wizard, contact validation
    │   └── faq.js                           # Accessible accordion expand/collapse
    ├── images/
    │   └── README.md                        # Placeholder workflow and replacement guide
    └── icons/                               # Vector iconography
```

---

## Interactive Components & Features

### Financial Calculators
Located in `assets/js/calculators.js`, featuring synchronized number inputs and range sliders:
* **SIP Calculator (`sip-calculator.html`)**:
  $$\text{Corpus} = P \times \frac{(1 + i)^n - 1}{i} \times (1 + i)$$
  *(where $P$ is monthly deposit, $i$ is periodic monthly rate $r / 12 / 100$, and $n$ is total months).*
* **Lump Sum Calculator (`lumpsum-calculator.html`)**:
  $$\text{Corpus} = P \times (1 + r / 100)^t$$
  *(where $P$ is initial investment, $r$ is annual return rate, and $t$ is tenure in years).*
* **Goal Planning Calculator (`goal-planning-calculator.html`)**:
  Calculates required monthly SIP to achieve a target future corpus given time horizon and anticipated return.

### Risk Education Questionnaire
Located on `risk-profile-questionnaire.html`:
* 5 structured multiple-choice questions assessing age horizon, market volatility reaction, loss tolerance, investment experience, and primary financial goal.
* Client-side scoring algorithm maps responses into one of three profiles:
  * **Conservative (Score 5–8)**: Emphasizes capital preservation, high debt allocation, and liquid funds.
  * **Moderate (Score 9–12)**: Balanced growth, hybrid funds, large-cap allocation, and debt cushion.
  * **Aggressive (Score 13–15)**: Long-term wealth creation, high equity allocation (flexi cap, mid cap), and high volatility absorption.

### Interactive Asset Allocation Switcher
Located on `asset-allocation.html` and managed by `assets/js/portfolio.js`:
* Toggle between **Conservative**, **Moderate**, and **Aggressive** investment allocations.
* Real-time dynamic CSS bar chart updates illustrating equity, debt, gold, and cash distributions.

### Three-Step Consultation Enquiry Form
Located on `consultation.html` and `contact.html` via `assets/js/forms.js`:
* **Step 1**: Investor Classification & Goals (New investor, Existing portfolio review, Retirement, Child education).
* **Step 2**: Investment Horizon & Preferred Mode (SIP, Lump sum, 1–3 years, 3–5 years, 5+ years).
* **Step 3**: Contact Verification (Name, Phone, Email, Preferred consultation time).
* **Security Guardrails**: Explicitly prevents input or collection of sensitive financial credentials (PAN, Aadhaar numbers, bank account numbers, or OTPs).

### FAQ Accordion & Navigation
* **Search & Filter**: Real-time keyword filtering across all 18+ FAQ questions on `faq.html`.
* **Mobile Drawer**: Responsive off-canvas navigation with accessible drawer backdrop and keyboard escape triggers.

---

## Hostinger Static Hosting Deployment Guide

The website is engineered for seamless deployment on **Hostinger Business Web Hosting, Cloud Hosting, or Premium Shared Hosting**.

### Prerequisites
* Active Hostinger hosting plan.
* Registered domain or subdomain mapped to your Hostinger account.
* Access to **hPanel** (Hostinger Control Panel).

---

### Method 1: Hostinger File Manager Upload (Recommended for Quick Deploy)

1. **Log in to hPanel**: Navigate to [hpanel.hostinger.com](https://hpanel.hostinger.com).
2. **Access File Manager**:
   * Under your hosting plan, find your domain name.
   * Click **Files** $\rightarrow$ **File Manager** (Files for `public_html`).
3. **Navigate to Document Root**:
   * Open the `public_html` directory.
   * If there is a default `default.php` file, delete or rename it.
4. **Prepare Website Zip**:
   * On your local computer, select all files in the project root (`index.html`, all 53 other `.html` files, `sitemap.xml`, `robots.txt`, and the `assets/` folder).
   * Right-click and compress into a single `.zip` archive (e.g., `mutual-fund-advisory.zip`).
5. **Upload & Extract**:
   * In Hostinger File Manager, click the **Upload** icon (top right) $\rightarrow$ **File** $\rightarrow$ select `mutual-fund-advisory.zip`.
   * Once uploaded, right-click `mutual-fund-advisory.zip` and select **Extract**.
   * Choose `public_html` as the target folder.
   * Delete the `.zip` file after extraction to keep the server clean.
6. **Verify File Placement**:
   Ensure `index.html` sits directly inside `public_html/index.html` (not nested inside a subfolder like `public_html/mutual-fund-advisory/index.html`).

---

### Method 2: FTP / SFTP Deployment (FileZilla or Cyberduck)

1. **Retrieve FTP Credentials**:
   * In hPanel, go to **Files** $\rightarrow$ **FTP Accounts**.
   * Note the **FTP Host**, **FTP Username**, **FTP Password**, and **Port** (`21` for FTP, `22` for SFTP).
2. **Connect via FTP Client**:
   * Open FileZilla.
   * Enter Host, Username, Password, Port $\rightarrow$ Click **Quickconnect**.
3. **Upload Files**:
   * On the Remote Site pane, navigate to `/public_html/`.
   * On the Local Site pane, select all project files and folders (`.html`, `sitemap.xml`, `robots.txt`, and `assets/`).
   * Drag and drop all items into `/public_html/`.
   * Wait for all transfers to complete.

---

### Method 3: Git Deployment via Hostinger Git Tool

1. Push your repository to GitHub, GitLab, or Bitbucket.
2. In hPanel, go to **Advanced** $\rightarrow$ **Git**.
3. Create a new repository link:
   * **Repository**: `https://github.com/your-username/mutual-fund-advisory.git`
   * **Branch**: `main`
   * **Install Path**: `public_html`
4. Click **Create** $\rightarrow$ Click **Deploy**.
5. Enable **Auto-Deployment** via Webhook so future git commits update the live website automatically.

---

### Apache .htaccess Configuration

To maximize Google PageSpeed scores, enable Gzip/Brotli compression, configure browser caching, enforce HTTPS, and implement security headers, create a file named `.htaccess` inside your `public_html` root:

```apache
# ----------------------------------------------------------------------
# Mutual Fund Advisory — Production Apache Configuration
# ----------------------------------------------------------------------

# 1. Force HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# 2. Browser Caching Rules (Expires Headers)
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresDefault "access plus 1 month"
    
    # HTML (keep short for frequent updates)
    ExpiresByType text/html "access plus 1 hour"
    
    # CSS, JavaScript
    ExpiresByType text/css "access plus 1 year"
    ExpiresByType application/javascript "access plus 1 year"
    ExpiresByType text/javascript "access plus 1 year"
    
    # Images & SVGs
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
    ExpiresByType image/svg+xml "access plus 1 year"
    ExpiresByType image/x-icon "access plus 1 year"
</IfModule>

# 3. Gzip / Deflate Compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/json
    AddOutputFilterByType DEFLATE image/svg+xml
</IfModule>

# 4. Security Headers
<IfModule mod_headers.c>
    Header set X-Content-Type-Options "nosniff"
    Header set X-Frame-Options "SAMEORIGIN"
    Header set X-XSS-Protection "1; mode=block"
    Header set Referrer-Policy "strict-origin-when-cross-origin"
    Header set Permissions-Policy "camera=(), microphone=(), geolocation=()"
</IfModule>

# 5. Custom 404 Error Document
ErrorDocument 404 /index.html
```

---

### SSL/TLS & Domain Activation

1. In hPanel, go to **Security** $\rightarrow$ **SSL**.
2. Activate **Free Let's Encrypt SSL** for your domain and www subdomain.
3. Toggle on **Force HTTPS**.
4. Check **DNS Management**: Ensure `@` and `www` A-records point to your Hostinger server IP address.

---

## Image Asset Workflow & Google Flow Generation

All 54 pages currently feature responsive architectural SVG/CSS image placeholders. Every placeholder displays the designated image title, recommended resolution, exact aspect ratio (`16:9` or `4:3`), and prompt hints without triggering 404 console errors or cumulative layout shifts (CLS).

### Master Generation Guide
Refer to [IMAGE-GENERATION-GUIDE.md](IMAGE-GENERATION-GUIDE.md) for **all 56 image specifications** and copy-ready Google Flow prompts.

### Replacement Workflow
1. Open [IMAGE-GENERATION-GUIDE.md](IMAGE-GENERATION-GUIDE.md).
2. Locate the prompt for the target image (e.g., `mutual-fund-hero-investment-planning.jpg`).
3. Paste the copy-ready prompt into **Google Flow** or your chosen high-resolution image generator.
4. Export the resulting image in **WebP or high-quality JPG** format at the specified dimensions.
5. Save the generated image file into `assets/images/` using the exact filename specified in the guide.
6. In the corresponding HTML file, replace the placeholder element:
   ```html
   <!-- Before: Placeholder -->
   <div class="img-placeholder-wrapper" style="aspect-ratio: 16/9;">
     ...
   </div>

   <!-- After: Production Image -->
   <img src="assets/images/mutual-fund-hero-investment-planning.jpg" 
        alt="Wealth management consultation with advisor explaining mutual fund portfolio plan" 
        class="img-fluid rounded shadow" 
        loading="lazy" 
        width="1200" 
        height="675">
   ```

---

## Regulatory Safeguards & Disclaimer Standard

In compliance with Indian financial advertising codes (SEBI and Advertising Standards Council of India - ASCI):

1. **Mandatory Mutual Fund Statutory Warning**:
   Every page features the standardized statutory notice:
   > *"Mutual fund investments are subject to market risks, read all scheme related documents carefully."*
2. **No Guaranteed Return Claims**:
   The website strictly refrains from using phrases such as *"guaranteed wealth"*, *"risk-free investment"*, *"assured returns"*, or *"market-beating profits"*.
3. **Illustrative Calculations**:
   All calculator outputs clearly indicate:
   > *"Calculations shown are for educational and illustrative purposes only. They do not represent or guarantee future performance of any mutual fund scheme."*
4. **Data Privacy Protection**:
   Enquiry forms collect only high-level contact details for educational follow-up. They strictly forbid and reject sensitive identity documents (PAN, Aadhaar) or bank login credentials.

---

## Local Development & Maintenance

### Running Locally
Because the website uses pure static HTML/CSS/JS with zero build steps, you can open any file directly in a web browser, or serve it using any lightweight local HTTP server:

```powershell
# Option 1: Python HTTP Server (Recommended)
python -m http.server 8000

# Option 2: Node.js http-server (if installed)
npx http-server -p 8000

# Option 3: VS Code Live Server extension
# Right click index.html -> "Open with Live Server"
```

Open `http://localhost:8000` in your web browser.

### Automated Site Verification
A verification script is included to validate HTML syntax, ensure zero broken internal links, and inventory all image placeholders:

```powershell
python verify_site.py
```

Expected output:
```
Total HTML files: 54
Broken internal links: 0
Total placeholder instances: 56
Unique image filenames: 56
```

---

## License & Intellectual Property
Designed and developed for generic mutual fund advisory, wealth management, and investor education demonstration. All code and structural layouts are open for commercial adaptation in accordance with regulatory registration guidelines.
