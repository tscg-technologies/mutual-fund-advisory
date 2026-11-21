"""
Generate 16 Core Company Pages with Dedicated Image Placeholders
"""

from templates import render_html_page, make_placeholder

def build_core_pages():
    pages = {}

    # 1. index.html
    pages["index.html"] = {
        "title": "Mutual Fund Advisory | Wealth Management & Investor Education",
        "meta_desc": "Explore mutual fund education, SIP investment concepts, goal-based financial planning, asset allocation, and portfolio reviews for Indian investors.",
        "active_nav": "home",
        "breadcrumbs": [],
        "content": f"""
  <!-- Hero Section -->
  <section class="hero">
    <div class="container hero-grid">
      <div class="hero-content reveal-on-scroll">
        <div class="hero-badges-row">
          <span class="hero-feature-badge">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="#18A875"><circle cx="12" cy="12" r="10"/></svg>
            SEBI &amp; AMFI Regulatory Concepts
          </span>
          <span class="hero-feature-badge">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="#C6A15B"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            Unbiased Investor Education
          </span>
        </div>
        <h1>Make Your Financial Goals Part of Your Investment Journey</h1>
        <p class="hero-lead">
          Understand mutual funds, explore disciplined investment strategies, and build financial awareness through structured education, asset allocation, and goal-oriented planning.
        </p>
        <div class="btn-group">
          <a href="mutual-funds.html" class="btn btn-primary btn-lg">Explore Mutual Funds</a>
          <a href="sip-calculator.html" class="btn btn-outline-white btn-lg">Start Your Investment Journey</a>
        </div>
      </div>
      <div class="hero-media">
        {make_placeholder("mutual-fund-hero-investment-planning.jpg", "Strategic Financial Planning & Advisory", "16-9", "A senior wealth manager and client reviewing long-term portfolio allocation over tablet analytics.", "1200x675", "Hero Concept Visual")}
      </div>
    </div>
  </section>

  <!-- Quick Navigation Cards -->
  <section class="section section-light">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Quick Navigation</span>
        <h2 class="section-title">Essential Investment Pillars</h2>
        <p class="section-subtitle">Structured pathways designed to guide your journey from foundational understanding to disciplined wealth management.</p>
      </div>

      <div class="card-grid-4">
        <div class="feature-card reveal-on-scroll delay-100">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"/></svg>
          </div>
          <h3 class="feature-card-title">Explore Mutual Funds</h3>
          <p class="feature-card-text">Understand how professional fund managers pool capital to invest in diversified equities, debt, and hybrid securities.</p>
          <a href="mutual-funds.html" class="feature-card-link">Explore Fund Types &rarr;</a>
        </div>

        <div class="feature-card reveal-on-scroll delay-200">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <h3 class="feature-card-title">Understand SIPs</h3>
          <p class="feature-card-text">Learn how Systematic Investment Plans leverage rupee-cost averaging and compounding over changing market cycles.</p>
          <a href="sip-investment.html" class="feature-card-link">Understand SIPs &rarr;</a>
        </div>

        <div class="feature-card reveal-on-scroll delay-300">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          </div>
          <h3 class="feature-card-title">Plan Financial Goals</h3>
          <p class="feature-card-text">Map concrete life aspirations—retirement, child education, or home purchase—to appropriate investment time horizons.</p>
          <a href="goal-based-investing.html" class="feature-card-link">Map Goals &rarr;</a>
        </div>

        <div class="feature-card reveal-on-scroll delay-400">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          </div>
          <h3 class="feature-card-title">Learn Basics</h3>
          <p class="feature-card-text">Master Net Asset Value (NAV), Total Expense Ratio (TER), Exit Loads, and Riskometer disclosures before investing.</p>
          <a href="investment-for-beginners.html" class="feature-card-link">Start Learning &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Mutual Fund Categories Preview -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-gold">Broad Spectrum</span>
        <h2 class="section-title">Mutual Fund Categories in India</h2>
        <p class="section-subtitle">SEBI categorizes schemes into distinct buckets to help investors identify risk-return profiles suited to their objectives.</p>
      </div>

      <div class="card-grid-4">
        <a href="equity-mutual-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-equity">Equity</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Equity Funds</h4>
          <p class="category-card-desc">Invest primarily in equity stocks across large, mid, and small-cap companies for long-term capital compounding.</p>
          <div class="category-meta">
            <span>Risk: High</span>
            <span class="category-horizon">Horizon: 5+ Yrs</span>
          </div>
        </a>

        <a href="debt-mutual-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-debt">Debt</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Debt Funds</h4>
          <p class="category-card-desc">Invest in government securities, treasury bills, and corporate bonds prioritizing relative capital stability.</p>
          <div class="category-meta">
            <span>Risk: Moderate</span>
            <span class="category-horizon">Horizon: 1-3 Yrs</span>
          </div>
        </a>

        <a href="hybrid-mutual-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-hybrid">Hybrid</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Hybrid Funds</h4>
          <p class="category-card-desc">Combine equity and debt assets to balance growth potential with downside protection through dynamic asset allocation.</p>
          <div class="category-meta">
            <span>Risk: Mod-High</span>
            <span class="category-horizon">Horizon: 3-5 Yrs</span>
          </div>
        </a>

        <a href="index-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-passive">Passive</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Index Funds</h4>
          <p class="category-card-desc">Passively replicate broad market indices like Nifty 50 or BSE Sensex with low expense ratios and minimal tracking error.</p>
          <div class="category-meta">
            <span>Risk: Market Risk</span>
            <span class="category-horizon">Horizon: 5+ Yrs</span>
          </div>
        </a>

        <a href="ELSS.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-tax">Tax Saving</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">ELSS Funds</h4>
          <p class="category-card-desc">Equity-linked savings schemes offering tax deduction concepts under Section 80C with a statutory 3-year lock-in period.</p>
          <div class="category-meta">
            <span>Risk: High</span>
            <span class="category-horizon">Horizon: 3+ Yrs</span>
          </div>
        </a>

        <a href="liquid-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-liquid">Liquidity</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Liquid Funds</h4>
          <p class="category-card-desc">Invest in money market securities maturing within 91 days, suitable for parking emergency buffers or short-term surpluses.</p>
          <div class="category-meta">
            <span>Risk: Low</span>
            <span class="category-horizon">Horizon: 1-90 Days</span>
          </div>
        </a>

        <a href="international-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-equity">Global</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">International Funds</h4>
          <p class="category-card-desc">Provide geographic diversification by investing in global equity markets, tech leaders, and foreign index funds.</p>
          <div class="category-meta">
            <span>Risk: High</span>
            <span class="category-horizon">Horizon: 5+ Yrs</span>
          </div>
        </a>

        <a href="sectoral-thematic-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-tax">Thematic</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Sectoral Funds</h4>
          <p class="category-card-desc">Concentrate capital in specific sectors such as banking, pharma, or technology; involves elevated cyclical risk.</p>
          <div class="category-meta">
            <span>Risk: Very High</span>
            <span class="category-horizon">Horizon: Tactical</span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- Why Understand Mutual Funds Section -->
  <section class="section section-light">
    <div class="container">
      <div class="card-grid-2" style="align-items: center;">
        <div>
          <span class="section-tag">Core Principles</span>
          <h2 class="section-title">Why Understanding Mutual Funds Matters</h2>
          <p class="section-subtitle mb-4">Mutual funds are not guaranteed-return instruments. Thorough education protects investors from unrealistic expectations and market volatility panics.</p>

          <ul style="display: flex; flex-direction: column; gap: 1rem;">
            <li style="display: flex; gap: 0.85rem;">
              <div style="width: 24px; height: 24px; border-radius: 50%; background: var(--green-light); color: var(--green-deep); display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">&check;</div>
              <div>
                <strong>Different Investment Objectives:</strong> Each fund category serves distinct goals, whether capital protection, income distribution, or aggressive wealth compounding.
              </div>
            </li>
            <li style="display: flex; gap: 0.85rem;">
              <div style="width: 24px; height: 24px; border-radius: 50%; background: var(--green-light); color: var(--green-deep); display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">&check;</div>
              <div>
                <strong>Different Levels of Market Risk:</strong> Mutual funds reflect the volatility of underlying securities. NAV fluctuations are normal market characteristics, not failures.
              </div>
            </li>
            <li style="display: flex; gap: 0.85rem;">
              <div style="width: 24px; height: 24px; border-radius: 50%; background: var(--green-light); color: var(--green-deep); display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">&check;</div>
              <div>
                <strong>Professional Fund Management:</strong> Experienced portfolio managers and quantitative research teams conduct security analysis and statutory rebalancing.
              </div>
            </li>
            <li style="display: flex; gap: 0.85rem;">
              <div style="width: 24px; height: 24px; border-radius: 50%; background: var(--green-light); color: var(--green-deep); display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">&check;</div>
              <div>
                <strong>Cost Transparency:</strong> The Total Expense Ratio (TER) and exit load charges are legally mandated disclosures regulated by SEBI caps.
              </div>
            </li>
          </ul>
        </div>
        <div>
          {make_placeholder("mutual-fund-market-research.jpg", "Financial Analyst Reviewing Scheme Factsheets", "4-3", "An investment analyst reviewing SEBI factsheets, portfolio overlap metrics, and market risk graphs.", "1000x750", "Analysis & Research")}
        </div>
      </div>
    </div>
  </section>

  <!-- SIP Investment Section -->
  <section class="section">
    <div class="container">
      <div class="card-grid-2" style="align-items: center;">
        <div>
          {make_placeholder("mutual-fund-sip-investment.jpg", "Systematic Investment Planning Visual", "4-3", "A conceptual illustration of monthly staggered contributions building a disciplined investment structure over time.", "1000x750", "SIP Concept")}
        </div>
        <div>
          <span class="section-tag tag-navy">Disciplined Investing</span>
          <h2 class="section-title">Understand the Power of Investing Regularly</h2>
          <p class="section-subtitle mb-4">A Systematic Investment Plan (SIP) enables investors to commit a fixed sum into mutual fund schemes periodically, promoting behavioral discipline without the stress of market timing.</p>

          <div style="display: flex; flex-direction: column; gap: 1.25rem; margin-bottom: 2rem;">
            <div style="background: var(--bg-light); padding: 1.25rem; border-radius: var(--radius-md); border-left: 4px solid var(--green-primary);">
              <h4 style="margin-bottom: 0.35rem;">Rupee-Cost Averaging</h4>
              <p style="font-size: 0.9rem; margin: 0;">When markets decline, your fixed SIP installment purchases more fund units at lower NAVs; when markets rise, fewer units are bought at higher NAVs, evening out purchase costs over time.</p>
            </div>
            <div style="background: var(--bg-light); padding: 1.25rem; border-radius: var(--radius-md); border-left: 4px solid var(--navy-primary);">
              <h4 style="margin-bottom: 0.35rem;">Compounding Growth Potential</h4>
              <p style="font-size: 0.9rem; margin: 0;">Reinvested earnings generate further returns across multi-year cycles. Compounding accelerates exponentially the longer the uninterrupted investment horizon.</p>
            </div>
          </div>

          <div class="btn-group">
            <a href="sip-investment.html" class="btn btn-primary">Explore SIP Investment</a>
            <a href="sip-calculator.html" class="btn btn-outline">SIP Calculator</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive SIP Calculator Component on Homepage -->
  <section class="section section-light">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Interactive Education</span>
        <h2 class="section-title">Illustrative SIP Growth Calculator</h2>
        <p class="section-subtitle">Experiment with different monthly contributions, timeframes, and hypothetical annual rates to understand compounding dynamics.</p>
      </div>

      <div class="calculator-wrapper">
        <div class="calculator-grid">
          <div>
            <div class="calc-control-group">
              <div class="calc-label-row">
                <label for="sipAmountRange" class="calc-label">Monthly Investment Amount</label>
                <div class="calc-input-display">
                  <span>₹</span>
                  <input type="number" id="sipAmountInput" value="5000" min="500" max="500000" step="500">
                </div>
              </div>
              <input type="range" id="sipAmountRange" class="calc-range-slider" min="500" max="100000" step="500" value="5000">
            </div>

            <div class="calc-control-group">
              <div class="calc-label-row">
                <label for="sipRateRange" class="calc-label">Expected Annual Return Rate (%)</label>
                <div class="calc-input-display">
                  <input type="number" id="sipRateInput" value="12" min="1" max="30" step="0.5">
                  <span>%</span>
                </div>
              </div>
              <input type="range" id="sipRateRange" class="calc-range-slider" min="1" max="25" step="0.5" value="12">
            </div>

            <div class="calc-control-group">
              <div class="calc-label-row">
                <label for="sipYearsRange" class="calc-label">Time Horizon (Years)</label>
                <div class="calc-input-display">
                  <input type="number" id="sipYearsInput" value="10" min="1" max="40" step="1">
                  <span>Yrs</span>
                </div>
              </div>
              <input type="range" id="sipYearsRange" class="calc-range-slider" min="1" max="35" step="1" value="10">
            </div>

            <div class="btn-group mt-4">
              <button type="button" id="sipResetBtn" class="btn btn-outline btn-sm">Reset Inputs</button>
            </div>
          </div>

          <div>
            <div class="calc-results-card">
              <h4 style="margin-bottom: 1rem; color: var(--navy-primary);">Illustrative Output Breakdown</h4>
              <div class="calc-stat-box">
                <span class="calc-stat-label">Total Amount Invested:</span>
                <span class="calc-stat-val" id="sipInvestedDisplay">₹6,00,000</span>
              </div>
              <div class="calc-stat-box">
                <span class="calc-stat-label">Illustrative Est. Gain:</span>
                <span class="calc-stat-val text-green" id="sipGainDisplay">₹5,61,695</span>
              </div>
              <div class="calc-stat-box highlight">
                <span class="calc-stat-label">Estimated Future Value:</span>
                <span class="calc-stat-val" id="sipTotalDisplay">₹11,61,695</span>
              </div>

              <div class="calc-breakdown-bar">
                <div class="calc-bar-invested" id="sipBarInvested" style="width: 52%;"></div>
                <div class="calc-bar-gain" id="sipBarGain" style="width: 48%;"></div>
              </div>
              <div class="calc-legend">
                <div class="calc-legend-item">
                  <span class="legend-dot dot-invested"></span>
                  <span>Invested Capital</span>
                </div>
                <div class="calc-legend-item">
                  <span class="legend-dot dot-gain"></span>
                  <span>Compounded Returns</span>
                </div>
              </div>

              <div class="calc-disclaimer-box">
                <strong>ILLUSTRATIVE ESTIMATE — NOT A PREDICTION OR GUARANTEE OF MUTUAL FUND RETURNS.</strong>
                Mutual fund investments are subject to market risks. Actual returns fluctuate and calculations exclude scheme expenses, exit loads, and applicable taxes.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Financial Goals Section -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-gold">Life Milestones</span>
        <h2 class="section-title">Aligning Investments to Financial Goals</h2>
        <p class="section-subtitle">Goal-based investing provides purpose and clarity to your portfolio, anchoring asset allocation to specific timeframes.</p>
      </div>

      <div class="card-grid-3">
        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
          </div>
          <h3 class="feature-card-title">Retirement Planning</h3>
          <p class="feature-card-text">Building an inflation-protected retirement corpus through systematic equity compounding over 15 to 30 years.</p>
          <a href="financial-planning.html" class="feature-card-link">Explore Retirement Concept &rarr;</a>
        </div>

        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
          </div>
          <h3 class="feature-card-title">Higher Education Fund</h3>
          <p class="feature-card-text">Accounting for education inflation by investing in balanced hybrid or flexi-cap portfolios for a 7 to 12-year window.</p>
          <a href="goal-based-investing.html" class="feature-card-link">Explore Education Mapping &rarr;</a>
        </div>

        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
          </div>
          <h3 class="feature-card-title">Home Down Payment</h3>
          <p class="feature-card-text">Balancing capital safety and returns over a 3 to 5-year timeline with short-duration debt and conservative hybrid schemes.</p>
          <a href="goal-planning-calculator.html" class="feature-card-link">Calculate Target Savings &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- 5-Stage Investment Process -->
  <section class="section section-navy">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-tag tag-navy">Methodology</span>
        <h2 class="section-title text-white">The 5-Stage Investor Education Process</h2>
        <p class="section-subtitle text-muted">A structured educational framework guiding rational, goal-oriented decision making.</p>
      </div>

      <div class="process-steps-grid">
        <div class="process-step-card" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
          <div class="process-step-number" style="background: var(--green-primary);">1</div>
          <h4 class="process-step-title text-white">Understand Goals</h4>
          <p class="process-step-desc" style="color: #CBD5E1;">Clarify what you want to achieve, your expected horizon, and liquidity requirements.</p>
        </div>

        <div class="process-step-card" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
          <div class="process-step-number" style="background: var(--green-primary);">2</div>
          <h4 class="process-step-title text-white">Understand Risk</h4>
          <p class="process-step-desc" style="color: #CBD5E1;">Assess emotional comfort with market swings and financial ability to absorb paper losses.</p>
        </div>

        <div class="process-step-card" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
          <div class="process-step-number" style="background: var(--green-primary);">3</div>
          <h4 class="process-step-title text-white">Explore Categories</h4>
          <p class="process-step-desc" style="color: #CBD5E1;">Evaluate equity, debt, and hybrid fund categories matching your asset allocation targets.</p>
        </div>

        <div class="process-step-card" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
          <div class="process-step-number" style="background: var(--green-primary);">4</div>
          <h4 class="process-step-title text-white">Understand Costs</h4>
          <p class="process-step-desc" style="color: #CBD5E1;">Review TER, exit loads, turnover ratios, and applicable capital gains tax rules.</p>
        </div>

        <div class="process-step-card" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
          <div class="process-step-number" style="background: var(--green-primary);">5</div>
          <h4 class="process-step-title text-white">Review Periodically</h4>
          <p class="process-step-desc" style="color: #CBD5E1;">Perform annual checkups to rebalance asset classes and prune portfolio overlap.</p>
        </div>
      </div>

      <div class="regulatory-banner mt-5" style="background: rgba(254, 243, 199, 0.1); border-color: rgba(252, 211, 77, 0.2); color: #FCD34D;">
        <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <div>
          <strong>Educational Framework Notice:</strong> The 5-stage timeline represents a conceptual educational journey. It does not constitute a personalized suitability assessment or formal client advisory agreement.
        </div>
      </div>
    </div>
  </section>

  <!-- Investor Resources Preview -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Knowledge Hub</span>
        <h2 class="section-title">Investor Education &amp; Insights</h2>
        <p class="section-subtitle">Deepen your financial literacy with objective guides on fund operations, structures, and metrics.</p>
      </div>

      <div class="card-grid-3">
        <div class="article-card">
          <div class="article-card-body">
            <div class="article-meta">
              <span>Beginners</span> &bull; <span>5 Min Read</span>
            </div>
            <h3 class="article-title"><a href="investment-for-beginners.html">Mutual Funds Explained for Beginners</a></h3>
            <p class="article-excerpt">A plain-language guide detailing how mutual funds operate in India, SEBI protections, and key terminology.</p>
            <a href="investment-for-beginners.html" class="feature-card-link">Read Guide &rarr;</a>
          </div>
        </div>

        <div class="article-card">
          <div class="article-card-body">
            <div class="article-meta">
              <span>Strategy</span> &bull; <span>6 Min Read</span>
            </div>
            <h3 class="article-title"><a href="sip-investment.html">SIP vs Lump Sum: Choosing the Right Route</a></h3>
            <p class="article-excerpt">Understanding the trade-offs between dollar-cost averaging through SIPs versus deploying lump-sum windfalls.</p>
            <a href="sip-investment.html" class="feature-card-link">Read Guide &rarr;</a>
          </div>
        </div>

        <div class="article-card">
          <div class="article-card-body">
            <div class="article-meta">
              <span>Evaluation</span> &bull; <span>4 Min Read</span>
            </div>
            <h3 class="article-title"><a href="direct-vs-regular.html">Direct vs Regular Mutual Fund Plans</a></h3>
            <p class="article-excerpt">Examining expense ratio differentials, distributor commissions, and deciding what fits your advisory requirements.</p>
            <a href="direct-vs-regular.html" class="feature-card-link">Read Guide &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Final CTA Section -->
  <section class="section section-light" style="border-top: 1px solid var(--border-subtle);">
    <div class="container text-center" style="max-width: 780px;">
      <h2 style="font-size: 2.25rem; margin-bottom: 1rem;">Take the Time to Understand Your Investment Choices</h2>
      <p style="color: var(--text-muted); font-size: 1.1rem; margin-bottom: 2rem;">
        Empower yourself with sound financial literacy. Explore our calculators, compare fund categories, or enquire about a structured consultation.
      </p>
      <div class="btn-group" style="justify-content: center;">
        <a href="investor-resources.html" class="btn btn-outline btn-lg">Explore Resources</a>
        <a href="consultation.html" class="btn btn-primary btn-lg">Request Consultation</a>
      </div>
    </div>
  </section>
"""
    }

    # 2. about.html
    pages["about.html"] = {
        "title": "About Us | Mutual Fund Advisory Philosophy & Principles",
        "meta_desc": "Learn about our investor-first philosophy, commitment to financial education, transparent disclosures, and disciplined wealth management frameworks.",
        "active_nav": "about",
        "breadcrumbs": [("About Us", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">About Our Platform</span>
      <h1 class="page-banner-title">Empowering Investors Through Unbiased Education &amp; Discipline</h1>
      <p class="page-banner-desc">We champion long-term financial literacy, objective asset allocation, and regulatory transparency to help Indian investors navigate the capital markets with confidence.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2" style="align-items: center;">
        <div>
          <span class="section-tag">Our Educational Philosophy</span>
          <h2 class="section-title">An Investor-First Perspective in Wealth Management</h2>
          <p>
            The Indian financial services landscape offers remarkable wealth-creation opportunities through mutual funds. However, misinformation, unrealistic return expectations, and short-term speculative behavior frequently erode investor outcomes.
          </p>
          <p>
            Our core mission is to bridge the financial literacy gap. We emphasize that successful investing is not about predicting market peaks or chasing the latest high-performing fund, but about executing a structured financial plan anchored in asset allocation, risk awareness, and patient compounding.
          </p>
          <p>
            Every educational framework we publish adheres to the highest standards of objectivity, making clear distinctions between regulated advisory, scheme distribution, and general financial education.
          </p>
        </div>
        <div>
          {make_placeholder("mutual-fund-investor-education.jpg", "Financial Planning & Investor Literacy Workshop", "4-3", "An engaging wealth education seminar with interactive visual dashboards illustrating long-term asset allocation.", "1000x750", "Investor Education")}
        </div>
      </div>
    </div>
  </section>

  <!-- Core Values -->
  <section class="section section-light">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-gold">Guiding Principles</span>
        <h2 class="section-title">Our Six Foundational Pillars</h2>
        <p class="section-subtitle">Values that govern every concept, educational module, and consultation framework presented on this demonstration platform.</p>
      </div>

      <div class="card-grid-3">
        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
          </div>
          <h3 class="feature-card-title">1. Transparency</h3>
          <p class="feature-card-text">Total openness regarding scheme expense ratios, distribution commissions, exit charges, and capital gains taxation without hidden costs.</p>
        </div>

        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3 class="feature-card-title">2. Responsibility</h3>
          <p class="feature-card-text">Upholding strict ethical safeguards. We never promise guaranteed returns, capital protection, or speculative overnight wealth.</p>
        </div>

        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
          </div>
          <h3 class="feature-card-title">3. Discipline</h3>
          <p class="feature-card-text">Promoting systematic investing (SIP), rebalancing protocols, and emotional fortitude across turbulent market corrections.</p>
        </div>

        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
          </div>
          <h3 class="feature-card-title">4. Investor Awareness</h3>
          <p class="feature-card-text">Empowering investors with the critical ability to evaluate scheme information documents (SID), Key Information Memorandums (KIM), and factsheets.</p>
        </div>

        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          </div>
          <h3 class="feature-card-title">5. Clarity</h3>
          <p class="feature-card-text">Demystifying intricate financial jargon into actionable, intuitive insights that retail and institutional participants can easily grasp.</p>
        </div>

        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/></svg>
          </div>
          <h3 class="feature-card-title">6. Long-Term Thinking</h3>
          <p class="feature-card-text">Treating mutual fund investments as multi-year participations in India's macroeconomic growth rather than trading instruments.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Regulatory Safe Harbor Box -->
  <section class="section">
    <div class="container container-narrow">
      <div class="regulatory-banner">
        <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <div>
          <strong>Demonstration Platform Safeguard:</strong> This website is an architectural and educational demonstration. It does not represent an active SEBI Registered Investment Adviser (RIA) or AMFI Registered Mutual Fund Distributor (MFD). We do not solicit funds, manage client capital, or execute transactions.
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 3. services.html
    pages["services.html"] = {
        "title": "Our Services Overview | Mutual Fund Education & Planning",
        "meta_desc": "Explore our 5 core educational service areas covering mutual fund fundamentals, financial goal planning, portfolio review concepts, and corporate workshops.",
        "active_nav": "about",
        "breadcrumbs": [("Services", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Service Taxonomy</span>
      <h1 class="page-banner-title">Structured Financial Services &amp; Education Capabilities</h1>
      <p class="page-banner-desc">Organized into five distinct disciplines designed to serve individuals, families, and corporate organizations seeking structured wealth education.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="mb-5">
        {make_placeholder("mutual-fund-financial-consultation.jpg", "Comprehensive Financial Advisory Capabilities", "16-9", "A corporate board meeting setting reviewing financial education offerings and wealth advisory frameworks.", "1200x675", "Services Overview")}
      </div>

      <div class="regulatory-banner mb-5">
        <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <div>
          <strong>Regulatory Service Notice:</strong> Before live commercial deployment, the operating entity must select its authorized operational model (Model A: SEBI RIA, Model B: AMFI MFD, or Model C: Pure Investor Education) and remove any services not legally authorized under its respective registrations.
        </div>
      </div>

      <!-- Area A -->
      <div class="mb-5 pb-4" style="border-bottom: 1px solid var(--border-subtle);">
        <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.5rem;">
          <span style="background: var(--navy-primary); color: white; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">A</span>
          <h2>Mutual Fund Education</h2>
        </div>
        <p class="mb-4">Foundational literacy programs designed to familiarize new and transitioning investors with market structures.</p>
        <div class="card-grid-3">
          <div class="feature-card">
            <h4 class="feature-card-title">Mutual Fund Basics</h4>
            <p class="feature-card-text">Comprehensive demystification of asset management companies (AMCs), unit creation, NAV calculations, and custodial roles.</p>
          </div>
          <div class="feature-card">
            <h4 class="feature-card-title">Category Literacy</h4>
            <p class="feature-card-text">In-depth breakdown of SEBI categorization across 36+ official scheme categories including market-cap parameters.</p>
          </div>
          <div class="feature-card">
            <h4 class="feature-card-title">SIP &amp; Lump Sum Concepts</h4>
            <p class="feature-card-text">Mathematical mechanics of rupee-cost averaging, systematic transfers (STP), and staggered lump sum deployments.</p>
          </div>
        </div>
      </div>

      <!-- Area B -->
      <div class="mb-5 pb-4" style="border-bottom: 1px solid var(--border-subtle);">
        <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.5rem;">
          <span style="background: var(--navy-primary); color: white; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">B</span>
          <h2>Investment Planning Education</h2>
        </div>
        <p class="mb-4">Equipping investors to build purposeful, horizon-based asset allocation blueprints.</p>
        <div class="card-grid-3">
          <div class="feature-card">
            <h4 class="feature-card-title">Goal-Based Planning</h4>
            <p class="feature-card-text">Calculating corpus targets for major life milestones while adjusting for historical inflation rates in education and healthcare.</p>
          </div>
          <div class="feature-card">
            <h4 class="feature-card-title">Asset Allocation Concepts</h4>
            <p class="feature-card-text">Understanding equity-to-debt ratios, negative correlation benefits, and volatility moderation across market regimes.</p>
          </div>
          <div class="feature-card">
            <h4 class="feature-card-title">Retirement Readiness</h4>
            <p class="feature-card-text">Conceptualizing post-retirement cash flows, safe withdrawal rates, and Systematic Withdrawal Plans (SWP).</p>
          </div>
        </div>
      </div>

      <!-- Area C -->
      <div class="mb-5 pb-4" style="border-bottom: 1px solid var(--border-subtle);">
        <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.5rem;">
          <span style="background: var(--navy-primary); color: white; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">C</span>
          <h2>Portfolio Education &amp; Analysis</h2>
        </div>
        <p class="mb-4">Techniques to diagnose portfolio health, eliminate unnecessary overlap, and manage cost drag.</p>
        <div class="card-grid-3">
          <div class="feature-card">
            <h4 class="feature-card-title">Portfolio Overlap Diagnosis</h4>
            <p class="feature-card-text">Analyzing common underlying stock holdings across different equity schemes to prevent illusionary diversification.</p>
          </div>
          <div class="feature-card">
            <h4 class="feature-card-title">Category Drift Tracking</h4>
            <p class="feature-card-text">Monitoring how portfolio allocations naturally shift over bull markets and understanding disciplined rebalancing triggers.</p>
          </div>
          <div class="feature-card">
            <h4 class="feature-card-title">Expense Drag Evaluation</h4>
            <p class="feature-card-text">Quantifying the long-term compound effect of Total Expense Ratios (TER) on multi-decade portfolio terminal values.</p>
          </div>
        </div>
      </div>

      <!-- Area D -->
      <div class="mb-5 pb-4" style="border-bottom: 1px solid var(--border-subtle);">
        <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.5rem;">
          <span style="background: var(--navy-primary); color: white; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">D</span>
          <h2>Investor Support &amp; Guidance</h2>
        </div>
        <p class="mb-4">Assisting investors through statutory documentation, regulatory processes, and operational formalities.</p>
        <div class="card-grid-3">
          <div class="feature-card">
            <h4 class="feature-card-title">KYC &amp; Onboarding Literacy</h4>
            <p class="feature-card-text">Clarifying CKYC, KRA verification, FATCA compliance, and nomination procedures mandated by SEBI and AMFI.</p>
          </div>
          <div class="feature-card">
            <h4 class="feature-card-title">Scheme Factsheet Interpretation</h4>
            <p class="feature-card-text">Guiding investors on how to read portfolio disclosures, standard deviation, Sharpe ratios, and benchmark tracking error.</p>
          </div>
          <div class="feature-card">
            <h4 class="feature-card-title">Grievance Redressal Guidance</h4>
            <p class="feature-card-text">Educating investors on SEBI SCORES portal mechanics, registrar touchpoints (CAMS/KFintech), and ombudsman processes.</p>
          </div>
        </div>
      </div>

      <!-- Area E -->
      <div>
        <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.5rem;">
          <span style="background: var(--navy-primary); color: white; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">E</span>
          <h2>Business &amp; Corporate Financial Education</h2>
        </div>
        <p class="mb-4">Workplace financial wellness sessions designed to cultivate disciplined financial habits among employees.</p>
        <div class="card-grid-3">
          <div class="feature-card">
            <h4 class="feature-card-title">Employee Financial Literacy</h4>
            <p class="feature-card-text">Interactive corporate workshops covering personal budgeting, emergency fund creation, and early SIP discipline.</p>
          </div>
          <div class="feature-card">
            <h4 class="feature-card-title">Tax Awareness Sessions</h4>
            <p class="feature-card-text">Educational presentations covering Section 80C, equity vs debt fund capital gains tax rules, and regime comparisons.</p>
          </div>
          <div class="feature-card">
            <h4 class="feature-card-title">Retirement Planning Clinics</h4>
            <p class="feature-card-text">Helping corporate employees understand EPF, NPS, and mutual fund synergy for post-retirement wealth security.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 4. mutual-funds.html
    pages["mutual-funds.html"] = {
        "title": "Mutual Funds Overview | Categories & Structures in India",
        "meta_desc": "Explore all 14 major mutual fund categories in India. Understand equity, debt, hybrid, passive, and liquid funds under SEBI regulatory guidelines.",
        "active_nav": "funds",
        "breadcrumbs": [("Mutual Funds", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Fund Overview</span>
      <h1 class="page-banner-title">The Complete Guide to Mutual Funds in India</h1>
      <p class="page-banner-desc">Explore SEBI-defined categories, investment objectives, volatility dynamics, and structural distinctions across Indian mutual funds.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">How Mutual Funds Work</span>
          <h2 class="section-title">Collective Investment Vehicles Regulated by SEBI</h2>
          <p>
            A mutual fund is a trust that pools savings from numerous investors sharing a common financial objective. The pooled capital is managed by a registered Asset Management Company (AMC) and invested in stocks, bonds, money market instruments, and other securities.
          </p>
          <p>
            Each investor holds units that represent a proportional share of the scheme's net assets. Income and capital appreciation generated by the portfolio are distributed among unitholders in proportion to their unit holdings, after deducting allowable scheme expenses.
          </p>
          <div class="regulatory-banner">
            <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <div>
              <strong>Statutory Disclosure:</strong> Mutual fund investments are subject to market risks. Past performance is not indicative of future returns. Read all scheme-related documents carefully before investing.
            </div>
          </div>
        </div>
        <div>
          {make_placeholder("mutual-fund-wealth-planning.jpg", "Mutual Fund Structure & Custodial Mechanics", "4-3", "An infographic-style visualization illustrating the flow of capital from investors to AMC, custodian, and portfolio assets.", "1000x750", "Structure Architecture")}
        </div>
      </div>

      <div class="section-header">
        <span class="section-tag tag-gold">Browse Scheme Types</span>
        <h2 class="section-title">Explore 14 Major Scheme Categories</h2>
        <p class="section-subtitle">Click on any category to explore in-depth definitions, risk characteristics, typical horizons, and suitability considerations.</p>
      </div>

      <div class="card-grid-3">
        <a href="equity-mutual-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-equity">Core Equity</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Equity Mutual Funds</h4>
          <p class="category-card-desc">Growth-oriented funds investing at least 65% in equity shares across capitalization tiers.</p>
          <div class="category-meta"><span>Risk: High</span><span class="category-horizon">Horizon: 5+ Yrs</span></div>
        </a>

        <a href="debt-mutual-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-debt">Fixed Income</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Debt Mutual Funds</h4>
          <p class="category-card-desc">Income-focused portfolios investing in government securities, corporate debentures, and money markets.</p>
          <div class="category-meta"><span>Risk: Low to Moderate</span><span class="category-horizon">Horizon: 1-3 Yrs</span></div>
        </a>

        <a href="hybrid-mutual-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-hybrid">Multi-Asset</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Hybrid Mutual Funds</h4>
          <p class="category-card-desc">Combined allocations across equities and debt to moderate drawdown volatility.</p>
          <div class="category-meta"><span>Risk: Moderate to High</span><span class="category-horizon">Horizon: 3-5 Yrs</span></div>
        </a>

        <a href="index-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-passive">Passive Index</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Index Funds</h4>
          <p class="category-card-desc">Rule-based funds replicating benchmark indices such as Nifty 50, Sensex, or Nifty Next 50.</p>
          <div class="category-meta"><span>Risk: Market Risk</span><span class="category-horizon">Horizon: 5+ Yrs</span></div>
        </a>

        <a href="large-cap-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-equity">Top 100 Stocks</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Large Cap Funds</h4>
          <p class="category-card-desc">Mandated to invest minimum 80% in the top 100 established market leaders by market cap.</p>
          <div class="category-meta"><span>Risk: Moderate-High</span><span class="category-horizon">Horizon: 5+ Yrs</span></div>
        </a>

        <a href="mid-cap-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-equity">Ranks 101-250</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Mid Cap Funds</h4>
          <p class="category-card-desc">Invests minimum 65% in mid-sized growing companies with higher earnings growth potential.</p>
          <div class="category-meta"><span>Risk: High</span><span class="category-horizon">Horizon: 7+ Yrs</span></div>
        </a>

        <a href="small-cap-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-equity">Ranks 251+</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Small Cap Funds</h4>
          <p class="category-card-desc">Minimum 65% exposure to emerging small-cap companies; high growth potential with high volatility.</p>
          <div class="category-meta"><span>Risk: Very High</span><span class="category-horizon">Horizon: 7-10 Yrs</span></div>
        </a>

        <a href="flexi-cap-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-equity">Unconstrained</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Flexi Cap Funds</h4>
          <p class="category-card-desc">Dynamically allocates across large, mid, and small-cap stocks at the fund manager's discretion.</p>
          <div class="category-meta"><span>Risk: High</span><span class="category-horizon">Horizon: 5+ Yrs</span></div>
        </a>

        <a href="ELSS.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-tax">Section 80C</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">ELSS (Tax Saving)</h4>
          <p class="category-card-desc">Equity schemes offering tax deduction under 80C with the shortest statutory lock-in of 3 years.</p>
          <div class="category-meta"><span>Risk: High</span><span class="category-horizon">Horizon: 3+ Yrs</span></div>
        </a>

        <a href="liquid-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-liquid">Short Cash</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Liquid Funds</h4>
          <p class="category-card-desc">Debt securities maturing up to 91 days; prime vehicle for emergency buffers and treasury management.</p>
          <div class="category-meta"><span>Risk: Low</span><span class="category-horizon">Horizon: 1-90 Days</span></div>
        </a>

        <a href="overnight-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-liquid">1-Day Maturity</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Overnight Funds</h4>
          <p class="category-card-desc">Invests in securities maturing in 1 business day; lowest interest rate and default risk.</p>
          <div class="category-meta"><span>Risk: Lowest</span><span class="category-horizon">Horizon: 1-7 Days</span></div>
        </a>

        <a href="international-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-equity">Global Stocks</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">International Funds</h4>
          <p class="category-card-desc">Feeder funds investing in foreign equity markets and overseas exchange-traded funds.</p>
          <div class="category-meta"><span>Risk: High + Currency</span><span class="category-horizon">Horizon: 5+ Yrs</span></div>
        </a>

        <a href="fund-of-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-passive">FoF Architecture</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Fund of Funds</h4>
          <p class="category-card-desc">Schemes that invest in other mutual fund units rather than individual securities directly.</p>
          <div class="category-meta"><span>Risk: Underlying Dependent</span><span class="category-horizon">Horizon: 3-5 Yrs</span></div>
        </a>

        <a href="sectoral-thematic-funds.html" class="category-card">
          <div class="category-card-header">
            <span class="category-badge badge-tax">Targeted Theme</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <h4 class="category-card-title">Sectoral &amp; Thematic</h4>
          <p class="category-card-desc">Focuses on a specific economic industry or macro theme with elevated concentration risk.</p>
          <div class="category-meta"><span>Risk: Very High</span><span class="category-horizon">Horizon: Tactical</span></div>
        </a>
      </div>
    </div>
  </section>
"""
    }

    # 5. investment-approach.html
    pages["investment-approach.html"] = {
        "title": "Investment Approach | Disciplined Wealth Architecture",
        "meta_desc": "Explore our educational investment framework: goal definition, time horizon mapping, risk capacity, asset allocation, diversification, and cost awareness.",
        "active_nav": "planning",
        "breadcrumbs": [("Investment Approach", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Framework &amp; Principles</span>
      <h1 class="page-banner-title">Our Disciplined Investment Approach</h1>
      <p class="page-banner-desc">A structured educational framework emphasizing risk-adjusted returns, process over prediction, and long-term asset allocation.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Philosophy</span>
          <h2 class="section-title">Process Over Market Timing</h2>
          <p>
            Academic research consistently reveals that asset allocation—not stock picking or short-term market timing—drives over 90% of long-term portfolio return variability.
          </p>
          <p>
            Our investment approach educates investors to construct resilient portfolios that survive market corrections and capture compounding growth through patient, goal-aligned discipline.
          </p>
        </div>
        <div>
          {make_placeholder("mutual-fund-asset-allocation.jpg", "Asset Allocation & Modern Portfolio Theory", "4-3", "An educational chart displaying the efficient frontier and correlation matrix between equities and fixed income.", "1000x750", "Asset Allocation Model")}
        </div>
      </div>

      <div class="section-header">
        <span class="section-tag tag-gold">The 8 Pillars</span>
        <h2 class="section-title">The Strategic Framework</h2>
      </div>

      <div class="card-grid-4">
        <div class="feature-card">
          <h4 class="feature-card-title">1. Define Goals</h4>
          <p class="feature-card-text">Every rupee must have a defined purpose, whether funding child education in 10 years or generating retirement income in 20.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">2. Investment Horizon</h4>
          <p class="feature-card-text">Matching the liquidity demands of your goal to the appropriate volatility profile of equity or fixed-income assets.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">3. Risk Capacity</h4>
          <p class="feature-card-text">Evaluating objective financial factors: emergency savings, dependable income, liabilities, and dependants.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">4. Risk Tolerance</h4>
          <p class="feature-card-text">Evaluating subjective psychological factors: comfort with temporary paper drawdowns without panic selling.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">5. Asset Allocation</h4>
          <p class="feature-card-text">Setting optimal equity, debt, and gold ratios to balance growth aspirations with downside protection.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">6. Diversification</h4>
          <p class="feature-card-text">Spreading allocations across uncorrelated sectors and cap sizes while avoiding unproductive fund overlap.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">7. Periodic Rebalancing</h4>
          <p class="feature-card-text">Restoring target asset allocations annually, automatically selling overextended assets and buying undervalued ones.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">8. Cost &amp; Tax Efficiency</h4>
          <p class="feature-card-text">Minimizing expense ratio drag, turnover costs, and optimizing long-term capital gains tax treatment.</p>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 6. financial-planning.html
    pages["financial-planning.html"] = {
        "title": "Financial Planning | Goal-Based Wealth Architecture",
        "meta_desc": "Understand foundational financial planning: retirement mapping, education corpus planning, inflation impact, and emergency buffer creation in India.",
        "active_nav": "planning",
        "breadcrumbs": [("Financial Planning", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Holistic Architecture</span>
      <h1 class="page-banner-title">Foundations of Financial Planning</h1>
      <p class="page-banner-desc">Learn how to organize income, expenses, liabilities, and investments into a coherent life roadmap.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Core Tenets</span>
          <h2 class="section-title">Why Plan Before You Invest?</h2>
          <p>
            Investing in mutual funds without a financial plan is like setting sail without a destination. Financial planning provides the blueprint that determines what categories of funds to select, how much capital to allocate, and how long to hold them.
          </p>
          <p>
            A robust plan accounts for the silent wealth-destroyer: inflation. While nominal living costs rise, educational and healthcare inflation in India historically runs even higher, necessitating inflation-beating asset classes.
          </p>
        </div>
        <div>
          {make_placeholder("mutual-fund-financial-goals.jpg", "Financial Planning Roadmap & Corpus Targets", "4-3", "A couple reviewing life milestones on a digital tablet with retirement and education projections.", "1000x750", "Planning Visual")}
        </div>
      </div>

      <div class="section-header">
        <span class="section-tag tag-gold">Core Milestone Pillars</span>
        <h2 class="section-title">Key Elements of a Financial Plan</h2>
      </div>

      <div class="card-grid-3">
        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3 class="feature-card-title">1. Emergency Liquidity</h3>
          <p class="feature-card-text">Maintaining 6 to 12 months of living expenses in liquid mutual funds or sweep-in deposits before committing capital to long-term equities.</p>
        </div>

        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
          </div>
          <h3 class="feature-card-title">2. Retirement Security</h3>
          <p class="feature-card-text">Estimating post-retirement living costs over a 25-30 year non-earning span and building an accumulation portfolio via equity SIPs.</p>
        </div>

        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/></svg>
          </div>
          <h3 class="feature-card-title">3. Children's Goals</h3>
          <p class="feature-card-text">Factoring 8-10% education inflation into higher education targets, de-risking from equities into debt funds 2-3 years prior to matriculation.</p>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 7. goal-based-investing.html
    pages["goal-based-investing.html"] = {
        "title": "Goal-Based Investing | Purpose-Driven Asset Allocation",
        "meta_desc": "Learn how goal-based investing separates short, medium, and long-term objectives and maps them to appropriate mutual fund categories.",
        "active_nav": "planning",
        "breadcrumbs": [("Goal-Based Investing", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Purposeful Wealth</span>
      <h1 class="page-banner-title">Goal-Based Mutual Fund Investing</h1>
      <p class="page-banner-desc">Eliminate emotional decision-making by anchoring your mutual fund schemes to concrete life milestones.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Objective Mapping</span>
          <h2 class="section-title">Mapping Horizons to Asset Classes</h2>
          <p>
            When capital has an assigned mission, temporary market drawdowns no longer provoke panic. If equity markets drop in year 3 of a 15-year retirement goal, the decline is irrelevant to current cash flow.
          </p>
          <p>
            Conversely, money required in 18 months for a property purchase must never be exposed to equities, regardless of how bullish market forecasts appear.
          </p>
        </div>
        <div>
          {make_placeholder("mutual-fund-retirement-planning.jpg", "Life Milestone Goals & Target Retirement Planning", "4-3", "An illustrative family roadmap depicting retirement, college education, and home ownership targets.", "1000x750", "Goal Planning Visual")}
        </div>
      </div>

      <div class="card-grid-3 mb-5">
        <div class="feature-card" style="border-top: 4px solid #0284C7;">
          <h3 class="feature-card-title">Short-Term Goals (&lt; 3 Yrs)</h3>
          <p class="feature-card-text">Examples: Emergency reserve, travel fund, upcoming gadget or tax outflow.</p>
          <ul style="font-size: 0.885rem; color: var(--text-body); display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
            <li><strong>Primary Focus:</strong> Capital preservation &amp; high liquidity.</li>
            <li><strong>Suitable Categories:</strong> Liquid funds, ultra short duration, overnight funds.</li>
            <li><strong>Avoid:</strong> Pure equity funds due to short-term drawdown risk.</li>
          </ul>
        </div>

        <div class="feature-card" style="border-top: 4px solid #D97706;">
          <h3 class="feature-card-title">Medium-Term Goals (3-5 Yrs)</h3>
          <p class="feature-card-text">Examples: Vehicle purchase, home down payment, higher certificate course.</p>
          <ul style="font-size: 0.885rem; color: var(--text-body); display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
            <li><strong>Primary Focus:</strong> Moderate growth with volatility dampening.</li>
            <li><strong>Suitable Categories:</strong> Conservative hybrid, balanced advantage, short duration debt.</li>
            <li><strong>Asset Mix:</strong> 25-40% Equity, 60-75% Debt.</li>
          </ul>
        </div>

        <div class="feature-card" style="border-top: 4px solid #16A34A;">
          <h3 class="feature-card-title">Long-Term Goals (5+ Yrs)</h3>
          <p class="feature-card-text">Examples: Retirement corpus, child education, legacy wealth creation.</p>
          <ul style="font-size: 0.885rem; color: var(--text-body); display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
            <li><strong>Primary Focus:</strong> Compounding wealth above consumer inflation.</li>
            <li><strong>Suitable Categories:</strong> Flexi cap, large &amp; mid cap, index funds.</li>
            <li><strong>Asset Mix:</strong> 65-80% Equity, 20-35% Fixed Income.</li>
          </ul>
        </div>
      </div>

      <div class="calculator-wrapper text-center p-4">
        <h3>Ready to map your milestone?</h3>
        <p class="mb-3">Use our educational Goal Planning Calculator to calculate your required monthly SIP.</p>
        <a href="goal-planning-calculator.html" class="btn btn-primary">Open Goal Planning Calculator</a>
      </div>
    </div>
  </section>
"""
    }

    # 8. portfolio-review.html
    pages["portfolio-review.html"] = {
        "title": "Portfolio Review Concepts | Mutual Fund Health Check",
        "meta_desc": "Understand the principles of mutual fund portfolio reviews: scheme overlap, asset allocation drift, expense ratio drag, and rebalancing discipline.",
        "active_nav": "planning",
        "breadcrumbs": [("Portfolio Review", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Diagnostics</span>
      <h1 class="page-banner-title">Educational Portfolio Review Concepts</h1>
      <p class="page-banner-desc">Learn how experienced wealth managers diagnose existing portfolios to prune duplication, assess risk drift, and re-align with life goals.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Health Diagnostics</span>
          <h2 class="section-title">Why Review Your Mutual Fund Portfolio?</h2>
          <p>
            Investors frequently accumulate 15 to 25 mutual fund schemes over several years without realizing that many schemes invest in the exact same underlying companies. This illusion of diversification increases tracking complexity without enhancing risk-adjusted returns.
          </p>
          <p>
            An objective portfolio review examines scheme overlap, asset class allocation drift, portfolio concentration, and fee drag, providing the clarity needed to consolidate and optimize holdings.
          </p>
        </div>
        <div>
          {make_placeholder("mutual-fund-portfolio-review.jpg", "Financial Analyst Conducting Portfolio Review", "4-3", "An advisor reviewing stock overlap metrics, standard deviations, and category weights on multiple screens.", "1000x750", "Review Analytics")}
        </div>
      </div>

      <!-- Demo Mockup -->
      <div class="mockup-window mb-5">
        <div class="mockup-header">
          <div class="mockup-dots">
            <span class="mockup-dot red"></span>
            <span class="mockup-dot yellow"></span>
            <span class="mockup-dot green"></span>
          </div>
          <span>ILLUSTRATIVE DEMO PORTFOLIO REVIEW INTERFACE</span>
          <span>DEMO DATA ONLY</span>
        </div>
        <div class="mockup-body">
          <div class="mockup-watermark">
            ILLUSTRATIVE DEMO PORTFOLIO — NOT AN ACTUAL INVESTOR PORTFOLIO OR ACCOUNT
          </div>

          <div class="card-grid-3 mb-4">
            <div style="background: white; padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
              <span style="font-size: 0.8rem; color: var(--text-muted);">Current Equity Drift</span>
              <h3 style="color: var(--navy-primary); margin-top: 0.25rem;">78.4%</h3>
              <span style="font-size: 0.75rem; color: #D97706;">+8.4% above target (70%)</span>
            </div>
            <div style="background: white; padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
              <span style="font-size: 0.8rem; color: var(--text-muted);">Top 10 Stock Overlap</span>
              <h3 style="color: var(--navy-primary); margin-top: 0.25rem;">46.2%</h3>
              <span style="font-size: 0.75rem; color: var(--danger);">High duplication across 5 schemes</span>
            </div>
            <div style="background: white; padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
              <span style="font-size: 0.8rem; color: var(--text-muted);">Weighted Avg TER</span>
              <h3 style="color: var(--navy-primary); margin-top: 0.25rem;">1.42%</h3>
              <span style="font-size: 0.75rem; color: var(--green-deep);">Optimization potential identified</span>
            </div>
          </div>

          <div style="background: white; padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
            <h4 style="margin-bottom: 1rem;">Illustrative Category Exposure vs Target</h4>
            
            <div class="alloc-item">
              <div class="alloc-label-bar">
                <span>Large Cap Equity (Current: 45% vs Target: 35%)</span>
                <span>45%</span>
              </div>
              <div class="alloc-progress">
                <div class="alloc-progress-fill" style="width: 45%; background: #4F46E5;"></div>
              </div>
            </div>

            <div class="alloc-item">
              <div class="alloc-label-bar">
                <span>Mid &amp; Small Cap Equity (Current: 33.4% vs Target: 25%)</span>
                <span>33.4%</span>
              </div>
              <div class="alloc-progress">
                <div class="alloc-progress-fill" style="width: 33.4%; background: #10B981;"></div>
              </div>
            </div>

            <div class="alloc-item">
              <div class="alloc-label-bar">
                <span>Short Duration Debt (Current: 16.6% vs Target: 30%)</span>
                <span>16.6%</span>
              </div>
              <div class="alloc-progress">
                <div class="alloc-progress-fill" style="width: 16.6%; background: #F59E0B;"></div>
              </div>
            </div>

            <div class="alloc-item">
              <div class="alloc-label-bar">
                <span>Liquid Cash Buffer (Current: 5% vs Target: 10%)</span>
                <span>5%</span>
              </div>
              <div class="alloc-progress">
                <div class="alloc-progress-fill" style="width: 5%; background: #0284C7;"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 9. asset-allocation.html
    pages["asset-allocation.html"] = {
        "title": "Asset Allocation | Balancing Equity, Debt, and Hybrid",
        "meta_desc": "Understand strategic asset allocation principles. Explore interactive models balancing equity compounding and fixed income stability.",
        "active_nav": "planning",
        "breadcrumbs": [("Asset Allocation", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Portfolio Science</span>
      <h1 class="page-banner-title">Asset Allocation Frameworks</h1>
      <p class="page-banner-desc">Discover how strategically combining uncorrelated asset classes moderates risk while compounding capital over time.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="mb-5">
        {make_placeholder("mutual-fund-investment-dashboard.jpg", "Interactive Asset Allocation Dashboard Visual", "16-9", "A modern private wealth management interface showing interactive asset allocation sliders and risk charts.", "1200x675", "Allocation Interface")}
      </div>

      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Interactive Simulation</span>
          <h2 class="section-title">Simulate Educational Allocation Profiles</h2>
          <p class="mb-4">
            Select an illustrative investor risk profile below to examine how the target blend across Equity, Debt, Hybrid, and Cash assets shifts.
          </p>

          <div class="form-group">
            <label for="portfolioProfileSelect" class="form-label">Choose Illustrative Profile:</label>
            <select id="portfolioProfileSelect" class="form-control">
              <option value="conservative">Conservative Profile (Lower Risk Tolerance)</option>
              <option value="moderate" selected>Moderate Profile (Balanced Risk Tolerance)</option>
              <option value="aggressive">Aggressive Profile (Growth-Oriented Tolerance)</option>
            </select>
          </div>

          <p id="portfolioProfileDesc" style="font-size: 0.925rem; color: var(--navy-secondary); font-style: italic; background: var(--bg-light); padding: 1rem; border-radius: var(--radius-sm); border-left: 3px solid var(--green-primary);">
            Illustrative framework balancing growth and fixed-income stability over a 5 to 7-year time horizon.
          </p>
        </div>

        <div>
          <div class="mockup-window">
            <div class="mockup-header">
              <span>ILLUSTRATIVE ALLOCATION VISUALIZER</span>
              <span>DEMO ONLY</span>
            </div>
            <div class="mockup-body">
              <div class="mockup-watermark">ILLUSTRATIVE DEMO DATA — NOT A PERSONAL RECOMMENDATION</div>

              <div class="alloc-item">
                <div class="alloc-label-bar">
                  <span>Equity Mutual Funds</span>
                  <span id="allocEquityVal" class="font-bold text-navy">50%</span>
                </div>
                <div class="alloc-progress">
                  <div class="alloc-progress-fill" id="allocEquityBar" style="width: 50%; background: #4F46E5;"></div>
                </div>
              </div>

              <div class="alloc-item">
                <div class="alloc-label-bar">
                  <span>Debt Mutual Funds</span>
                  <span id="allocDebtVal" class="font-bold text-navy">35%</span>
                </div>
                <div class="alloc-progress">
                  <div class="alloc-progress-fill" id="allocDebtBar" style="width: 35%; background: #16A34A;"></div>
                </div>
              </div>

              <div class="alloc-item">
                <div class="alloc-label-bar">
                  <span>Hybrid &amp; Multi-Asset</span>
                  <span id="allocHybridVal" class="font-bold text-navy">10%</span>
                </div>
                <div class="alloc-progress">
                  <div class="alloc-progress-fill" id="allocHybridBar" style="width: 10%; background: #D97706;"></div>
                </div>
              </div>

              <div class="alloc-item">
                <div class="alloc-label-bar">
                  <span>Liquid Cash &amp; Emergency</span>
                  <span id="allocCashVal" class="font-bold text-navy">5%</span>
                </div>
                <div class="alloc-progress">
                  <div class="alloc-progress-fill" id="allocCashBar" style="width: 5%; background: #0284C7;"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 10. risk-management.html
    pages["risk-management.html"] = {
        "title": "Understanding Investment Risk | Mutual Fund Risk Dimensions",
        "meta_desc": "Explore 8 primary financial risk dimensions: market, interest rate, credit, liquidity, concentration, currency, inflation, and behavioral risks.",
        "active_nav": "planning",
        "breadcrumbs": [("Risk Management", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Risk Literacy</span>
      <h1 class="page-banner-title">Understanding Investment Risk in Mutual Funds</h1>
      <p class="page-banner-desc">Risk is not merely the chance of losing money; it is volatility, purchasing power erosion, and behavioral errors.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="mb-5">
        {make_placeholder("mutual-fund-risk-management.jpg", "Multi-Dimensional Financial Risk Spectrum", "16-9", "A quantitative radar chart mapping market risk, duration risk, credit spreads, and liquidity friction.", "1200x675", "Risk Dimensions")}
      </div>

      <div class="section-header">
        <span class="section-tag tag-gold">8 Dimensions of Risk</span>
        <h2 class="section-title">The Spectrum of Mutual Fund Risks</h2>
        <p class="section-subtitle">A comprehensive breakdown of risks present in Indian capital market schemes.</p>
      </div>

      <div class="card-grid-4">
        <div class="feature-card">
          <h4 class="feature-card-title">1. Market Risk</h4>
          <p class="feature-card-text">Macroeconomic swings, global events, and sentiment shifts affecting equity valuations across the board.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">2. Interest Rate Risk</h4>
          <p class="feature-card-text">Bond prices move inversely to interest rates. When RBI hikes repo rates, long-duration debt funds face temporary NAV declines.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">3. Credit Risk</h4>
          <p class="feature-card-text">The risk that corporate bond issuers delay or default on interest payments or principal repayments upon maturity.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">4. Liquidity Risk</h4>
          <p class="feature-card-text">Difficulty selling illiquid securities in secondary bond markets during market panics without steep price haircuts.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">5. Concentration Risk</h4>
          <p class="feature-card-text">Over-exposure to a single sector, business group, or theme, magnifying localized market drawdowns.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">6. Currency Risk</h4>
          <p class="feature-card-text">Fluctuations between the Indian Rupee and foreign currencies impacting the net NAV of international feeder funds.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">7. Inflation Risk</h4>
          <p class="feature-card-text">The danger that safe, low-yielding fixed investments deliver post-tax returns below real consumer inflation.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">8. Behavioral Risk</h4>
          <p class="feature-card-text">Panic-selling at market bottoms or FOMO-buying during speculative bull bubbles, sabotaging compounding.</p>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 11. investment-process.html
    pages["investment-process.html"] = {
        "title": "Investment Process | 5-Stage Investor Education Framework",
        "meta_desc": "Explore our 5-stage investor education process: Goal Awareness, Financial Awareness, Risk Awareness, Product Education, and Periodic Review.",
        "active_nav": "about",
        "breadcrumbs": [("Investment Process", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Systematic Methodology</span>
      <h1 class="page-banner-title">The 5-Stage Investor Education Process</h1>
      <p class="page-banner-desc">A structured sequence developed to move investors from ambiguity to disciplined, goal-directed clarity.</p>
    </div>
  </section>

  <section class="section">
    <div class="container container-narrow">
      <div class="mb-5">
        {make_placeholder("mutual-fund-investor-meeting.jpg", "5-Stage Investor Consultation Process", "16-9", "A senior financial planner and an investor walking through a 5-stage milestone timeline on a glass whiteboard.", "1200x675", "Process Architecture")}
      </div>

      <div style="display: flex; flex-direction: column; gap: 2.5rem;">
        <div class="feature-card" style="border-left: 5px solid var(--navy-primary);">
          <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem;">
            <span style="background: var(--navy-primary); color: white; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">1</span>
            <h3 style="margin: 0;">Stage 1 — Goal Awareness</h3>
          </div>
          <p>
            Understanding specifically what you are investing for. We articulate distinct goals (e.g. buying a residence in 6 years vs retiring in 22 years), estimating realistic future corpus targets adjusted for inflation.
          </p>
        </div>

        <div class="feature-card" style="border-left: 5px solid var(--green-primary);">
          <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem;">
            <span style="background: var(--green-primary); color: white; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">2</span>
            <h3 style="margin: 0;">Stage 2 — Financial Awareness</h3>
          </div>
          <p>
            Evaluating current cash flows, monthly surplus, debt obligations, insurance safety nets, and emergency cash reserves to establish how much can be committed uninterruptedly to long-term schemes.
          </p>
        </div>

        <div class="feature-card" style="border-left: 5px solid var(--gold-accent);">
          <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem;">
            <span style="background: var(--gold-accent); color: white; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">3</span>
            <h3 style="margin: 0;">Stage 3 — Risk Awareness</h3>
          </div>
          <p>
            Assessing the twin dimensions of risk: financial risk capacity (ability to sustain paper drawdowns without liquidating) and psychological risk tolerance (emotional resilience during market volatility).
          </p>
        </div>

        <div class="feature-card" style="border-left: 5px solid #0284C7);">
          <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem;">
            <span style="background: #0284C7; color: white; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">4</span>
            <h3 style="margin: 0;">Stage 4 — Product Education</h3>
          </div>
          <p>
            Examining scheme documents, Total Expense Ratios, exit load structures, benchmark tracking errors, and portfolio concentration before deploying capital across equity, debt, and hybrid buckets.
          </p>
        </div>

        <div class="feature-card" style="border-left: 5px solid var(--green-deep);">
          <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem;">
            <span style="background: var(--green-deep); color: white; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">5</span>
            <h3 style="margin: 0;">Stage 5 — Review Awareness</h3>
          </div>
          <p>
            Conducting systematic annual reviews to measure progress against milestones, rebalance drifted asset weights back to original allocations, and manage capital gains tax exposures.
          </p>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 12. team.html
    pages["team.html"] = {
        "title": "Team Overview | Wealth Management Advisory Professionals",
        "meta_desc": "Meet our educational advisory team structure. Professional profiles dedicated to research, financial planning literacy, and investor awareness.",
        "active_nav": "about",
        "breadcrumbs": [("Team", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Leadership &amp; Research</span>
      <h1 class="page-banner-title">Team Overview &amp; Advisory Profiles</h1>
      <p class="page-banner-desc">A disciplined group of financial planners, market researchers, and investor education specialists.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="mb-5">
        {make_placeholder("mutual-fund-team-collaboration.jpg", "Advisory Investment Committee Collaboration", "16-9", "A professional investment committee reviewing macroeconomic research and portfolio models.", "1200x675", "Advisory Team")}
      </div>

      <div class="regulatory-banner mb-5">
        <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <div>
          <strong>Demonstration Disclaimer:</strong> The team profiles below represent generic functional roles for demonstration purposes. In a live production deployment, verified credentials, certified designations, and regulatory registration disclosures must be reviewed and published.
        </div>
      </div>

      <div class="card-grid-3">
        <div class="feature-card text-center">
          <div style="width: 80px; height: 80px; border-radius: 50%; background: var(--bg-light); border: 2px solid var(--border-subtle); margin: 0 auto 1.25rem; display: flex; align-items: center; justify-content: center; color: var(--navy-primary);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          </div>
          <h3 class="feature-card-title">Senior Wealth Planner</h3>
          <p class="text-green font-semibold" style="font-size: 0.85rem; margin-bottom: 0.75rem;">Goal-Based Planning &amp; Allocation</p>
          <p class="feature-card-text">Specializes in long-term retirement roadmaps, cash flow modeling, and multi-asset allocation strategies for family offices and retail investors.</p>
        </div>

        <div class="feature-card text-center">
          <div style="width: 80px; height: 80px; border-radius: 50%; background: var(--bg-light); border: 2px solid var(--border-subtle); margin: 0 auto 1.25rem; display: flex; align-items: center; justify-content: center; color: var(--navy-primary);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          </div>
          <h3 class="feature-card-title">Mutual Fund Research Analyst</h3>
          <p class="text-green font-semibold" style="font-size: 0.85rem; margin-bottom: 0.75rem;">Fund Analytics &amp; Risk Metrics</p>
          <p class="feature-card-text">Focuses on quantitative scheme evaluations, portfolio overlap diagnosis, duration curves, and tracking error analytics.</p>
        </div>

        <div class="feature-card text-center">
          <div style="width: 80px; height: 80px; border-radius: 50%; background: var(--bg-light); border: 2px solid var(--border-subtle); margin: 0 auto 1.25rem; display: flex; align-items: center; justify-content: center; color: var(--navy-primary);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          </div>
          <h3 class="feature-card-title">Investor Education Specialist</h3>
          <p class="text-green font-semibold" style="font-size: 0.85rem; margin-bottom: 0.75rem;">Workshops &amp; Financial Literacy</p>
          <p class="feature-card-text">Leads corporate financial literacy initiatives, beginner guides, and investor awareness programs across Indian institutions.</p>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 13. insights.html
    pages["insights.html"] = {
        "title": "Financial Insights & Market Education | Mutual Fund Advisory",
        "meta_desc": "Explore in-depth articles on mutual fund operations, SIP strategies, direct plans, taxation rules, and asset allocation principles.",
        "active_nav": "insights",
        "breadcrumbs": [("Insights", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Knowledge Base</span>
      <h1 class="page-banner-title">Financial Insights &amp; Market Education</h1>
      <p class="page-banner-desc">Evidence-based perspectives, regulatory updates, and actionable frameworks for long-term investors.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="mb-5">
        {make_placeholder("mutual-fund-market-insights.jpg", "Financial Research & Market Insights Desk", "16-9", "A financial researcher reviewing macroeconomic charts, corporate earnings data, and capital market news.", "1200x675", "Insights Desk")}
      </div>

      <div class="card-grid-3">
        <div class="article-card">
          <div class="article-card-body">
            <div class="article-meta"><span>Fundamentals</span> &bull; <span>5 Min Read</span></div>
            <h3 class="article-title"><a href="article-details.html">Demystifying Mutual Funds: A Step-by-Step Educational Guide</a></h3>
            <p class="article-excerpt">How collective investment trusts work in India, AMC responsibilities, unit pricing, and regulatory protections.</p>
            <a href="article-details.html" class="feature-card-link">Read In-Depth &rarr;</a>
          </div>
        </div>

        <div class="article-card">
          <div class="article-card-body">
            <div class="article-meta"><span>Strategy</span> &bull; <span>6 Min Read</span></div>
            <h3 class="article-title"><a href="sip-investment.html">SIP vs Lump Sum: The Behavioral and Mathematical Trade-Off</a></h3>
            <p class="article-excerpt">Why rupee-cost averaging shields retail investors from emotional market tops and bottoms.</p>
            <a href="sip-investment.html" class="feature-card-link">Read In-Depth &rarr;</a>
          </div>
        </div>

        <div class="article-card">
          <div class="article-card-body">
            <div class="article-meta"><span>Costs &amp; Plans</span> &bull; <span>4 Min Read</span></div>
            <h3 class="article-title"><a href="direct-vs-regular.html">Direct vs Regular Plans: Understanding the Difference</a></h3>
            <p class="article-excerpt">How distributor commissions impact NAV and what service expectations accompany each plan option.</p>
            <a href="direct-vs-regular.html" class="feature-card-link">Read In-Depth &rarr;</a>
          </div>
        </div>

        <div class="article-card">
          <div class="article-card-body">
            <div class="article-meta"><span>Metrics</span> &bull; <span>5 Min Read</span></div>
            <h3 class="article-title"><a href="nav-explained.html">What Is NAV? The Most Common Pricing Misconception</a></h3>
            <p class="article-excerpt">Why a ₹10 NAV fund is not 'cheaper' than a ₹100 NAV fund, and how units accurately represent asset values.</p>
            <a href="nav-explained.html" class="feature-card-link">Read In-Depth &rarr;</a>
          </div>
        </div>

        <div class="article-card">
          <div class="article-card-body">
            <div class="article-meta"><span>Transparency</span> &bull; <span>5 Min Read</span></div>
            <h3 class="article-title"><a href="expense-ratio.html">How Total Expense Ratios (TER) Impact Returns</a></h3>
            <p class="article-excerpt">SEBI expense caps, AMC management charges, operating fees, and compounding cost drag.</p>
            <a href="expense-ratio.html" class="feature-card-link">Read In-Depth &rarr;</a>
          </div>
        </div>

        <div class="article-card">
          <div class="article-card-body">
            <div class="article-meta"><span>Taxation</span> &bull; <span>6 Min Read</span></div>
            <h3 class="article-title"><a href="investment-taxation.html">Navigating Mutual Fund Capital Gains Taxation</a></h3>
            <p class="article-excerpt">Understanding STCG and LTCG holding periods across equity and non-equity mutual fund schemes.</p>
            <a href="investment-taxation.html" class="feature-card-link">Read In-Depth &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 14. article-details.html
    pages["article-details.html"] = {
        "title": "Demystifying Mutual Funds | In-Depth Investor Article",
        "meta_desc": "Read our comprehensive editorial on how mutual funds pool investor capital, NAV mechanics, SEBI mandates, and goal-aligned investing.",
        "active_nav": "insights",
        "breadcrumbs": [("Insights", "insights.html"), ("Demystifying Mutual Funds", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Featured Article</span>
      <h1 class="page-banner-title">Demystifying Mutual Funds: A Step-by-Step Educational Guide</h1>
      <div style="display: flex; gap: 1rem; color: #CBD5E1; font-size: 0.85rem; margin-top: 0.75rem;">
        <span>Published: Educational Series</span> &bull; 
        <span>Reading Time: 8 Minutes</span> &bull; 
        <span>Topic: Mutual Fund Fundamentals</span>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container container-narrow">
      <div class="mb-5">
        {make_placeholder("mutual-fund-reading-factsheet.jpg", "How to Read a Mutual Fund Factsheet", "16-9", "An educational breakdown of a monthly mutual fund factsheet, showing top 10 holdings, sector weights, and expense disclosures.", "1200x675", "Factsheet Guide")}
      </div>

      <article style="font-size: 1.05rem; line-height: 1.8; color: var(--text-body);">
        <p class="font-medium" style="font-size: 1.15rem; color: var(--navy-primary); margin-bottom: 2rem;">
          Mutual funds have become the primary bridge connecting everyday Indian savings to the wealth-generating potential of domestic and global capital markets. Yet, misconceptions regarding safety, returns, and operational mechanics persist.
        </p>

        <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--navy-primary);">1. What Actually Happens When You Invest in a Mutual Fund?</h3>
        <p>
          When you purchase units in a mutual fund scheme, your money is pooled together with contributions from lakhs of fellow investors. This pooled capital is managed by an Asset Management Company (AMC) regulated under the SEBI (Mutual Funds) Regulations, 1996.
        </p>
        <p>
          A dedicated fund management team, supported by equity analysts and credit researchers, invests the corpus across hundreds of underlying securities according to the mandate published in the Scheme Information Document (SID).
        </p>

        <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--navy-primary);">2. Understanding the NAV (Net Asset Value)</h3>
        <p>
          The Net Asset Value is simply the total market value of all securities held in the portfolio, plus accrued dividends and interest, minus permissible scheme operating expenses, divided by the total number of outstanding units. NAV is computed at the close of every business day.
        </p>

        <div class="regulatory-banner my-4">
          <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          <div>
            <strong>Common Fallacy:</strong> A lower NAV does not mean a scheme is cheaper or has higher growth potential than a scheme with a higher NAV. The return percentage depends purely on the growth of the underlying securities in the portfolio.
          </div>
        </div>

        <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--navy-primary);">3. Direct vs Regular Plans</h3>
        <p>
          Every mutual fund scheme offers two choices: Direct Plan and Regular Plan. In a Direct Plan, no distributor commission is paid, resulting in a lower Total Expense Ratio and slightly higher net NAV compounding over decades. In a Regular Plan, a distribution commission is paid to an AMFI-registered distributor who provides investor guidance and execution support.
        </p>

        <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--navy-primary);">4. Conclusion: Discipline Over Speculation</h3>
        <p>
          Mutual funds are not lottery tickets; they are systematic wealth-compounding tools. Aligning your scheme selections with concrete life horizons and maintaining asset allocation through market fluctuations is the true cornerstone of financial independence.
        </p>
      </article>

      <div class="p-4 mt-5 text-center" style="background: var(--bg-light); border-radius: var(--radius-lg); border: 1px solid var(--border-subtle);">
        <h4>Looking to apply these concepts to your personal journey?</h4>
        <p class="mb-3">Explore our interactive SIP Calculator or submit an educational enquiry.</p>
        <div class="btn-group" style="justify-content: center;">
          <a href="sip-calculator.html" class="btn btn-outline">SIP Calculator</a>
          <a href="consultation.html" class="btn btn-primary">Request Consultation</a>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 15. faq.html
    pages["faq.html"] = {
        "title": "Frequently Asked Questions | Mutual Fund Advisory FAQs",
        "meta_desc": "Find clear answers to common questions about mutual funds, SIP mechanics, capital gains taxes, direct vs regular plans, and safety regulations in India.",
        "active_nav": "resources",
        "breadcrumbs": [("FAQs", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Knowledge Clearinghouse</span>
      <h1 class="page-banner-title">Frequently Asked Questions</h1>
      <p class="page-banner-desc">Clear, objective answers to fundamental questions about mutual fund investing and regulatory standards.</p>
    </div>
  </section>

  <section class="section">
    <div class="container container-narrow">
      <div class="mb-5">
        {make_placeholder("mutual-fund-faq-support.jpg", "Investor Support & Client Helpdesk Interface", "16-9", "A helpful customer support desk assisting investors with KYC inquiries, portal navigation, and scheme documentation.", "1200x675", "FAQ Support")}
      </div>

      <div class="accordion-container">
        <!-- FAQ 1 -->
        <div class="accordion-item active">
          <button class="accordion-button" aria-expanded="true">
            <span>What exactly is a mutual fund, and are my returns guaranteed?</span>
            <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="accordion-collapse" style="max-height: 300px;">
            <div class="accordion-body">
              A mutual fund pools savings from multiple investors to invest in a diversified portfolio of securities (equities, bonds, money market instruments) managed by an Asset Management Company (AMC). <strong>Mutual funds never guarantee returns.</strong> Portfolio values fluctuate daily according to market conditions and underlying security performance.
            </div>
          </div>
        </div>

        <!-- FAQ 2 -->
        <div class="accordion-item">
          <button class="accordion-button" aria-expanded="false">
            <span>How does an SIP differ from a lump sum investment?</span>
            <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="accordion-collapse">
            <div class="accordion-body">
              In a lump sum investment, you deploy a single capital amount on a specific date, which exposes your purchase to prevailing market valuations. In a Systematic Investment Plan (SIP), you invest a fixed sum periodically (typically monthly), benefiting from rupee-cost averaging where more units are bought during downturns and fewer during peaks.
            </div>
          </div>
        </div>

        <!-- FAQ 3 -->
        <div class="accordion-item">
          <button class="accordion-button" aria-expanded="false">
            <span>What is the difference between Direct and Regular plans?</span>
            <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="accordion-collapse">
            <div class="accordion-body">
              Direct Plans are purchased directly from the AMC without distributor commissions, giving them a lower Total Expense Ratio (TER) and higher NAV. Regular Plans are transacted through an AMFI-registered distributor whose commission is deducted from the scheme expense, in exchange for distributor assistance.
            </div>
          </div>
        </div>

        <!-- FAQ 4 -->
        <div class="accordion-item">
          <button class="accordion-button" aria-expanded="false">
            <span>What is an ELSS fund and what are the lock-in rules?</span>
            <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="accordion-collapse">
            <div class="accordion-body">
              An Equity Linked Savings Scheme (ELSS) is a diversified equity fund eligible for tax deduction under Section 80C of the Income Tax Act (under the Old Tax Regime). It has a statutory lock-in period of 3 years from the date of each individual unit purchase. Units cannot be redeemed before 36 months have elapsed.
            </div>
          </div>
        </div>

        <!-- FAQ 5 -->
        <div class="accordion-item">
          <button class="accordion-button" aria-expanded="false">
            <span>How are mutual fund capital gains taxed in India?</span>
            <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="accordion-collapse">
            <div class="accordion-body">
              Taxation depends on the asset classification (equity vs debt/specified mutual funds), the holding duration, and applicable statutory provisions. For equity funds, holding more than 12 months constitutes long-term capital gains, while holding 12 months or less is short-term. Tax laws evolve periodically; investors must consult current tax provisions or a qualified tax adviser.
            </div>
          </div>
        </div>

        <!-- FAQ 6 -->
        <div class="accordion-item">
          <button class="accordion-button" aria-expanded="false">
            <span>What is the SEBI Riskometer?</span>
            <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="accordion-collapse">
            <div class="accordion-body">
              The Riskometer is a graphical depiction mandated by SEBI displaying six risk tiers: Low, Low to Moderate, Moderate, Moderately High, High, and Very High. It is calculated by AMCs each month based on actual underlying portfolio attributes (credit risk, duration, liquidity, market cap).
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 16. contact.html
    pages["contact.html"] = {
        "title": "Contact Us | Mutual Fund Advisory Enquiry & Office",
        "meta_desc": "Get in touch with Mutual Fund Advisory. Phone: 0000000000, demo@example.com, Hyderabad, Telangana. Submit an educational consultation enquiry.",
        "active_nav": "contact",
        "breadcrumbs": [("Contact Us", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Get in Touch</span>
      <h1 class="page-banner-title">Contact Mutual Fund Advisory</h1>
      <p class="page-banner-desc">Reach out for general enquiries, educational workshops, or consultation scheduling.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2">
        <div>
          <span class="section-tag">Communication Channels</span>
          <h2 class="section-title">We Are Here to Assist Your Financial Education</h2>
          <p class="mb-4">
            Connect with our advisory desk for questions regarding mutual fund categories, educational frameworks, or corporate employee sessions.
          </p>

          <div class="footer-contact-info mb-4" style="font-size: 1rem; gap: 1rem;">
            <div class="footer-contact-item">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-green"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              <span><strong>Telephone:</strong> 0000000000</span>
            </div>
            <div class="footer-contact-item">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-green"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <span><strong>Email:</strong> demo@example.com</span>
            </div>
            <div class="footer-contact-item">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-green"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <span><strong>Office Address:</strong> Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000</span>
            </div>
          </div>

          <div class="mb-4">
            {make_placeholder("mutual-fund-advisory-office.jpg", "Advisory Headquarters & Welcome Reception", "4-3", "A modern, professional wealth management reception desk in Hyderabad with financial market displays.", "1000x750", "Office Visual")}
          </div>

          <div class="regulatory-banner">
            <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <div>
              <strong>Safe Harbor Notice:</strong> Please do not share PAN numbers, bank account numbers, Aadhaar details, Demat login credentials, or portfolio statements via contact forms.
            </div>
          </div>
        </div>

        <div>
          <div class="form-card">
            <h3 style="margin-bottom: 1.25rem;">Send a General Enquiry</h3>

            <div id="contactSuccessAlert" class="form-success-alert">
              Demo enquiry submitted successfully. No personal information has been transmitted or stored.
            </div>

            <form id="contactForm" novalidate>
              <div class="form-group">
                <label for="contactName" class="form-label">Full Name *</label>
                <input type="text" id="contactName" class="form-control" placeholder="Enter your full name">
                <span class="form-error-msg">Please enter your full name.</span>
              </div>

              <div class="form-group">
                <label for="contactEmail" class="form-label">Email Address *</label>
                <input type="email" id="contactEmail" class="form-control" placeholder="name@example.com">
                <span class="form-error-msg">Please enter a valid email address.</span>
              </div>

              <div class="form-group">
                <label for="contactMessage" class="form-label">Message / Enquiry *</label>
                <textarea id="contactMessage" class="form-control" placeholder="How can we assist your mutual fund educational journey?"></textarea>
                <span class="form-error-msg">Please enter your message.</span>
              </div>

              <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">Submit Demo Message</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # Write each file
    for filename, pdata in pages.items():
        html = render_html_page(
            filename=filename,
            title=pdata["title"],
            meta_desc=pdata["meta_desc"],
            active_nav=pdata["active_nav"],
            breadcrumbs=pdata["breadcrumbs"],
            content_html=pdata["content"]
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {filename}")

if __name__ == "__main__":
    build_core_pages()
