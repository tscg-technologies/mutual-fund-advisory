"""
Generate 14 Mutual Fund Category Pages
"""

from templates import render_html_page, make_placeholder

CATEGORY_DEFS = {
    "equity-mutual-funds.html": {
        "title": "Equity Mutual Funds | Capital Growth & Equity Market Exposure",
        "name": "Equity Mutual Funds",
        "badge": "Equity",
        "tag_class": "badge-equity",
        "placeholder_img": "mutual-fund-equity-investment.jpg",
        "placeholder_title": "Equity Market Research & Stock Selection",
        "prompt_hint": "An equity portfolio manager analyzing Indian corporate earnings and growth trends.",
        "meta_desc": "Comprehensive educational guide to equity mutual funds in India: equity securities, market volatility, market caps, long-term horizon, and SEBI regulations.",
        "definition": "Equity mutual funds are collective investment schemes mandated by SEBI to invest a minimum of 65% of their total assets in equity and equity-related securities of listed companies.",
        "how_works": "The scheme pools money from investors to purchase shares of companies across diverse sectors. As the underlying businesses expand earnings and their share prices appreciate, the scheme's Net Asset Value (NAV) increases. Schemes may also receive dividends, which are reinvested or paid out depending on the plan chosen.",
        "objective": "To achieve long-term capital appreciation by participating in corporate India's economic expansion, outperforming consumer inflation over multi-year cycles.",
        "risk_profile": "High to Very High. Subject to equity market volatility, macroeconomic cycles, and company-specific earnings fluctuations.",
        "horizon": "Minimum 5 to 7 years. Equities require sufficient time to smooth out short-term market corrections and allow compounding to work.",
        "portfolio_traits": "Diversified across 30 to 70 companies, multiple sectors (financials, technology, healthcare, manufacturing), with varying weightings according to the scheme's mandate.",
        "important_risks": "Market drawdowns during economic recessions, sector underperformance, corporate governance issues in specific holdings, and elevated short-term volatility.",
        "costs_liquidity": "Total Expense Ratios typically range from 0.5% to 2.25% depending on Direct vs Regular plan. Liquidity is high with T+2 redemption payouts, though exit loads (usually 1% if redeemed within 1 year) may apply.",
        "questions_to_ask": [
            "What is my time horizon? Can I remain invested without liquidating for at least 5 years?",
            "Can I tolerate a temporary paper drop of 15% to 25% without panic selling?",
            "Does the scheme's market-cap focus (large, mid, small) align with my overall risk tolerance?"
        ],
        "related": [
            ("Large Cap Funds", "large-cap-funds.html"),
            ("Flexi Cap Funds", "flexi-cap-funds.html"),
            ("Index Funds", "index-funds.html"),
            ("ELSS", "ELSS.html")
        ]
    },

    "debt-mutual-funds.html": {
        "title": "Debt Mutual Funds | Fixed Income & Capital Preservation",
        "name": "Debt Mutual Funds",
        "badge": "Fixed Income",
        "tag_class": "badge-debt",
        "placeholder_img": "mutual-fund-debt-investment.jpg",
        "placeholder_title": "Fixed Income Yield Curve & Bond Research",
        "prompt_hint": "A debt fund manager evaluating sovereign yield curves, credit ratings, and interest rate movements.",
        "meta_desc": "Learn about debt mutual funds in India: government securities, corporate bonds, credit risk, interest rate risk, duration, and liquidity concepts.",
        "definition": "Debt mutual funds invest primarily in fixed-income securities, such as Government of India Bonds (G-Secs), Treasury Bills, State Development Loans (SDLs), corporate bonds, debentures, and commercial papers.",
        "how_works": "The fund lends capital to governments and corporate entities in exchange for periodic interest (coupon) payments and principal repayment at maturity. The fund's NAV reflects both regular accrued interest and capital gains or losses caused by interest rate fluctuations in the bond market.",
        "objective": "To generate regular income and provide capital stability with lower day-to-day volatility compared to equity markets.",
        "risk_profile": "Low to Moderate. Although safer than equities, debt funds carry interest rate risk, credit/default risk, and liquidity risk. They are NOT risk-free or guaranteed products.",
        "horizon": "From 1 day (overnight funds) to 3+ years (banking & PSU, corporate bond, or dynamic bond funds) depending on scheme duration.",
        "portfolio_traits": "Constructed with bonds carrying defined maturities and credit ratings (AAA, AA, A, sovereign). Regulated Macaulay duration dictates interest rate sensitivity.",
        "important_risks": "Interest rate risk (bond prices drop when RBI hikes interest rates) and credit default risk (issuers failing to honor coupon or principal repayments).",
        "costs_liquidity": "TERs are generally lower than equity funds (0.15% to 1.5%). Redemption proceeds are typically settled within T+1 or T+2 working days.",
        "questions_to_ask": [
            "Does the scheme's Macaulay duration match my investment horizon?",
            "What is the average credit quality of the underlying corporate portfolio?",
            "Am I aware of the current tax treatment of debt mutual funds under the Income Tax Act?"
        ],
        "related": [
            ("Liquid Funds", "liquid-funds.html"),
            ("Overnight Funds", "overnight-funds.html"),
            ("Hybrid Mutual Funds", "hybrid-mutual-funds.html"),
            ("Asset Allocation", "asset-allocation.html")
        ]
    },

    "hybrid-mutual-funds.html": {
        "title": "Hybrid Mutual Funds | Multi-Asset Blended Investing",
        "name": "Hybrid Mutual Funds",
        "badge": "Multi-Asset",
        "tag_class": "badge-hybrid",
        "placeholder_img": "mutual-fund-hybrid-allocation.jpg",
        "placeholder_title": "Multi-Asset Allocation & Hedging Dynamics",
        "prompt_hint": "Interactive split illustration showing equities, bonds, and cash components functioning in harmony.",
        "meta_desc": "Explore hybrid mutual funds in India: balanced advantage, aggressive hybrid, multi-asset allocation, risk moderation, and portfolio rebalancing.",
        "definition": "Hybrid mutual funds invest simultaneously in more than one asset class—typically combining equities and debt instruments, and occasionally gold or real estate investment trusts (REITs).",
        "how_works": "The fund manager allocates capital across growth-seeking equity shares and stability-focused debt securities according to predefined mandates. In Dynamic Asset Allocation (Balanced Advantage) funds, the ratio shifts automatically based on market valuation metrics (P/E, P/B, trend indicators).",
        "objective": "To achieve long-term capital appreciation while curbing downside volatility during turbulent equity market drawdowns.",
        "risk_profile": "Moderate to High. Lower volatility than pure equity funds, but higher volatility than pure debt instruments.",
        "horizon": "3 to 5 years. Sufficient time for the dual-engine strategy to capture equity rallies and cushion downward corrections.",
        "portfolio_traits": "Blended equity-debt holdings. Aggressive hybrid schemes hold 65-80% in equity; conservative hybrid schemes hold 75-90% in debt.",
        "important_risks": "Equity market drawdowns impacting the equity portion, alongside credit and interest rate sensitivity in the fixed-income portion.",
        "costs_liquidity": "TERs typically range from 0.8% to 2.10%. Exit loads of 1% commonly apply if more than 10-12% of units are redeemed within 1 year.",
        "questions_to_ask": [
            "Is the scheme an aggressive, conservative, or dynamic asset allocation (balanced advantage) fund?",
            "How does the scheme determine its asset reallocation triggers?",
            "What is the scheme's tax classification based on its average equity holding?"
        ],
        "related": [
            ("Equity Mutual Funds", "equity-mutual-funds.html"),
            ("Debt Mutual Funds", "debt-mutual-funds.html"),
            ("Asset Allocation", "asset-allocation.html"),
            ("Risk Management", "risk-management.html")
        ]
    },

    "index-funds.html": {
        "title": "Index Funds & ETFs | Low-Cost Passive Investment",
        "name": "Index Funds",
        "badge": "Passive Index",
        "tag_class": "badge-passive",
        "placeholder_img": "mutual-fund-index-tracking.jpg",
        "placeholder_title": "Benchmark Index Tracking & Quantitative Modeling",
        "prompt_hint": "Digital dashboard tracking Nifty 50 and Sensex benchmarks against index fund replication accuracy.",
        "meta_desc": "Understand passive index funds in India: Nifty 50, Sensex, tracking error, low expense ratios, and rule-based portfolio construction.",
        "definition": "Index funds are passively managed mutual funds designed to mirror the composition and performance of a specific market index, such as the Nifty 50, BSE Sensex, or Nifty Next 50.",
        "how_works": "Unlike active funds where a fund manager picks stocks to beat the benchmark, an index fund manager invests in the exact same companies with the exact same weightings as the underlying index, rebalancing only when the index constituents change.",
        "objective": "To deliver returns that closely match the total return of the benchmark index before deducting scheme expenses, without taking active manager risk.",
        "risk_profile": "High. The fund carries 100% of the market risk of the underlying index. If the index falls 20%, the fund NAV will also drop approximately 20%.",
        "horizon": "5+ years. Designed for long-term investors seeking broad market participation.",
        "portfolio_traits": "Zero stock selection bias. High transparency, identical stock holdings to benchmark, and minimal portfolio turnover.",
        "important_risks": "Systemic market risk and 'tracking error'—the mathematical difference between scheme returns and index performance due to cash drag, expenses, and corporate action timings.",
        "costs_liquidity": "Very low Total Expense Ratios (often 0.10% to 0.40% for direct plans). Highly liquid with standard mutual fund redemption mechanics.",
        "questions_to_ask": [
            "What is the historical tracking error and tracking difference of the scheme?",
            "Which benchmark index does the scheme replicate?",
            "Am I comfortable accepting exact market returns without the possibility of active alpha?"
        ],
        "related": [
            ("Large Cap Funds", "large-cap-funds.html"),
            ("Flexi Cap Funds", "flexi-cap-funds.html"),
            ("Expense Ratio", "expense-ratio.html"),
            ("SIP Investment", "sip-investment.html")
        ]
    },

    "large-cap-funds.html": {
        "title": "Large Cap Funds | Bluechip Equity Market Leaders",
        "name": "Large Cap Funds",
        "badge": "Top 100",
        "tag_class": "badge-equity",
        "placeholder_img": "mutual-fund-large-cap-bluechip.jpg",
        "placeholder_title": "Bluechip Corporate Leadership & Steady Growth",
        "prompt_hint": "Panoramic view of modern financial district representing established corporate conglomerates.",
        "meta_desc": "Explore large cap mutual funds in India: top 100 companies by market capitalization, established business models, resilience, and volatility characteristics.",
        "definition": "Large cap mutual funds are mandated by SEBI to invest at least 80% of their total assets in the equity shares of the top 100 companies ranked by full market capitalization in India.",
        "how_works": "These funds invest in well-established industry leaders—often referred to as 'bluechip' companies. These enterprises typically have strong balance sheets, institutional governance, dominant market share, and steady dividend histories.",
        "objective": "To generate steady capital appreciation with comparatively lower volatility than mid or small cap equity funds over multi-year cycles.",
        "risk_profile": "Moderate-High. While less volatile than smaller-cap companies, they remain fully exposed to overall equity market drawdowns.",
        "horizon": "5+ years. Ideal core holding for equity investors building a foundational wealth portfolio.",
        "portfolio_traits": "Concentrated in prominent sectors like banking, IT, energy, consumer staples, and auto manufacturing.",
        "important_risks": "Macroeconomic market cycles, systemic corrections, and active fund manager underperformance relative to low-cost passive indices.",
        "costs_liquidity": "High liquidity due to deep trading volumes in underlying stocks. TERs range from 0.8% to 2.15%. Standard 1% exit load for 1 year.",
        "questions_to_ask": [
            "Has the active large-cap scheme consistently beaten its benchmark index over 5 and 7-year rolling periods?",
            "What is the fund manager's investment style (growth vs value orientation)?",
            "How does this holding complement my existing index fund or mid-cap allocations?"
        ],
        "related": [
            ("Index Funds", "index-funds.html"),
            ("Mid Cap Funds", "mid-cap-funds.html"),
            ("Flexi Cap Funds", "flexi-cap-funds.html"),
            ("Equity Mutual Funds", "equity-mutual-funds.html")
        ]
    },

    "mid-cap-funds.html": {
        "title": "Mid Cap Funds | Growth-Oriented Emerging Companies",
        "name": "Mid Cap Funds",
        "badge": "Ranks 101-250",
        "tag_class": "badge-equity",
        "placeholder_img": "mutual-fund-mid-cap-growth.jpg",
        "placeholder_title": "Mid-Sized Corporate Expansion & Market Penetration",
        "prompt_hint": "Modern industrial manufacturing facility symbolizing growing mid-tier commercial enterprises.",
        "meta_desc": "Discover mid cap mutual funds in India: companies ranked 101st to 250th by market cap, higher growth potential, cyclical swings, and investment horizons.",
        "definition": "Mid cap mutual funds must invest at least 65% of their total portfolio in companies ranked from 101st to 250th in terms of full market capitalization.",
        "how_works": "Mid-cap companies are generally beyond their embryonic stage but have significant runway for commercial expansion. When an agile mid-sized business successfully expands, its stock price can appreciate substantially, boosting the scheme's NAV.",
        "objective": "To generate higher long-term capital compounding by capturing the transition of mid-sized firms into industry leaders.",
        "risk_profile": "High. Mid caps experience greater price swings, lower liquidity during market panics, and higher vulnerability to economic downturns than large caps.",
        "horizon": "7+ years. Essential to navigate full economic business cycles and endure interim drawdowns.",
        "portfolio_traits": "Diverse exposure to specialty chemicals, capital goods, emerging consumer brands, and niche technology providers.",
        "important_risks": "Severe cyclical corrections during bear markets, earnings volatility, and institutional liquidity crunches during risk-off regimes.",
        "costs_liquidity": "Moderate liquidity. TERs typically 0.9% to 2.25%. Standard exit loads apply for redemption within 12 months.",
        "questions_to_ask": [
            "Do I have a minimum 7-year time horizon to accommodate sharper market swings?",
            "What proportion of my total equity portfolio is allocated to mid and small caps?",
            "How experienced is the fund management team in mid-market credit and equity research?"
        ],
        "related": [
            ("Large Cap Funds", "large-cap-funds.html"),
            ("Small Cap Funds", "small-cap-funds.html"),
            ("Flexi Cap Funds", "flexi-cap-funds.html"),
            ("SIP Investment", "sip-investment.html")
        ]
    },

    "small-cap-funds.html": {
        "title": "Small Cap Funds | High-Growth Emerging Enterprises",
        "name": "Small Cap Funds",
        "badge": "Ranks 251+",
        "tag_class": "badge-equity",
        "placeholder_img": "mutual-fund-small-cap-enterprises.jpg",
        "placeholder_title": "Early-Stage Enterprises & High Compounding Potential",
        "prompt_hint": "Tech startup laboratory showcasing high-innovation emerging businesses in Indian industry.",
        "meta_desc": "Comprehensive guide to small cap mutual funds in India: stocks ranked 251st onwards, high volatility, growth drivers, liquidity, and extended time horizons.",
        "definition": "Small cap mutual funds are required by SEBI to invest at least 65% of their assets in companies ranked 251st and beyond by full market capitalization.",
        "how_works": "Small caps are early-stage or niche companies with smaller operational scale. While many small businesses remain volatile, successful ones can scale exponentially, yielding high compounding returns for patient long-term investors.",
        "objective": "To achieve superior long-term capital compounding by identifying high-potential early-stage companies before they are widely discovered by institutional markets.",
        "risk_profile": "Very High. Small cap stocks can experience protracted drawdowns of 30% to 50% during bear phases and take several years to recover.",
        "horizon": "7 to 10 years minimum. Not suitable for short or medium-term financial goals.",
        "portfolio_traits": "Widely diversified across 60 to 100+ small-cap stocks to minimize single-company blow-up risk, alongside tactical cash buffers for liquidity.",
        "important_risks": "Illiquidity risk (difficulty selling large blocks during panics), governance risks, higher failure rates among smaller firms, and sharp price volatility.",
        "costs_liquidity": "Liquidity can be constrained during bear phases. Some funds temporarily restrict lump sum inflows to protect existing investors.",
        "questions_to_ask": [
            "Can I stomach a 40% paper drawdown without halting my systematic SIP investments?",
            "Is my small-cap allocation capped at a prudent percentage (e.g. 10-20%) of my overall portfolio?",
            "Does the scheme have a proven risk-management framework to avoid illiquid holdings?"
        ],
        "related": [
            ("Mid Cap Funds", "mid-cap-funds.html"),
            ("Large Cap Funds", "large-cap-funds.html"),
            ("Flexi Cap Funds", "flexi-cap-funds.html"),
            ("Risk Management", "risk-management.html")
        ]
    },

    "flexi-cap-funds.html": {
        "title": "Flexi Cap Funds | Dynamic Multi-Cap Allocation Discretion",
        "name": "Flexi Cap Funds",
        "badge": "Unconstrained",
        "tag_class": "badge-equity",
        "placeholder_img": "mutual-fund-flexi-cap-dynamic.jpg",
        "placeholder_title": "Agile Capital Allocation Across Cap Horizons",
        "prompt_hint": "A wealth management strategist toggling dynamic weights between large, mid, and small cap sectors.",
        "meta_desc": "Understand flexi cap mutual funds: minimum 65% equity allocation with complete fund manager discretion across large, mid, and small capitalization stocks.",
        "definition": "Flexi cap mutual funds are equity schemes that must invest at least 65% of their total assets in equity shares, with total freedom to allocate across large, mid, and small cap companies without fixed sub-limits.",
        "how_works": "The fund manager exercises tactical agility. If large caps appear richly valued, the manager can tilt the portfolio toward undervalued mid caps, and vice versa when macro risks favor defensive bluechips.",
        "objective": "To generate long-term capital growth by capitalizing on relative valuation mispricings across all market capitalizations.",
        "risk_profile": "High. The risk level depends on how heavily the fund manager tilts the portfolio toward volatile mid/small caps versus stable large caps.",
        "horizon": "5+ years. Recommended as a cornerstone holding for general long-term wealth accumulation.",
        "portfolio_traits": "Typically holds 60-75% in large caps for liquidity and stability, and 25-40% in mid/small caps for accelerated alpha generation.",
        "important_risks": "Fund manager selection risk—the danger that the manager shifts into small caps right before a downturn or into cash during a rally.",
        "costs_liquidity": "High overall liquidity. TERs range from 0.8% to 2.2%. Standard 1% exit load for 1 year.",
        "questions_to_ask": [
            "What has been the historical allocation split (large vs mid vs small) of the scheme over different market cycles?",
            "Does the fund manager follow a growth, value, or blend investment discipline?",
            "How does this flexi-cap fund overlap with my existing mutual fund schemes?"
        ],
        "related": [
            ("Equity Mutual Funds", "equity-mutual-funds.html"),
            ("Large Cap Funds", "large-cap-funds.html"),
            ("Mid Cap Funds", "mid-cap-funds.html"),
            ("Portfolio Review", "portfolio-review.html")
        ]
    },

    "ELSS.html": {
        "title": "ELSS Tax Saving Mutual Funds | Section 80C & 3-Year Lock-In",
        "name": "ELSS (Tax Saving Mutual Funds)",
        "badge": "Section 80C",
        "tag_class": "badge-tax",
        "placeholder_img": "mutual-fund-elss-tax-saving.jpg",
        "placeholder_title": "Tax Optimization & Long-Term Compounding Synergy",
        "prompt_hint": "Financial planning desk with tax calculation sheets, calendar deadlines, and investment growth projections.",
        "meta_desc": "Comprehensive guide to ELSS (Equity Linked Savings Schemes): 3-year statutory lock-in, Section 80C tax deduction concepts, and equity market risk.",
        "definition": "Equity Linked Savings Schemes (ELSS) are diversified equity mutual funds that qualify for tax deduction under Section 80C of the Income Tax Act, 1961 (under the Old Tax Regime), carrying a statutory lock-in period of 3 years.",
        "how_works": "Investments up to ₹1.5 lakh per financial year in ELSS can be claimed as a deduction under Section 80C. The pooled capital is invested in a diversified portfolio across large, mid, and small cap companies. Every individual SIP installment has its own 36-month lock-in period.",
        "objective": "To achieve long-term capital compounding while providing immediate tax savings benefits under eligible tax regimes.",
        "risk_profile": "High. Despite the tax benefit, ELSS is a 100% market-linked equity product subject to regular market volatility.",
        "horizon": "3 to 5+ years. Although units unlock after 3 years, remaining invested for 5+ years is generally advisable for equity compounding.",
        "portfolio_traits": "Similar to flexi cap funds; diversified across 40-70 companies without market cap restrictions.",
        "important_risks": "Capital lock-in (units cannot be redeemed, switched, or pledged under any circumstances before 3 years) and equity market volatility.",
        "costs_liquidity": "Zero liquidity during the first 36 months of each unit. No exit loads apply once the 3-year lock-in expires.",
        "questions_to_ask": [
            "Does my tax plan follow the Old or New Tax Regime? (Section 80C deductions are not available under the New Tax Regime).",
            "Am I aware that each monthly SIP installment is locked for exactly 36 months from its specific allotment date?",
            "Do I have liquid emergency funds so I do not need the locked capital unexpectedly?"
        ],
        "related": [
            ("Equity Mutual Funds", "equity-mutual-funds.html"),
            ("Flexi Cap Funds", "flexi-cap-funds.html"),
            ("Investment Taxation", "investment-taxation.html"),
            ("SIP Investment", "sip-investment.html")
        ]
    },

    "liquid-funds.html": {
        "title": "Liquid Mutual Funds | Short-Term Cash & Emergency Reserves",
        "name": "Liquid Mutual Funds",
        "badge": "Liquidity",
        "tag_class": "badge-liquid",
        "placeholder_img": "mutual-fund-liquid-cash-management.jpg",
        "placeholder_title": "Cash Management & Short-Duration Money Markets",
        "prompt_hint": "Corporate treasury desk monitoring commercial paper yields, call money rates, and daily settlement liquidity.",
        "meta_desc": "Learn about liquid mutual funds in India: debt securities up to 91-day maturity, capital safety, emergency fund parking, and 7-day graded exit loads.",
        "definition": "Liquid mutual funds are open-ended debt mutual fund schemes that invest exclusively in debt and money market securities with residual maturities of up to 91 days.",
        "how_works": "The scheme invests in ultra-short securities like Treasury Bills (T-Bills), Commercial Papers (CPs), Certificates of Deposit (CDs), and Tri-party Repos (TREPS). Returns stem from the accrual of short-term interest, resulting in stable, gradual NAV growth.",
        "objective": "To provide high liquidity, relative capital stability, and optimal yields on temporary surplus funds compared to standard savings accounts.",
        "risk_profile": "Low. Very low interest rate risk due to short maturity, but still subject to credit risk if an issuer defaults.",
        "horizon": "1 day to 3 months. Prime instrument for emergency funds, contingency cash, and Systematic Transfer Plan (STP) feeder accounts.",
        "portfolio_traits": "High concentration in sovereign and AAA/A1+ rated money market instruments with mark-to-market accounting.",
        "important_risks": "Credit default risk of corporate paper and sudden macro liquidity contractions.",
        "costs_liquidity": "Extremely high liquidity. Redemptions are processed within T+1 working days (with instant redemption facilities up to ₹50,000 in eligible schemes). A graded exit load applies for redemptions within the first 7 days.",
        "questions_to_ask": [
            "What is the credit rating distribution of the commercial papers held in the portfolio?",
            "Am I aware of the 7-day graded exit load structure?",
            "Is this fund being used as a temporary holding zone or a long-term investment?"
        ],
        "related": [
            ("Overnight Funds", "overnight-funds.html"),
            ("Debt Mutual Funds", "debt-mutual-funds.html"),
            ("Goal-Based Investing", "goal-based-investing.html"),
            ("Exit Load", "exit-load.html")
        ]
    },

    "overnight-funds.html": {
        "title": "Overnight Mutual Funds | 1-Day Maturity Fixed Income",
        "name": "Overnight Mutual Funds",
        "badge": "1-Day Maturity",
        "tag_class": "badge-liquid",
        "placeholder_img": "mutual-fund-overnight-money-markets.jpg",
        "placeholder_title": "Overnight Money Markets & Collateralized Borrowing",
        "prompt_hint": "RBI monetary policy graphics showing repo rates, overnight interbank borrowing, and sovereign treasury bills.",
        "meta_desc": "Understand overnight mutual funds in India: 1-day maturity instruments, lowest interest rate and credit risk, zero exit load, and corporate cash parking.",
        "definition": "Overnight mutual funds invest in debt securities that mature in just one business day, such as Tri-party Repos (TREPS), Reverse Repos, and call money markets.",
        "how_works": "Capital is lent out each day against collateral and repaid the following morning with interest. The scheme rolls over this process daily, virtually eliminating bond price volatility.",
        "objective": "To offer maximum capital safety and day-to-day liquidity for very short-term cash surpluses.",
        "risk_profile": "Lowest risk in the mutual fund spectrum. Virtually immune to interest rate swings and corporate credit downgrades.",
        "horizon": "1 day to 1 week. Ideal for corporate treasuries, business operational cash, or parking funds for a few days.",
        "portfolio_traits": "100% allocated to 1-day maturity instruments backed by Government securities collateral.",
        "important_risks": "Reinvestment risk (yields fluctuate daily with the prevailing interbank repo rate). Returns may trail inflation.",
        "costs_liquidity": "Minimal expense ratios (often 0.05% to 0.15%). Zero exit load regardless of redemption timing. T+1 redemption settlement.",
        "questions_to_ask": [
            "Do I require funds back within less than 7 days?",
            "How does the overnight yield compare to my current savings bank interest?",
            "Are there any transaction charges associated with my platform for short-term parking?"
        ],
        "related": [
            ("Liquid Funds", "liquid-funds.html"),
            ("Debt Mutual Funds", "debt-mutual-funds.html"),
            ("Expense Ratio", "expense-ratio.html"),
            ("Financial Planning", "financial-planning.html")
        ]
    },

    "international-funds.html": {
        "title": "International Mutual Funds | Global Geographic Diversification",
        "name": "International Mutual Funds",
        "badge": "Global Equities",
        "tag_class": "badge-equity",
        "placeholder_img": "mutual-fund-international-global-markets.jpg",
        "placeholder_title": "Global Stock Exchanges & Currency Diversification",
        "prompt_hint": "A dual world map connecting Wall Street, European exchanges, and Indian markets with currency vectors.",
        "meta_desc": "Explore international mutual funds in India: investing in global equities, currency depreciation dynamics, geographic risk, and tax treatment.",
        "definition": "International mutual funds (also known as overseas funds or feeder funds) invest in stocks of companies listed outside India or in units of foreign mutual funds and exchange-traded funds (ETFs).",
        "how_works": "Indian investors contribute in Rupees. The scheme converts the capital into foreign currency (such as USD or EUR) to invest in international markets (e.g. US tech giants, European healthcare, or Asian manufacturing leaders).",
        "objective": "To achieve geographic diversification, tap into global technological innovators not listed in India, and benefit from potential rupee currency depreciation.",
        "risk_profile": "High. In addition to equity market volatility, international funds carry currency exchange rate risk and foreign geopolitical/regulatory risks.",
        "horizon": "5 to 7+ years. Allows time for foreign business cycles and currency trends to unfold.",
        "portfolio_traits": "Targeted exposure to the S&P 500, Nasdaq 100, global thematic innovators, or emerging market clusters.",
        "important_risks": "Currency volatility (if the Rupee strengthens against the USD, fund returns decline), country-specific regulatory restrictions, and overseas investment quota limits mandated by RBI/SEBI.",
        "costs_liquidity": "Can involve a two-tier fee structure (feeder fund expense plus underlying master fund expense). Taxed according to current non-equity rules.",
        "questions_to_ask": [
            "Are fresh investments currently permitted under prevailing RBI industry-wide overseas investment limits?",
            "What is the underlying country and sector concentration of the master fund?",
            "How does currency fluctuation impact my net INR returns?"
        ],
        "related": [
            ("Equity Mutual Funds", "equity-mutual-funds.html"),
            ("Index Funds", "index-funds.html"),
            ("Diversification", "diversification.html"),
            ("Investment Taxation", "investment-taxation.html")
        ]
    },

    "fund-of-funds.html": {
        "title": "Fund of Funds (FoF) | Multi-Manager Collective Investing",
        "name": "Fund of Funds (FoF)",
        "badge": "FoF Architecture",
        "tag_class": "badge-passive",
        "placeholder_img": "mutual-fund-fof-architecture.jpg",
        "placeholder_title": "Multi-Manager Scheme Layering & Asset Allocation",
        "prompt_hint": "Architectural diagram showing a master fund investing in multiple specialized underlying schemes.",
        "meta_desc": "Learn about Fund of Funds (FoF) in India: multi-manager diversification, asset allocation FoFs, gold FoFs, expense layering, and suitability.",
        "definition": "A Fund of Funds (FoF) is a mutual fund scheme that invests its assets in units of other mutual fund schemes, rather than directly holding individual shares or bonds.",
        "how_works": "The FoF manager selects a basket of high-performing underlying schemes across various AMCs or asset classes. For example, a Gold FoF invests in Gold ETFs, while an Asset Allocation FoF might hold 60% in an equity fund and 40% in a debt fund.",
        "objective": "To provide convenient single-ticket access to a diversified basket of underlying managers, specialized asset classes (like gold), or overseas strategies.",
        "risk_profile": "Dependent on the underlying funds. An equity FoF is High Risk, while a debt FoF is Moderate Risk.",
        "horizon": "3 to 5+ years depending on the underlying asset composition.",
        "portfolio_traits": "Holding list comprises other mutual fund scheme unit holdings rather than individual company stocks.",
        "important_risks": "Double expense ratio impact (the FoF charges an expense, and the underlying schemes also deduct their own TERs, subject to SEBI aggregate caps).",
        "costs_liquidity": "SEBI regulates total combined expense caps. Settlement may take an extra day (T+3) because underlying scheme units must be liquidated first.",
        "questions_to_ask": [
            "What is the total combined expense ratio of the FoF and its underlying schemes?",
            "Could I achieve the same asset allocation more cost-effectively by investing in the underlying funds directly?",
            "What is the tax status of this specific FoF scheme?"
        ],
        "related": [
            ("International Funds", "international-funds.html"),
            ("Hybrid Mutual Funds", "hybrid-mutual-funds.html"),
            ("Expense Ratio", "expense-ratio.html"),
            ("Asset Allocation", "asset-allocation.html")
        ]
    },

    "sectoral-thematic-funds.html": {
        "title": "Sectoral & Thematic Funds | Focused Industry Exposure",
        "name": "Sectoral and Thematic Funds",
        "badge": "Focused Theme",
        "tag_class": "badge-tax",
        "placeholder_img": "mutual-fund-sectoral-thematic-trends.jpg",
        "placeholder_title": "Sector Concentration & Cyclical Industry Trends",
        "prompt_hint": "Infographic displaying industry sectors: banking, pharma, infrastructure, and green energy cycles.",
        "meta_desc": "Comprehensive guide to sectoral and thematic mutual funds in India: concentration risk, cyclical timing, lack of diversification, and suitability.",
        "definition": "Sectoral funds invest minimum 80% in a single specific industry (such as Banking, Pharmaceuticals, or Technology), while Thematic funds invest across multiple sectors aligned around a common macro trend (such as Manufacturing, ESG, or Infrastructure).",
        "how_works": "When an entire sector experiences tailwinds (e.g. rising pharma demand or infrastructure spending), these funds can generate substantial returns. Conversely, when the sector enters a cyclical downturn, the fund has no leeway to diversify into other industries.",
        "objective": "To take tactical, high-conviction bets on specific macroeconomic themes expected to outpace broader market indices.",
        "risk_profile": "Very High. Extreme concentration risk. A prolonged slump in that single sector can lead to multi-year underperformance regardless of overall market health.",
        "horizon": "Tactical (typically 3 to 7 years, but requires disciplined exit timing). Not suitable as a primary core portfolio holding.",
        "portfolio_traits": "Concentrated in 20-35 stocks belonging strictly to the targeted industry or thematic universe.",
        "important_risks": "Lack of diversification, regulatory policy changes affecting that specific sector, and severe cyclical drawdowns.",
        "costs_liquidity": "Standard equity mutual fund liquidity with T+2 payouts. TERs typically 1.0% to 2.25%. Standard exit loads apply.",
        "questions_to_ask": [
            "Do I have specialized knowledge or a strong thesis on why this specific sector will outperform?",
            "What is my planned exit strategy if the sector cycle peaks or reverses?",
            "Is my sectoral exposure limited to a small satellite allocation (e.g. &lt; 10%) of my total wealth?"
        ],
        "related": [
            ("Equity Mutual Funds", "equity-mutual-funds.html"),
            ("Flexi Cap Funds", "flexi-cap-funds.html"),
            ("Risk Management", "risk-management.html"),
            ("Diversification", "diversification.html")
        ]
    }
}

def build_category_pages():
    for filename, data in CATEGORY_DEFS.items():
        rel_links = "".join([f'<a href="{url}" class="btn btn-outline btn-sm">{lbl}</a>' for lbl, url in data["related"]])
        questions_html = "".join([f'<li style="margin-bottom: 0.75rem;"><strong>&bull;</strong> {q}</li>' for q in data["questions_to_ask"]])

        content = f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="category-badge {data['tag_class']} mb-2" style="font-size: 0.85rem; padding: 0.3rem 0.8rem;">{data['badge']} Category</span>
      <h1 class="page-banner-title">{data['name']}</h1>
      <p class="page-banner-desc">{data['definition']}</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Category Definition &amp; Mechanics</span>
          <h2 class="section-title">How {data['name']} Function</h2>
          <p class="mb-3">{data['how_works']}</p>
          <p>
            <strong>Primary Objective:</strong> {data['objective']}
          </p>
          <div class="regulatory-banner">
            <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <div>
              <strong>Regulatory Risk Disclosure:</strong> Investments in {data['name']} are subject to market risks. Read all scheme information documents (SID) and key information memorandums (KIM) carefully before committing capital.
            </div>
          </div>
        </div>

        <div>
          {make_placeholder(data['placeholder_img'], data['placeholder_title'], "4-3", data['prompt_hint'], "1000x750", f"{data['badge']} Visual")}
        </div>
      </div>

      <!-- Key Specifications Table -->
      <div class="section-header">
        <span class="section-tag tag-gold">Category Blueprint</span>
        <h2 class="section-title">Operational Characteristics</h2>
      </div>

      <div class="comparison-table-wrapper mb-5">
        <table class="comparison-table">
          <thead>
            <tr>
              <th style="width: 28%;">Parameter</th>
              <th>Category Standard &amp; SEBI Framework</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>General Risk Rating</strong></td>
              <td><span class="category-badge {data['tag_class']}">{data['risk_profile']}</span></td>
            </tr>
            <tr>
              <td><strong>Recommended Investment Horizon</strong></td>
              <td><strong>{data['horizon']}</strong></td>
            </tr>
            <tr>
              <td><strong>Portfolio Construction</strong></td>
              <td>{data['portfolio_traits']}</td>
            </tr>
            <tr>
              <td><strong>Key Risks to Monitor</strong></td>
              <td>{data['important_risks']}</td>
            </tr>
            <tr>
              <td><strong>Costs &amp; Liquidity Profile</strong></td>
              <td>{data['costs_liquidity']}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Questions to Ask -->
      <div class="card-grid-2 mb-5">
        <div class="feature-card" style="border-left: 4px solid var(--green-primary);">
          <h3 class="feature-card-title">Questions to Ask Before Investing</h3>
          <ul style="list-style: none; padding-left: 0; color: var(--text-body); margin-top: 1rem;">
            {questions_html}
          </ul>
        </div>

        <div class="feature-card" style="border-left: 4px solid var(--navy-primary);">
          <h3 class="feature-card-title">Related Mutual Fund Categories</h3>
          <p class="feature-card-text">Compare this scheme category with adjacent asset classes to optimize your asset allocation.</p>
          <div class="btn-group mt-3">
            {rel_links}
          </div>
        </div>
      </div>

      <!-- Bottom CTA Banner -->
      <div class="p-4 text-center" style="background: var(--bg-light); border-radius: var(--radius-lg); border: 1px solid var(--border-subtle);">
        <h3>Want to analyze how this category fits your financial roadmap?</h3>
        <p class="mb-3 text-muted">Use our interactive calculators or schedule an educational consultation session.</p>
        <div class="btn-group" style="justify-content: center;">
          <a href="sip-calculator.html" class="btn btn-outline">SIP Calculator</a>
          <a href="consultation.html" class="btn btn-primary">Request Consultation</a>
        </div>
      </div>
    </div>
  </section>
"""

        html = render_html_page(
            filename=filename,
            title=data["title"],
            meta_desc=data["meta_desc"],
            active_nav="funds",
            breadcrumbs=[("Mutual Funds", "mutual-funds.html"), (data["name"], "")],
            content_html=content
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {filename}")

if __name__ == "__main__":
    build_category_pages()
