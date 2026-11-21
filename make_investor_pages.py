"""
Generate 7 Investor & Enquiry Pages + 5 Legal/Disclosure Pages (12 Total) with Dedicated Placeholders
"""

from templates import render_html_page, make_placeholder

def build_investor_and_legal_pages():
    pages = {}

    # 1. investor-resources.html
    pages["investor-resources.html"] = {
        "title": "Investor Resources & Glossary | Mutual Fund Advisory",
        "meta_desc": "Comprehensive mutual fund investor resources: financial glossary, factsheet checklist, regulatory bodies, and educational guides for Indian investors.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Knowledge Clearinghouse</span>
      <h1 class="page-banner-title">Investor Resource Library</h1>
      <p class="page-banner-desc">Curated educational references, factsheet checklists, and financial terminology guides to assist your investment literacy.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="mb-5">
        {make_placeholder("mutual-fund-investor-resources-library.jpg", "Digital Financial Knowledge & Resource Repository", "16-9", "A digital library interface displaying curated financial literacy guides, factsheet templates, and regulatory whitepapers.", "1200x675", "Resource Library")}
      </div>

      <div class="card-grid-3 mb-5">
        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          </div>
          <h3 class="feature-card-title">Interactive Calculators</h3>
          <p class="feature-card-text">Explore our suite of educational financial calculators to model SIP accumulation, lump sum compounding, and goal shortfalls.</p>
          <a href="sip-calculator.html" class="feature-card-link">Explore Calculators &rarr;</a>
        </div>

        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
          </div>
          <h3 class="feature-card-title">Risk Questionnaire</h3>
          <p class="feature-card-text">Complete our demo 5-question risk awareness questionnaire to understand how time horizon and volatility appetite interact.</p>
          <a href="risk-profile-questionnaire.html" class="feature-card-link">Take Questionnaire &rarr;</a>
        </div>

        <div class="feature-card">
          <div class="feature-card-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          </div>
          <h3 class="feature-card-title">Corporate Workshops</h3>
          <p class="feature-card-text">Discover structured workplace financial literacy modules covering budgeting, taxation awareness, and retirement clinics.</p>
          <a href="corporate-investment-planning.html" class="feature-card-link">Corporate Education &rarr;</a>
        </div>
      </div>

      <!-- Mutual Fund Glossary -->
      <div class="section-header">
        <span class="section-tag tag-gold">Reference Dictionary</span>
        <h2 class="section-title">Key Financial Terminology</h2>
        <p class="section-subtitle">Plain-English definitions of essential Indian mutual fund acronyms and concepts.</p>
      </div>

      <div class="comparison-table-wrapper mb-5">
        <table class="comparison-table">
          <thead>
            <tr>
              <th style="width: 20%;">Term / Acronym</th>
              <th>Plain-English Definition &amp; Context</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>AMC</strong></td>
              <td><strong>Asset Management Company:</strong> The corporate entity registered with SEBI that manages the pooled money of mutual fund schemes.</td>
            </tr>
            <tr>
              <td><strong>NAV</strong></td>
              <td><strong>Net Asset Value:</strong> The per-unit market value of a scheme calculated daily by dividing net assets by outstanding units.</td>
            </tr>
            <tr>
              <td><strong>TER</strong></td>
              <td><strong>Total Expense Ratio:</strong> The annual percentage of fund assets deducted daily to cover fund management, custodian, and registrar costs.</td>
            </tr>
            <tr>
              <td><strong>SID &amp; KIM</strong></td>
              <td><strong>Scheme Information Document &amp; Key Information Memorandum:</strong> Statutory legal offer documents detailing fund mandate, asset allocation limits, and risk factors.</td>
            </tr>
            <tr>
              <td><strong>Macaulay Duration</strong></td>
              <td>The weighted average time until all bond cash flows are received, measuring a debt fund's sensitivity to interest rate movements.</td>
            </tr>
            <tr>
              <td><strong>Tracking Error</strong></td>
              <td>The annualized standard deviation of the difference in returns between an index fund and its target benchmark index.</td>
            </tr>
            <tr>
              <td><strong>AUM</strong></td>
              <td><strong>Assets Under Management:</strong> The aggregate market value of all investments managed by a specific scheme or AMC.</td>
            </tr>
            <tr>
              <td><strong>SWP &amp; STP</strong></td>
              <td><strong>Systematic Withdrawal Plan &amp; Systematic Transfer Plan:</strong> Automated facilities to withdraw fixed cash or transfer tranches between schemes periodically.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
"""
    }

    # 2. sip-calculator.html
    pages["sip-calculator.html"] = {
        "title": "SIP Calculator | Systematic Investment Plan Growth Estimator",
        "meta_desc": "Calculate your illustrative mutual fund SIP growth: monthly contributions, time horizon, expected return rate, total invested, and estimated returns.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("SIP Calculator", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Interactive Tool</span>
      <h1 class="page-banner-title">Mutual Fund SIP Calculator</h1>
      <p class="page-banner-desc">Explore how monthly systematic contributions accumulate over different investment timeframes using standard compounding mathematics.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="mb-5">
        {make_placeholder("mutual-fund-sip-calculator-interface.jpg", "Interactive SIP Financial Modeling Platform", "16-9", "A user interacting with an advanced financial calculator interface displaying dynamic growth curves.", "1200x675", "Calculator Interface")}
      </div>

      <div class="calculator-wrapper mb-5">
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
                <label for="sipYearsRange" class="calc-label">Investment Horizon (Years)</label>
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
                Mutual fund investments are subject to market risks. Actual returns fluctuate and calculations exclude scheme expenses, exit loads, and applicable taxes. This tool does not recommend any specific scheme.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 3. lumpsum-calculator.html
    pages["lumpsum-calculator.html"] = {
        "title": "Lump Sum Calculator | One-Time Investment Growth Estimator",
        "meta_desc": "Calculate potential mutual fund growth for one-time lump sum investments: principal capital, annual growth assumptions, and future values.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Lump Sum Calculator", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Interactive Tool</span>
      <h1 class="page-banner-title">Mutual Fund Lump Sum Calculator</h1>
      <p class="page-banner-desc">Model the compounding potential of a single one-time capital investment over customized time horizons.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="mb-5">
        {make_placeholder("mutual-fund-lump-sum-calculator-interface.jpg", "Lump Sum Portfolio Growth Modeler", "16-9", "A digital dashboard showing single-deposit compounding projections over multi-year horizons.", "1200x675", "Lump Sum Modeler")}
      </div>

      <div class="calculator-wrapper mb-5">
        <div class="calculator-grid">
          <div>
            <div class="calc-control-group">
              <div class="calc-label-row">
                <label for="lumpAmountRange" class="calc-label">Total Investment Amount (₹)</label>
                <div class="calc-input-display">
                  <span>₹</span>
                  <input type="number" id="lumpAmountInput" value="100000" min="5000" max="10000000" step="5000">
                </div>
              </div>
              <input type="range" id="lumpAmountRange" class="calc-range-slider" min="5000" max="2500000" step="5000" value="100000">
            </div>

            <div class="calc-control-group">
              <div class="calc-label-row">
                <label for="lumpRateRange" class="calc-label">Expected Annual Return Rate (%)</label>
                <div class="calc-input-display">
                  <input type="number" id="lumpRateInput" value="11" min="1" max="30" step="0.5">
                  <span>%</span>
                </div>
              </div>
              <input type="range" id="lumpRateRange" class="calc-range-slider" min="1" max="25" step="0.5" value="11">
            </div>

            <div class="calc-control-group">
              <div class="calc-label-row">
                <label for="lumpYearsRange" class="calc-label">Investment Period (Years)</label>
                <div class="calc-input-display">
                  <input type="number" id="lumpYearsInput" value="5" min="1" max="35" step="1">
                  <span>Yrs</span>
                </div>
              </div>
              <input type="range" id="lumpYearsRange" class="calc-range-slider" min="1" max="30" step="1" value="5">
            </div>

            <div class="btn-group mt-4">
              <button type="button" id="lumpResetBtn" class="btn btn-outline btn-sm">Reset Inputs</button>
            </div>
          </div>

          <div>
            <div class="calc-results-card">
              <h4 style="margin-bottom: 1rem; color: var(--navy-primary);">Illustrative Output Breakdown</h4>
              <div class="calc-stat-box">
                <span class="calc-stat-label">Initial Principal Invested:</span>
                <span class="calc-stat-val" id="lumpInvestedDisplay">₹1,00,000</span>
              </div>
              <div class="calc-stat-box">
                <span class="calc-stat-label">Illustrative Est. Gain:</span>
                <span class="calc-stat-val text-green" id="lumpGainDisplay">₹68,506</span>
              </div>
              <div class="calc-stat-box highlight">
                <span class="calc-stat-label">Estimated Future Value:</span>
                <span class="calc-stat-val" id="lumpTotalDisplay">₹1,68,506</span>
              </div>

              <div class="calc-breakdown-bar">
                <div class="calc-bar-invested" id="lumpBarInvested" style="width: 59%;"></div>
                <div class="calc-bar-gain" id="lumpBarGain" style="width: 41%;"></div>
              </div>
              <div class="calc-legend">
                <div class="calc-legend-item">
                  <span class="legend-dot dot-invested"></span>
                  <span>Invested Principal</span>
                </div>
                <div class="calc-legend-item">
                  <span class="legend-dot dot-gain"></span>
                  <span>Compounded Gains</span>
                </div>
              </div>

              <div class="calc-disclaimer-box">
                <strong>ILLUSTRATIVE ESTIMATE — NOT A PREDICTION OR GUARANTEE OF MUTUAL FUND RETURNS.</strong>
                Mutual fund investments are subject to market risks. Actual market performance fluctuates daily and calculations do not account for taxes or exit charges.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 4. goal-planning-calculator.html
    pages["goal-planning-calculator.html"] = {
        "title": "Goal Planning Calculator | Milestone Corpus & SIP Requirements",
        "meta_desc": "Calculate your goal target corpus, future value of current savings, shortfall, and required monthly SIP using standard financial math.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Goal Planning Calculator", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Milestone Planning</span>
      <h1 class="page-banner-title">Goal Planning Financial Calculator</h1>
      <p class="page-banner-desc">Determine the required monthly SIP contribution needed to bridge the gap between current savings and your future goal target.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="mb-5">
        {make_placeholder("mutual-fund-goal-calculator-interface.jpg", "Goal Planning & Shortfall Calculation Visualizer", "16-9", "A visual analytics tool calculating future target shortfalls and displaying recommended monthly SIP paths.", "1200x675", "Goal Shortfall Visualizer")}
      </div>

      <div class="calculator-wrapper mb-5">
        <div class="calculator-grid">
          <div>
            <div class="calc-control-group">
              <div class="calc-label-row">
                <label for="goalTargetRange" class="calc-label">Target Goal Amount (₹)</label>
                <div class="calc-input-display">
                  <span>₹</span>
                  <input type="number" id="goalTargetInput" value="5000000" min="50000" max="100000000" step="50000">
                </div>
              </div>
              <input type="range" id="goalTargetRange" class="calc-range-slider" min="500000" max="25000000" step="100000" value="5000000">
            </div>

            <div class="calc-control-group">
              <div class="calc-label-row">
                <label for="goalYearsRange" class="calc-label">Time to Goal (Years)</label>
                <div class="calc-input-display">
                  <input type="number" id="goalYearsInput" value="10" min="1" max="35" step="1">
                  <span>Yrs</span>
                </div>
              </div>
              <input type="range" id="goalYearsRange" class="calc-range-slider" min="1" max="30" step="1" value="10">
            </div>

            <div class="calc-control-group">
              <div class="calc-label-row">
                <label for="goalSavingsRange" class="calc-label">Current Savings Earmarked (₹)</label>
                <div class="calc-input-display">
                  <span>₹</span>
                  <input type="number" id="goalSavingsInput" value="200000" min="0" max="10000000" step="10000">
                </div>
              </div>
              <input type="range" id="goalSavingsRange" class="calc-range-slider" min="0" max="5000000" step="25000" value="200000">
            </div>

            <div class="calc-control-group">
              <div class="calc-label-row">
                <label for="goalRateRange" class="calc-label">Assumed Annual Return Rate (%)</label>
                <div class="calc-input-display">
                  <input type="number" id="goalRateInput" value="12" min="1" max="25" step="0.5">
                  <span>%</span>
                </div>
              </div>
              <input type="range" id="goalRateRange" class="calc-range-slider" min="1" max="20" step="0.5" value="12">
            </div>

            <div class="btn-group mt-4">
              <button type="button" id="goalResetBtn" class="btn btn-outline btn-sm">Reset Inputs</button>
            </div>
          </div>

          <div>
            <div class="calc-results-card">
              <h4 style="margin-bottom: 1rem; color: var(--navy-primary);">Target Gap &amp; SIP Output</h4>
              <div class="calc-stat-box">
                <span class="calc-stat-label">Target Milestone Amount:</span>
                <span class="calc-stat-val" id="goalTargetDisplay">₹50,00,000</span>
              </div>
              <div class="calc-stat-box">
                <span class="calc-stat-label">Future Value of Current Savings:</span>
                <span class="calc-stat-val" id="goalCurrentFvDisplay">₹6,21,170</span>
              </div>
              <div class="calc-stat-box">
                <span class="calc-stat-label">Corpus Shortfall:</span>
                <span class="calc-stat-val text-navy" id="goalShortfallDisplay">₹43,78,830</span>
              </div>
              <div class="calc-stat-box highlight">
                <span class="calc-stat-label">Required Monthly SIP:</span>
                <span class="calc-stat-val text-green" id="goalMonthlyReqDisplay">₹18,846</span>
              </div>

              <div class="calc-disclaimer-box">
                <strong>MATHEMATICAL ILLUSTRATION — NOT A FORECAST OR GUARANTEE.</strong>
                Calculations represent compound interest approximations and do not constitute personalized investment advice or scheme recommendations.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 5. risk-profile-questionnaire.html
    pages["risk-profile-questionnaire.html"] = {
        "title": "Demo Risk Education Questionnaire | Investor Risk Awareness",
        "meta_desc": "Take our interactive 5-question demo risk education questionnaire to understand how risk tolerance, capacity, and time horizon interact.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Demo Risk Questionnaire", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Self-Assessment Tool</span>
      <h1 class="page-banner-title">Demo Risk Education Questionnaire</h1>
      <p class="page-banner-desc">An educational exercise illustrating how investment horizons, emotional tolerance, and liquidity needs shape portfolio perspectives.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="mb-5">
        {make_placeholder("mutual-fund-risk-questionnaire-assessment.jpg", "Investor Risk Profiling Educational Survey", "16-9", "An intuitive risk assessment digital dashboard measuring investor drawdown tolerance and investment horizons.", "1200x675", "Risk Assessment Survey")}
      </div>

      <div class="regulatory-banner mb-5">
        <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <div>
          <strong>IMPORTANT EDUCATIONAL SAFEGUARD:</strong><br>
          This questionnaire is a frontend-only educational simulation. It does NOT constitute an approved SEBI suitability assessment or official risk profile. Results are for conceptual awareness only and do not generate scheme recommendations. No personal or financial responses are recorded or stored.
        </div>
      </div>

      <div class="questionnaire-card">
        <form id="riskQuestionnaireForm">
          <!-- Q1 -->
          <div class="question-block">
            <div class="question-title">1. What is your expected investment time horizon for this capital?</div>
            <div class="question-options-list">
              <label class="option-label">
                <input type="radio" name="q1" value="1" required>
                <div class="option-text-wrap">
                  <strong>Less than 2 years</strong>
                  <span>Short-term goals where capital preservation and quick liquidity are paramount.</span>
                </div>
              </label>
              <label class="option-label">
                <input type="radio" name="q1" value="2">
                <div class="option-text-wrap">
                  <strong>3 to 5 years</strong>
                  <span>Medium-term goals allowing moderate volatility for capital growth.</span>
                </div>
              </label>
              <label class="option-label">
                <input type="radio" name="q1" value="4">
                <div class="option-text-wrap">
                  <strong>More than 7 years</strong>
                  <span>Long-term wealth creation capable of enduring multiple business and market cycles.</span>
                </div>
              </label>
            </div>
          </div>

          <!-- Q2 -->
          <div class="question-block">
            <div class="question-title">2. If your portfolio experienced a temporary 20% paper drop during a market correction, how would you react?</div>
            <div class="question-options-list">
              <label class="option-label">
                <input type="radio" name="q2" value="1" required>
                <div class="option-text-wrap">
                  <strong>Panic and sell all holdings to prevent further losses</strong>
                  <span>High sensitivity to volatility; prefer capital certainty.</span>
                </div>
              </label>
              <label class="option-label">
                <input type="radio" name="q2" value="2">
                <div class="option-text-wrap">
                  <strong>Feel anxious but hold on until markets recover</strong>
                  <span>Moderate volatility tolerance; uncomfortable adding fresh capital.</span>
                </div>
              </label>
              <label class="option-label">
                <input type="radio" name="q2" value="4">
                <div class="option-text-wrap">
                  <strong>View it as an opportunity to purchase more units via SIP at lower valuations</strong>
                  <span>Comfortable with equity cyclicality and disciplined compounding.</span>
                </div>
              </label>
            </div>
          </div>

          <!-- Q3 -->
          <div class="question-block">
            <div class="question-title">3. What is your primary objective for this investment portfolio?</div>
            <div class="question-options-list">
              <label class="option-label">
                <input type="radio" name="q3" value="1" required>
                <div class="option-text-wrap">
                  <strong>Capital Protection</strong>
                  <span>Preventing capital erosion is more important than achieving high returns.</span>
                </div>
              </label>
              <label class="option-label">
                <input type="radio" name="q3" value="2">
                <div class="option-text-wrap">
                  <strong>Balanced Growth with Downside Protection</strong>
                  <span>Beating inflation with measured volatility through multi-asset allocations.</span>
                </div>
              </label>
              <label class="option-label">
                <input type="radio" name="q3" value="4">
                <div class="option-text-wrap">
                  <strong>Maximum Long-Term Capital Growth</strong>
                  <span>Aggressively compounding wealth across diversified equity markets.</span>
                </div>
              </label>
            </div>
          </div>

          <!-- Q4 -->
          <div class="question-block">
            <div class="question-title">4. How secure is your current primary income and emergency liquidity reserve?</div>
            <div class="question-options-list">
              <label class="option-label">
                <input type="radio" name="q4" value="1" required>
                <div class="option-text-wrap">
                  <strong>Uncertain income / Less than 3 months of emergency expenses saved</strong>
                  <span>Low capacity to absorb market drawdowns or illiquidity.</span>
                </div>
              </label>
              <label class="option-label">
                <input type="radio" name="q4" value="2">
                <div class="option-text-wrap">
                  <strong>Stable income / 3 to 6 months of living expenses saved</strong>
                  <span>Moderate financial cushion to weather temporary disruptions.</span>
                </div>
              </label>
              <label class="option-label">
                <input type="radio" name="q4" value="3">
                <div class="option-text-wrap">
                  <strong>Highly predictable income / Over 6 months of living expenses safely parked</strong>
                  <span>Robust financial risk capacity; long-term investments will not be needed early.</span>
                </div>
              </label>
            </div>
          </div>

          <!-- Q5 -->
          <div class="question-block">
            <div class="question-title">5. What is your prior familiarity with capital market fluctuations?</div>
            <div class="question-options-list">
              <label class="option-label">
                <input type="radio" name="q5" value="1" required>
                <div class="option-text-wrap">
                  <strong>First-time investor with zero market experience</strong>
                  <span>Familiar only with fixed deposits, postal schemes, and savings accounts.</span>
                </div>
              </label>
              <label class="option-label">
                <input type="radio" name="q5" value="2">
                <div class="option-text-wrap">
                  <strong>Have invested in mutual funds for a few years</strong>
                  <span>Understand NAV concept and have witnessed moderate market swings.</span>
                </div>
              </label>
              <label class="option-label">
                <input type="radio" name="q5" value="3">
                <div class="option-text-wrap">
                  <strong>Experienced investor who has navigated multiple bear markets</strong>
                  <span>Thorough understanding of equity drawdowns, debt credit risks, and asset allocation.</span>
                </div>
              </label>
            </div>
          </div>

          <div class="btn-group" style="justify-content: center; margin-top: 2rem;">
            <button type="submit" class="btn btn-primary btn-lg">Calculate Illustrative Profile</button>
            <button type="button" id="riskResetBtn" class="btn btn-outline btn-lg">Reset Answers</button>
          </div>
        </form>

        <div id="riskResultBox" class="questionnaire-result">
          <span class="section-tag tag-navy mb-2">Illustrative Educational Profile</span>
          <h3 id="riskCategoryTitle" style="color: var(--navy-primary); margin-bottom: 0.75rem;"></h3>
          <p id="riskCategoryDesc" style="color: var(--text-body); max-width: 650px; margin: 0 auto; line-height: 1.6;"></p>
          <div class="mt-4">
            <a href="asset-allocation.html" class="btn btn-navy btn-sm">Explore Matching Asset Allocation Concepts &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 6. consultation.html
    pages["consultation.html"] = {
        "title": "Consultation Enquiry | Wealth Management Education Desk",
        "meta_desc": "Schedule a structured educational consultation. Enquire about mutual fund concepts, portfolio reviews, SIP planning, or corporate workshops.",
        "active_nav": "contact",
        "breadcrumbs": [("Consultation Enquiry", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Structured Discussion</span>
      <h1 class="page-banner-title">Request an Educational Consultation</h1>
      <p class="page-banner-desc">Connect with our wealth advisory desk to discuss portfolio principles, goal mapping, and disciplined investment strategies.</p>
    </div>
  </section>

  <section class="section">
    <div class="container container-narrow">
      <div class="mb-5">
        {make_placeholder("mutual-fund-consultation-advisory-desk.jpg", "Financial Consultation & Wealth Advisory Meeting", "16-9", "A wealth advisor conducting an introductory financial consultation with an investor in a private meeting room.", "1200x675", "Advisory Consultation")}
      </div>

      <div class="regulatory-banner mb-4">
        <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <div>
          <strong>CONFIDENTIALITY &amp; SAFE HARBOR SAFEGUARD:</strong><br>
          This form is an educational demonstration interface. <strong>Do NOT submit PAN, Aadhaar, bank account numbers, Demat credentials, mutual fund account passwords, or financial statements.</strong> No personal or financial information is transmitted to any server or stored in any database.
        </div>
      </div>

      <div class="form-card">
        <div class="form-step-indicators">
          <div class="form-step-tab active" data-step="1">1. Contact Details</div>
          <div class="form-step-tab" data-step="2">2. Discussion Scope</div>
          <div class="form-step-tab" data-step="3">3. Preferred Schedule</div>
        </div>

        <div id="consultSuccessAlert" class="form-success-alert">
          Demo enquiry submitted successfully. No personal information has been transmitted or stored.
        </div>

        <form id="consultationForm" novalidate>
          <!-- Step 1 -->
          <div class="consult-step-section" id="step1">
            <div class="form-group">
              <label for="fullName" class="form-label">Full Name *</label>
              <input type="text" id="fullName" class="form-control" placeholder="Enter your full name">
              <span class="form-error-msg">Please enter your full name.</span>
            </div>

            <div class="form-group">
              <label for="emailAddress" class="form-label">Email Address *</label>
              <input type="email" id="emailAddress" class="form-control" placeholder="name@example.com">
              <span class="form-error-msg">Please enter a valid email address.</span>
            </div>

            <div class="form-group">
              <label for="phoneNumber" class="form-label">Phone Number (10 Digits) *</label>
              <input type="tel" id="phoneNumber" class="form-control" placeholder="e.g. 9876543210">
              <span class="form-error-msg">Please enter a valid 10-digit mobile number.</span>
            </div>

            <div class="form-group">
              <label for="userCity" class="form-label">City of Residence</label>
              <input type="text" id="userCity" class="form-control" placeholder="e.g. Hyderabad, Bengaluru, Mumbai">
            </div>
          </div>

          <!-- Step 2 -->
          <div class="consult-step-section" id="step2" style="display: none;">
            <div class="form-group">
              <label for="enquiryType" class="form-label">Primary Consultation Scope *</label>
              <select id="enquiryType" class="form-control">
                <option value="education">Mutual Fund General Education</option>
                <option value="sip">SIP Strategy &amp; Rupee-Cost Averaging</option>
                <option value="planning">Goal-Based Financial Planning</option>
                <option value="review">Portfolio Review &amp; Health Check Concepts</option>
                <option value="corporate">Corporate Financial Education Session</option>
                <option value="general">General Advisory Enquiry</option>
              </select>
            </div>

            <div class="form-group">
              <label for="consultMessage" class="form-label">Brief Background or Questions</label>
              <textarea id="consultMessage" class="form-control" placeholder="What specific financial topics or goals would you like to explore during the session?"></textarea>
            </div>
          </div>

          <!-- Step 3 -->
          <div class="consult-step-section" id="step3" style="display: none;">
            <div class="form-group">
              <label for="preferredMethod" class="form-label">Preferred Mode of Discussion</label>
              <select id="preferredMethod" class="form-control">
                <option value="video">Virtual Video Conference (Google Meet / Zoom)</option>
                <option value="phone">Direct Phone Call</option>
                <option value="inperson">In-Person Consultation (Office)</option>
              </select>
            </div>

            <div class="form-group">
              <label for="preferredTime" class="form-label">Preferred Time Window</label>
              <select id="preferredTime" class="form-control">
                <option value="morning">Morning (10:00 AM - 1:00 PM)</option>
                <option value="afternoon">Afternoon (2:00 PM - 5:00 PM)</option>
                <option value="evening">Evening (5:00 PM - 7:30 PM)</option>
              </select>
            </div>
          </div>

          <div class="btn-group mt-4" style="justify-content: space-between;">
            <button type="button" id="prevStepBtn" class="btn btn-outline" style="display: none;">&larr; Previous Step</button>
            <button type="button" id="nextStepBtn" class="btn btn-primary">Continue to Next Step &rarr;</button>
          </div>
        </form>
      </div>
    </div>
  </section>
"""
    }

    # 7. corporate-investment-planning.html
    pages["corporate-investment-planning.html"] = {
        "title": "Corporate Financial Education | Workplace Wellness Workshops",
        "meta_desc": "Workplace financial literacy programs: mutual fund basics, retirement awareness, tax planning, and systematic savings workshops for Indian corporate teams.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Corporate Financial Education", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Workplace Wellness</span>
      <h1 class="page-banner-title">Corporate Financial Education Programs</h1>
      <p class="page-banner-desc">Empower your workforce with evidence-based personal finance literacy, retirement clinics, and systematic investing workshops.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Employee Financial Wellness</span>
          <h2 class="section-title">Why Financial Literacy Matters to Employers</h2>
          <p>
            Financial stress is one of the leading contributors to workplace anxiety, reduced focus, and employee turnover. While organizations provide competitive compensation and retirement provident funds (EPF), many employees lack a structured understanding of how to manage savings, navigate inflation, and build wealth through mutual funds.
          </p>
          <p>
            Our unbiased corporate workshops equip employees at all career stages—from new campus hires to senior executives—with objective financial principles.
          </p>
          <div class="regulatory-banner">
            <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <div>
              <strong>Pure Educational Mandate:</strong> Corporate sessions are strictly educational. We do not sell financial products, solicit scheme investments, or offer individual stock tips during employee workshops.
            </div>
          </div>
        </div>

        <div>
          {make_placeholder("mutual-fund-corporate-workshop.jpg", "Corporate Financial Literacy Workshop", "4-3", "An engaging workplace seminar with corporate employees attending a financial planning masterclass.", "1000x750", "Corporate Education Visual")}
        </div>
      </div>

      <!-- Workshop Modules -->
      <div class="section-header">
        <span class="section-tag tag-gold">Modular Curriculum</span>
        <h2 class="section-title">Core Workplace Educational Modules</h2>
      </div>

      <div class="card-grid-3 mb-5">
        <div class="feature-card">
          <h4 class="feature-card-title">1. Young Professionals: Money 101</h4>
          <p class="feature-card-text">Budgeting, emergency funds, understanding CKYC, the dangers of high-interest revolving credit, and starting early ₹1,000 SIPs.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">2. Tax Literacy &amp; Regime Comparison</h4>
          <p class="feature-card-text">Demystifying the Old vs New Tax Regime, Section 80C deductions (ELSS), capital gains taxes, and optimizing salary structures.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">3. Mid-Career Milestone Mapping</h4>
          <p class="feature-card-text">Balancing home down payments, child education inflation, and establishing multi-asset portfolios across equity and debt.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">4. Retirement Readiness Clinics</h4>
          <p class="feature-card-text">Synergizing EPF, gratuity, NPS, and equity mutual funds to construct sustainable post-retirement cash flow streams via SWP.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">5. Market Volatility &amp; Psychology</h4>
          <p class="feature-card-text">Equipping employees with the behavioral discipline required to remain calm during market corrections and avoid speculative trading.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">6. Family Financial Security</h4>
          <p class="feature-card-text">Nominations, joint holdings, wills, estate basics, and ensuring financial records are transparently organized for loved ones.</p>
        </div>
      </div>

      <div class="p-4 text-center" style="background: var(--bg-light); border-radius: var(--radius-lg); border: 1px solid var(--border-subtle);">
        <h3>Interested in Hosting an Employee Financial Wellness Session?</h3>
        <p class="mb-3 text-muted">Submit an enquiry to discuss customized corporate workshops or virtual webinars for your organization.</p>
        <a href="consultation.html" class="btn btn-primary">Enquire About Corporate Sessions</a>
      </div>
    </div>
  </section>
"""
    }

    # 8. disclosures.html
    pages["disclosures.html"] = {
        "title": "Regulatory & Business Disclosures | Mutual Fund Advisory",
        "meta_desc": "Read comprehensive regulatory disclosures: Model A RIA vs Model B MFD vs Model C Investor Education, fee structures, conflicts of interest, and safeguards.",
        "active_nav": "legal",
        "breadcrumbs": [("Regulatory Disclosures", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Statutory Governance</span>
      <h1 class="page-banner-title">Regulatory &amp; Business Disclosures</h1>
      <p class="page-banner-desc">Essential information regarding business models, regulatory frameworks, conflict-of-interest policies, and demonstration notices.</p>
    </div>
  </section>

  <section class="section">
    <div class="container container-narrow">
      <div class="mb-5">
        {make_placeholder("mutual-fund-regulatory-governance-sebi.jpg", "Regulatory Compliance & Legal Framework Visual", "16-9", "A symbolic depiction of financial regulatory standards, legal codes, and SEBI compliance architecture.", "1200x675", "Regulatory Compliance")}
      </div>

      <div class="model-selector-box mb-5">
        <span class="model-tag" style="background: #E2E8F0; color: #1E293B;">DEVELOPMENT &amp; OPERATIONAL CONFIGURATION GUIDE</span>
        <h3 style="margin-bottom: 0.75rem;">Mandatory Business Model Selection</h3>
        <p style="font-size: 0.95rem; margin-bottom: 1rem;">
          In accordance with SEBI (Investment Advisers) Regulations, 2013 and SEBI (Mutual Funds) Regulations, 1996, financial services businesses in India must strictly segregate fee-based Investment Advisory from commission-earning Mutual Fund Distribution. A single legal entity cannot combine both under ambiguous claims.
        </p>

        <div style="display: flex; flex-direction: column; gap: 1rem; font-size: 0.9rem;">
          <div style="background: white; padding: 1rem; border-radius: var(--radius-sm); border-left: 4px solid #4F46E5;">
            <strong>Model A — SEBI-Registered Investment Adviser (RIA):</strong><br>
            If the real operator is a licensed RIA, the platform must display verified SEBI registration numbers, fee schedules, conflict-of-interest policies, and execute formal advisory agreements. No distribution commissions may be received.
          </div>
          <div style="background: white; padding: 1rem; border-radius: var(--radius-sm); border-left: 4px solid #16A34A;">
            <strong>Model B — AMFI-Registered Mutual Fund Distributor (MFD):</strong><br>
            If the real operator is an MFD, the platform must display valid AMFI ARN and EUIN credentials, disclose commission bands from AMCs, distribute Regular plans, and refrain from using regulated 'advisory' or 'independent advice' terminology.
          </div>
          <div style="background: white; padding: 1rem; border-radius: var(--radius-sm); border-left: 4px solid #D97706;">
            <strong>Model C — Investor Education Platform (Current Default):</strong><br>
            If the operator is neither, the platform operates purely as an investor literacy and education resource. No personalized investment advice is offered, no financial transactions are executed, and no client funds are handled.
          </div>
        </div>
      </div>

      <div style="font-size: 0.95rem; line-height: 1.7; color: var(--text-body);">
        <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">Demonstration Website Status</h3>
        <p>
          This website is a generic demonstration platform created to showcase wealth management user experience, responsive web architecture, and Indian mutual fund education. It does not possess SEBI registration, AMFI ARN, or NISM credentials. All logos, branding, calculations, and team profiles are illustrative placeholders.
        </p>

        <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">Statutory Risk Disclosure</h3>
        <p>
          Mutual fund investments are subject to market risks. Read all scheme-related documents carefully before investing. Mutual funds do not offer guaranteed returns or capital protection. Net Asset Values fluctuate daily based on capital market movements.
        </p>

        <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">Grievance Redressal Mechanism</h3>
        <p>
          In a live operational deployment under Indian law, investors have access to structured escalation pathways, including the AMC grievance cell, registrar desks (CAMS/KFintech), the SEBI Complaints Redress System (SCORES), and the SEBI SMART ODR online dispute resolution portal.
        </p>
      </div>
    </div>
  </section>
"""
    }

    # 9. privacy-policy.html
    pages["privacy-policy.html"] = {
        "title": "Privacy Policy | Mutual Fund Advisory Data Protection",
        "meta_desc": "Our commitment to data privacy: zero personal data retention on demo forms, strict non-collection of PAN/Aadhaar, and cookie transparency.",
        "active_nav": "legal",
        "breadcrumbs": [("Privacy Policy", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Data Protection</span>
      <h1 class="page-banner-title">Privacy Policy</h1>
      <p class="page-banner-desc">How we handle visitor data, maintain zero-storage principles for demonstration forms, and protect user privacy.</p>
    </div>
  </section>

  <section class="section">
    <div class="container container-narrow" style="font-size: 0.95rem; line-height: 1.7; color: var(--text-body);">
      <div class="mb-5">
        {make_placeholder("mutual-fund-data-privacy-security.jpg", "Data Privacy & Information Security Shield", "16-9", "A conceptual visualization representing data privacy, encryption safeguards, and investor confidentiality.", "1200x675", "Privacy Shield")}
      </div>

      <h3 style="color: var(--navy-primary); margin-bottom: 0.75rem;">1. Demonstration Platform Status</h3>
      <p>
        Mutual Fund Advisory operates as an educational demonstration website. We do not store, process, monetize, or transmit visitor personal data to any external server or third-party marketing network.
      </p>

      <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">2. Non-Collection of Sensitive Financial Information</h3>
      <p>
        We strictly forbid and prevent the collection of sensitive financial credentials. Our forms will never ask for:
      </p>
      <ul style="margin: 0.75rem 0 1rem 1.5rem; list-style: disc;">
        <li>Permanent Account Number (PAN)</li>
        <li>Aadhaar numbers or biometric details</li>
        <li>Bank account numbers, IFSC codes, or UPI PINs</li>
        <li>Demat account credentials or mutual fund login passwords</li>
        <li>Credit or debit card details</li>
      </ul>

      <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">3. Interactive Tools &amp; Calculators</h3>
      <p>
        All financial calculators (SIP Calculator, Lump Sum Calculator, Goal Planning Calculator, Risk Questionnaire) execute client-side using Vanilla JavaScript within your local browser sandbox. Numerical inputs are discarded upon refreshing or closing the browser tab.
      </p>

      <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">4. Cookies &amp; Local Storage</h3>
      <p>
        This website uses only essential session cookies necessary for interface navigation. We do not employ third-party advertising cookies, cross-site trackers, or invasive analytics pixels.
      </p>
    </div>
  </section>
"""
    }

    # 10. terms-and-conditions.html
    pages["terms-and-conditions.html"] = {
        "title": "Terms and Conditions | Mutual Fund Advisory Website Use",
        "meta_desc": "Read the terms governing the use of the Mutual Fund Advisory demonstration website: educational use, disclaimer of warranties, and intellectual property.",
        "active_nav": "legal",
        "breadcrumbs": [("Terms & Conditions", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Legal Terms</span>
      <h1 class="page-banner-title">Terms and Conditions of Use</h1>
      <p class="page-banner-desc">Please read these terms and conditions carefully before utilizing this educational demonstration platform.</p>
    </div>
  </section>

  <section class="section">
    <div class="container container-narrow" style="font-size: 0.95rem; line-height: 1.7; color: var(--text-body);">
      <div class="mb-5">
        {make_placeholder("mutual-fund-legal-terms-compliance.jpg", "Website Legal Terms & Compliance Overview", "16-9", "A conceptual illustration of legal terms, intellectual property protections, and terms of service documentation.", "1200x675", "Legal Terms")}
      </div>

      <h3 style="color: var(--navy-primary); margin-bottom: 0.75rem;">1. Acceptance of Terms</h3>
      <p>
        By accessing or browsing this website, you acknowledge that you have read, understood, and agreed to be bound by these terms. If you do not agree with any portion of these terms, please discontinue use of this website.
      </p>

      <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">2. Educational Purpose Only</h3>
      <p>
        All content, articles, tables, interactive calculators, and illustrations published on this website are provided strictly for investor awareness and educational purposes. Nothing on this website constitutes personalized financial, investment, tax, or legal advice.
      </p>

      <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">3. Disclaimer of Warranties</h3>
      <p>
        This website and its calculation models are provided on an "as is" and "as available" basis without warranties of any kind, whether express or implied. We do not warrant that mathematical estimates will match actual mutual fund performance.
      </p>

      <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">4. Limitation of Liability</h3>
      <p>
        Under no circumstances shall the operators, authors, or web developers be liable for any direct, indirect, incidental, or consequential damages arising from the use of or inability to use this demonstration website.
      </p>
    </div>
  </section>
"""
    }

    # 11. disclaimer.html
    pages["disclaimer.html"] = {
        "title": "Statutory Disclaimer | Mutual Fund Advisory Risk Warning",
        "meta_desc": "Mandatory statutory disclaimer: Mutual fund investments are subject to market risks. Read all scheme-related documents carefully. Demonstration notice.",
        "active_nav": "legal",
        "breadcrumbs": [("Disclaimer", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Legal Notice</span>
      <h1 class="page-banner-title">Statutory Disclaimer &amp; Risk Warning</h1>
      <p class="page-banner-desc">Mandatory regulatory disclosure regarding mutual fund market risks, non-guarantee of returns, and demonstration limits.</p>
    </div>
  </section>

  <section class="section">
    <div class="container container-narrow" style="font-size: 0.95rem; line-height: 1.7; color: var(--text-body);">
      <div class="mb-5">
        {make_placeholder("mutual-fund-statutory-risk-disclaimer.jpg", "Statutory Risk Disclaimer & Regulatory Notice", "16-9", "A formal regulatory notice layout displaying SEBI statutory risk warnings and investor caution guidelines.", "1200x675", "Statutory Notice")}
      </div>

      <div class="regulatory-banner mb-5" style="border-left: 4px solid var(--danger);">
        <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <div>
          <strong>MANDATORY STATUTORY NOTICE:</strong><br>
          Mutual fund investments are subject to market risks. Read all scheme-related documents carefully. This is a demonstration website and does not offer investment advice or execute mutual fund transactions.
        </div>
      </div>

      <h3 style="color: var(--navy-primary); margin-bottom: 0.75rem;">No Guarantee of Returns or Capital Protection</h3>
      <p>
        Mutual funds are market-linked instruments. Past performance of any mutual fund scheme, index, or asset class is not indicative of future returns. Mutual funds do not guarantee capital protection or fixed yields.
      </p>

      <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">Demonstration Platform Boundaries</h3>
      <p>
        This website is a generic demonstration platform created to illustrate wealth management website design, responsive frontend architecture, and mutual fund educational concepts. It does not represent an actual operating business, SEBI Registered Investment Adviser, or AMFI Registered Mutual Fund Distributor.
      </p>

      <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">Consult a Registered Professional</h3>
      <p>
        Before committing capital to any mutual fund scheme, investors must evaluate their own financial position, risk capacity, and time horizon, and consult a qualified, registered financial adviser.
      </p>
    </div>
  </section>
"""
    }

    # 12. cookie-policy.html
    pages["cookie-policy.html"] = {
        "title": "Cookie Policy | Mutual Fund Advisory Browser Usage",
        "meta_desc": "Understand our cookie policy: essential session cookies only, zero third-party advertising tracking, and browser configuration guidelines.",
        "active_nav": "legal",
        "breadcrumbs": [("Cookie Policy", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Browser Privacy</span>
      <h1 class="page-banner-title">Cookie Policy</h1>
      <p class="page-banner-desc">Learn about how cookies and browser storage are utilized on this educational demonstration website.</p>
    </div>
  </section>

  <section class="section">
    <div class="container container-narrow" style="font-size: 0.95rem; line-height: 1.7; color: var(--text-body);">
      <div class="mb-5">
        {make_placeholder("mutual-fund-cookie-privacy-browser.jpg", "Browser Cookie Settings & Privacy Controls", "16-9", "An illustration of browser settings toggles for session cookies, caching, and privacy permissions.", "1200x675", "Cookie Preferences")}
      </div>

      <h3 style="color: var(--navy-primary); margin-bottom: 0.75rem;">1. What Are Cookies?</h3>
      <p>
        Cookies are small text files stored on your computer or mobile device when you visit a website. They are widely used to make websites work efficiently and provide seamless navigation.
      </p>

      <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">2. How We Use Cookies</h3>
      <p>
        This demonstration website uses only strictly necessary session cookies that allow you to navigate pages and maintain interface settings (such as mobile drawer states). We do not store tracking cookies or behavioral profile cookies.
      </p>

      <h3 style="color: var(--navy-primary); margin-top: 2rem; margin-bottom: 0.75rem;">3. Managing Your Cookie Preferences</h3>
      <p>
        You can control or disable cookies at any time through your browser settings (Chrome, Safari, Firefox, Edge). Disabling all cookies will not impair your ability to view and read the educational content on this website.
      </p>
    </div>
  </section>
"""
    }

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
    build_investor_and_legal_pages()
