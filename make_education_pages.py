"""
Generate 12 Investment Strategy & Education Pages with Dedicated Placeholders
"""

from templates import render_html_page, make_placeholder

def build_education_pages():
    pages = {}

    # 1. sip-investment.html
    pages["sip-investment.html"] = {
        "title": "SIP Investment | Systematic Investment Plan Concepts",
        "meta_desc": "Master Systematic Investment Plans (SIP) in India: rupee-cost averaging, compounding, market volatility absorption, discipline, and execution flexibility.",
        "active_nav": "planning",
        "breadcrumbs": [("Investment Planning", "financial-planning.html"), ("SIP Investment", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Disciplined Wealth Creation</span>
      <h1 class="page-banner-title">Demystifying Systematic Investment Plans (SIP)</h1>
      <p class="page-banner-desc">Learn how regular, automated contributions harness rupee-cost averaging and compounding across market cycles.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Core Mechanics</span>
          <h2 class="section-title">What is a Systematic Investment Plan?</h2>
          <p>
            A Systematic Investment Plan (SIP) is an investment route offered by mutual funds allowing investors to contribute a fixed monetary sum (e.g., ₹1,000, ₹5,000, or ₹25,000) at predefined intervals (monthly, quarterly, or weekly) into a chosen mutual fund scheme.
          </p>
          <p>
            Rather than attempting to guess short-term market tops and bottoms, an SIP automates disciplined habit formation. On the designated debit date, the fixed installment purchases units at the prevailing day's Net Asset Value (NAV).
          </p>
          <div class="regulatory-banner">
            <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <div>
              <strong>Important Risk Safeguard:</strong> An SIP does NOT eliminate market risk, nor does it guarantee profits. An SIP in an equity mutual fund will experience temporary paper losses whenever broad equity markets undergo downward corrections.
            </div>
          </div>
        </div>

        <div>
          {make_placeholder("mutual-fund-sip-compounding-timeline.jpg", "Systematic Investment Plan Timeline & Averaging", "4-3", "An illustrative timeline showcasing monthly contributions navigating market peaks and valleys.", "1000x750", "SIP Timeline Visual")}
        </div>
      </div>

      <!-- Rupee-Cost Averaging Conceptual Table -->
      <div class="section-header">
        <span class="section-tag tag-gold">Mathematical Principle</span>
        <h2 class="section-title">How Rupee-Cost Averaging Works</h2>
        <p class="section-subtitle">Illustrative example of a fixed ₹5,000 monthly SIP during fluctuating market NAV levels.</p>
      </div>

      <div class="comparison-table-wrapper mb-5">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>Month</th>
              <th>Fixed Monthly Outflow</th>
              <th>Prevailing Scheme NAV</th>
              <th>Units Allotted</th>
              <th>Key Behavioral Takeaway</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Month 1 (Market High)</strong></td>
              <td>₹5,000</td>
              <td>₹100</td>
              <td>50.00 Units</td>
              <td>Market is elevated; fewer units purchased at higher valuation.</td>
            </tr>
            <tr>
              <td><strong>Month 2 (Market Correction)</strong></td>
              <td>₹5,000</td>
              <td>₹80</td>
              <td>62.50 Units</td>
              <td>Market drops 20%; fixed capital automatically buys MORE units.</td>
            </tr>
            <tr>
              <td><strong>Month 3 (Market Trough)</strong></td>
              <td>₹5,000</td>
              <td>₹62.50</td>
              <td>80.00 Units</td>
              <td>Market hits bottom; investor accumulates maximum units.</td>
            </tr>
            <tr>
              <td><strong>Month 4 (Market Recovery)</strong></td>
              <td>₹5,000</td>
              <td>₹90</td>
              <td>55.55 Units</td>
              <td>Market recovers partially; accumulated units compound in value.</td>
            </tr>
            <tr style="background: var(--bg-light); font-weight: bold;">
              <td><strong>Total / Average</strong></td>
              <td>₹20,000 Invested</td>
              <td>Avg NAV: ₹83.12</td>
              <td>248.05 Total Units</td>
              <td>Portfolio Value at Month 4 NAV (₹90) = ₹22,324.50</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card-grid-3 mb-5">
        <div class="feature-card">
          <h4 class="feature-card-title">Flexibility &amp; Control</h4>
          <p class="feature-card-text">Investors can pause, increase (Top-Up SIP), or terminate an SIP at any time without financial penalties from the mutual fund.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">Compounding Horizon</h4>
          <p class="feature-card-text">Returns generated in earlier years begin generating their own returns, causing portfolio growth curves to steepen sharply after 7-10 years.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">Eliminating Market Timing</h4>
          <p class="feature-card-text">Removes the anxiety of deciding whether today is the 'right time' to enter the market, fostering disciplined long-term consistency.</p>
        </div>
      </div>

      <div class="p-4 text-center" style="background: var(--bg-light); border-radius: var(--radius-lg); border: 1px solid var(--border-subtle);">
        <h3>Calculate Your Illustrative SIP Returns</h3>
        <p class="mb-3">Explore our educational SIP calculator with custom return and horizon assumptions.</p>
        <a href="sip-calculator.html" class="btn btn-primary">Open Interactive SIP Calculator</a>
      </div>
    </div>
  </section>
"""
    }

    # 2. lump-sum-investment.html
    pages["lump-sum-investment.html"] = {
        "title": "Lump Sum Investment | Timing, Horizon & STP Strategies",
        "meta_desc": "Understand lump sum mutual fund investing in India: one-time capital deployment, market timing risks, Systematic Transfer Plans (STP), and horizon matching.",
        "active_nav": "planning",
        "breadcrumbs": [("Investment Planning", "financial-planning.html"), ("Lump Sum Investment", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Capital Deployment</span>
      <h1 class="page-banner-title">Lump Sum Mutual Fund Investing</h1>
      <p class="page-banner-desc">Examine the advantages, psychological challenges, and staggered deployment alternatives for lump sum capital.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Deployment Dynamics</span>
          <h2 class="section-title">What is Lump Sum Investing?</h2>
          <p>
            Lump sum investing refers to depositing a single large capital amount into a mutual fund scheme in one transaction (such as an annual bonus, business dividend, property sale proceeds, or retirement gratuity).
          </p>
          <p>
            When deploying a lump sum into debt or liquid funds, timing risk is negligible because underlying bond prices have low volatility. However, deploying a large lump sum into equity mutual funds requires careful horizon evaluation.
          </p>
          <div class="regulatory-banner">
            <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <div>
              <strong>Objective Perspective:</strong> Lump sum investing is neither universally superior nor inferior to SIP investing. Its suitability depends entirely on prevailing market valuations, investor risk capacity, and time horizon.
            </div>
          </div>
        </div>

        <div>
          {make_placeholder("mutual-fund-lump-sum-deployment.jpg", "Lump Sum vs Staggered Deployment Analysis", "4-3", "A portfolio manager comparing lump sum entry trajectories against staggered Systematic Transfer Plans (STP).", "1000x750", "Lump Sum Visual")}
        </div>
      </div>

      <!-- The STP Strategy -->
      <div class="section-header">
        <span class="section-tag tag-gold">Prudent Alternative</span>
        <h2 class="section-title">The Systematic Transfer Plan (STP) Route</h2>
        <p class="section-subtitle">How cautious investors mitigate entry-timing risk when deploying large lump sums.</p>
      </div>

      <div class="card-grid-3 mb-5">
        <div class="feature-card">
          <div class="feature-card-icon">1</div>
          <h4 class="feature-card-title">Initial Parking</h4>
          <p class="feature-card-text">Park the entire lump sum capital into a low-volatility Liquid or Ultra Short Duration debt fund of the target AMC.</p>
        </div>
        <div class="feature-card">
          <div class="feature-card-icon">2</div>
          <h4 class="feature-card-title">Automated Tranche Transfer</h4>
          <p class="feature-card-text">Instruct the AMC to systematically transfer a fixed portion (e.g. 1/12th each month) into the target equity scheme.</p>
        </div>
        <div class="feature-card">
          <div class="feature-card-icon">3</div>
          <h4 class="feature-card-title">Averaging &amp; Accrual</h4>
          <p class="feature-card-text">The parked balance earns short-term debt accrual returns while equity tranches benefit from rupee-cost averaging over 6 to 18 months.</p>
        </div>
      </div>

      <div class="p-4 text-center" style="background: var(--bg-light); border-radius: var(--radius-lg); border: 1px solid var(--border-subtle);">
        <h3>Calculate Illustrative Lump Sum Compounding</h3>
        <p class="mb-3">Explore our educational Lump Sum Calculator with customizable rate and timeframe parameters.</p>
        <a href="lumpsum-calculator.html" class="btn btn-primary">Open Lump Sum Calculator</a>
      </div>
    </div>
  </section>
"""
    }

    # 3. direct-vs-regular.html
    pages["direct-vs-regular.html"] = {
        "title": "Direct vs Regular Plans | Mutual Fund Expense Differences",
        "meta_desc": "Compare Direct and Regular mutual fund plans in India: distributor commissions, Total Expense Ratio (TER), net NAV compounding, and investor responsibilities.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Direct vs Regular Plans", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Cost &amp; Intermediary Transparency</span>
      <h1 class="page-banner-title">Direct vs Regular Mutual Fund Plans</h1>
      <p class="page-banner-desc">Understand how scheme expense ratios differ, what services intermediaries provide, and how to evaluate which route matches your needs.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Regulatory Context</span>
          <h2 class="section-title">SEBI's Dual-Plan Framework</h2>
          <p>
            Effective January 1, 2013, the Securities and Exchange Board of India (SEBI) mandated that every mutual fund scheme must offer two separate plans: a <strong>Direct Plan</strong> and a <strong>Regular Plan</strong>.
          </p>
          <p>
            Both plans share the exact same underlying portfolio of stocks or bonds and are managed by the exact same fund manager. The only difference lies in how they are distributed and the associated operating expense ratio.
          </p>
          <div class="regulatory-banner">
            <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <div>
              <strong>Objective Perspective:</strong> Direct plans are not automatically the optimal choice for every investor, nor are regular plans inherently unsuitable. Investors who lack time, market knowledge, or emotional discipline often benefit from professional distributor guidance that outweighs the expense differential.
            </div>
          </div>
        </div>

        <div>
          {make_placeholder("mutual-fund-direct-vs-regular-comparison.jpg", "Direct vs Regular Plan Evaluation Dialogue", "4-3", "An investor discussing fee structures and distribution advisory models with a certified planner.", "1000x750", "Direct vs Regular Consultation")}
        </div>
      </div>

      <!-- Comparison Table -->
      <div class="section-header">
        <span class="section-tag tag-gold">Side-by-Side Analysis</span>
        <h2 class="section-title">Direct Plan vs Regular Plan Breakdown</h2>
      </div>

      <div class="comparison-table-wrapper mb-5">
        <table class="comparison-table">
          <thead>
            <tr>
              <th style="width: 25%;">Feature</th>
              <th style="width: 37.5%;">Direct Plan</th>
              <th style="width: 37.5%;">Regular Plan</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Intermediary Involvement</strong></td>
              <td>Zero intermediaries. Investor purchases directly from the AMC or via an execution-only platform (EOP).</td>
              <td>Transacted through an AMFI-registered Mutual Fund Distributor (MFD), bank, or financial broker.</td>
            </tr>
            <tr>
              <td><strong>Distribution Commission</strong></td>
              <td>Zero commission paid out of the fund.</td>
              <td>Trail commission is paid out of the scheme assets to the distributor for the lifetime of the investment.</td>
            </tr>
            <tr>
              <td><strong>Total Expense Ratio (TER)</strong></td>
              <td>Lower (typically 0.5% to 1.25% lower in equity funds).</td>
              <td>Higher due to embedded ongoing distribution commissions.</td>
            </tr>
            <tr>
              <td><strong>Net Asset Value (NAV)</strong></td>
              <td>Higher NAV due to lower ongoing daily fee deductions.</td>
              <td>Slightly lower NAV compared to the direct plan of the exact same scheme.</td>
            </tr>
            <tr>
              <td><strong>Investor Responsibilities</strong></td>
              <td>Investor must conduct independent research, scheme selection, periodic portfolio rebalancing, and operational paperwork.</td>
              <td>Distributor assists with scheme recommendations, KYC verification, portfolio tracking, and operational queries.</td>
            </tr>
            <tr>
              <td><strong>Ideal For</strong></td>
              <td>Self-directed, knowledgeable investors comfortable executing transactions independently.</td>
              <td>Investors seeking hand-holding, ongoing operational support, and assistance with behavioral discipline.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
"""
    }

    # 4. growth-vs-idcw.html
    pages["growth-vs-idcw.html"] = {
        "title": "Growth vs IDCW | Mutual Fund Option Comparison",
        "meta_desc": "Understand Growth versus IDCW (Income Distribution cum Capital Withdrawal) options in mutual funds: NAV impact, compounding, and taxation.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Growth vs IDCW", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Distribution Mechanics</span>
      <h1 class="page-banner-title">Growth vs IDCW (Dividend) Options</h1>
      <p class="page-banner-desc">Learn how these two scheme options handle generated profits and what that means for your long-term compounding and taxation.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Terminology Shift</span>
          <h2 class="section-title">What is IDCW?</h2>
          <p>
            SEBI renamed the traditional 'Dividend Option' to <strong>Income Distribution cum Capital Withdrawal (IDCW)</strong> to clarify a fundamental reality: mutual fund payouts are not guaranteed interest or extra bonus money; they are simply a distribution of your own accumulated capital and profits.
          </p>
          <p>
            Whenever a mutual fund declares an IDCW payout, the scheme's Net Asset Value (NAV) immediately falls by the exact per-unit distribution amount declared.
          </p>
          <div class="regulatory-banner">
            <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <div>
              <strong>Important Clarification:</strong> IDCW payouts are entirely at the discretion of the AMC trustees and are never guaranteed. They should never be treated as a fixed monthly income substitute.
            </div>
          </div>
        </div>

        <div>
          {make_placeholder("mutual-fund-growth-vs-idcw-distribution.jpg", "NAV Impact of IDCW Distribution", "4-3", "Educational graph showing how NAV automatically adjusts downward following an IDCW payout.", "1000x750", "IDCW NAV Graph")}
        </div>
      </div>

      <!-- Comparison Cards -->
      <div class="card-grid-2 mb-5">
        <div class="feature-card" style="border-top: 4px solid var(--green-primary);">
          <h3 class="feature-card-title">Growth Option</h3>
          <p class="feature-card-text">All profits, capital gains, and dividends earned by the portfolio are automatically retained and reinvested into the scheme.</p>
          <ul style="font-size: 0.9rem; color: var(--text-body); display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
            <li><strong>NAV Trajectory:</strong> Grows continuously with underlying asset values.</li>
            <li><strong>Compounding Effect:</strong> Maximum compounding efficiency because zero capital is leaked out.</li>
            <li><strong>Tax Event:</strong> Tax is payable ONLY when you redeem units.</li>
            <li><strong>Suitability:</strong> Long-term wealth creation where periodic cash flows are not required.</li>
          </ul>
        </div>

        <div class="feature-card" style="border-top: 4px solid var(--navy-primary);">
          <h3 class="feature-card-title">IDCW Option</h3>
          <p class="feature-card-text">A portion of accumulated profits and capital is periodically paid out to unitholders at the AMC's discretion.</p>
          <ul style="font-size: 0.9rem; color: var(--text-body); display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
            <li><strong>NAV Trajectory:</strong> Drops by the distribution amount on the ex-distribution date.</li>
            <li><strong>Compounding Effect:</strong> Compounding is curtailed because distributed funds exit the scheme.</li>
            <li><strong>Tax Event:</strong> Payouts are added to your taxable income and taxed at your applicable slab rate.</li>
            <li><strong>Suitability:</strong> Investors seeking occasional cash distributions who understand the tax implications.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 5. nav-explained.html
    pages["nav-explained.html"] = {
        "title": "Understanding NAV | Net Asset Value Calculation & Myths",
        "meta_desc": "Learn how mutual fund Net Asset Value (NAV) is calculated, how units work, and debunk the persistent myth that low NAV funds are cheaper.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Understanding NAV", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Valuation Science</span>
      <h1 class="page-banner-title">Understanding Net Asset Value (NAV)</h1>
      <p class="page-banner-desc">Explore how mutual fund units are priced, how daily portfolio accounting operates, and why NAV is not like a stock price.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Definition &amp; Formula</span>
          <h2 class="section-title">What is Net Asset Value?</h2>
          <p>
            Net Asset Value (NAV) represents the market value per unit of a mutual fund scheme. It is calculated by summing the total market value of all underlying shares, bonds, cash, and accrued interest held by the fund, subtracting permissible operating expenses, and dividing by the total number of outstanding units.
          </p>
          <div style="background: var(--bg-light); padding: 1.25rem; border-radius: var(--radius-md); border-left: 4px solid var(--green-primary); margin: 1.5rem 0;">
            <p style="font-family: monospace; font-size: 0.95rem; margin: 0; color: var(--navy-primary);">
              NAV = (Market Value of Investments + Receivables - Liabilities &amp; Expenses) / Total Outstanding Units
            </p>
          </div>
          <p>
            Under SEBI guidelines, the NAV of every scheme is calculated and published at the close of every business day after stock and bond markets shut down.
          </p>
        </div>

        <div>
          {make_placeholder("mutual-fund-nav-calculation-accounting.jpg", "Daily NAV Calculation & Portfolio Accounting", "4-3", "An accounting flow showing stock market closing prices feeding into AMC net asset calculations.", "1000x750", "NAV Accounting Visual")}
        </div>
      </div>

      <!-- The Big NAV Myth -->
      <div class="section-header">
        <span class="section-tag tag-gold">Common Fallacy</span>
        <h2 class="section-title">The "Low NAV = Cheap" Myth Debunked</h2>
        <p class="section-subtitle">Why a ₹10 NAV fund has identical return potential to a ₹1,000 NAV fund holding the same assets.</p>
      </div>

      <div class="comparison-table-wrapper mb-5">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>Metric</th>
              <th>Scheme A (New Scheme / NFO)</th>
              <th>Scheme B (Established Scheme)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Invested Capital</strong></td>
              <td>₹1,00,000</td>
              <td>₹1,00,000</td>
            </tr>
            <tr>
              <td><strong>Current NAV</strong></td>
              <td>₹10</td>
              <td>₹1,000</td>
            </tr>
            <tr>
              <td><strong>Units Allotted</strong></td>
              <td>10,000 Units</td>
              <td>100 Units</td>
            </tr>
            <tr>
              <td><strong>Hypothetical Portfolio Gain (+15%)</strong></td>
              <td>New NAV = ₹11.50</td>
              <td>New NAV = ₹1,150.00</td>
            </tr>
            <tr style="background: #F0FDF4; font-weight: bold; color: var(--green-deep);">
              <td><strong>Final Portfolio Value</strong></td>
              <td>10,000 x ₹11.50 = ₹1,15,000 (+15%)</td>
              <td>100 x ₹1,150 = ₹1,15,000 (+15%)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
"""
    }

    # 6. expense-ratio.html
    pages["expense-ratio.html"] = {
        "title": "Expense Ratio | Total Expense Ratio (TER) Impact in India",
        "meta_desc": "Understand Total Expense Ratio (TER) in mutual funds: management fees, administrative expenses, SEBI statutory caps, and long-term compounding impact.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Expense Ratio", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Fee Transparency</span>
      <h1 class="page-banner-title">Understanding Total Expense Ratio (TER)</h1>
      <p class="page-banner-desc">Explore the operating costs of managing mutual fund schemes, SEBI statutory caps, and how expenses affect terminal portfolio values.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Cost Components</span>
          <h2 class="section-title">What Makes Up the Expense Ratio?</h2>
          <p>
            The Total Expense Ratio (TER) represents the annual percentage of scheme assets deducted on a daily pro-rata basis to cover the operational, administrative, and management costs of running a mutual fund.
          </p>
          <ul style="display: flex; flex-direction: column; gap: 0.75rem; margin: 1.25rem 0;">
            <li><strong>Investment Management Fees:</strong> Remuneration for the fund managers, equity analysts, and research teams.</li>
            <li><strong>Registrar &amp; Transfer Fees (RTA):</strong> Recordkeeping and servicing managed by CAMS or KFintech.</li>
            <li><strong>Custodian &amp; Audit Fees:</strong> Safeguarding securities and independent chartered accounting verification.</li>
            <li><strong>Distribution Commissions (Regular Plans only):</strong> Ongoing trail compensation paid to mutual fund distributors.</li>
          </ul>
        </div>

        <div>
          {make_placeholder("mutual-fund-expense-ratio-ter-breakdown.jpg", "TER Breakdown & Compounding Cost Drag", "4-3", "An analytical chart demonstrating the 20-year terminal divergence between a 0.5% TER and 1.8% TER.", "1000x750", "Expense Drag Visual")}
        </div>
      </div>

      <!-- SEBI Slab Structure -->
      <div class="section-header">
        <span class="section-tag tag-gold">Regulatory Protection</span>
        <h2 class="section-title">SEBI Regulated Expense Slabs</h2>
        <p class="section-subtitle">SEBI mandates that as an equity scheme's Assets Under Management (AUM) grow, the permissible TER cap must decline.</p>
      </div>

      <div class="comparison-table-wrapper mb-5">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>Scheme AUM Slab (Equity Schemes)</th>
              <th>Maximum Permissible Base TER Cap</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>On the first ₹500 Crores of AUM</td>
              <td>2.25%</td>
            </tr>
            <tr>
              <td>On the next ₹250 Crores of AUM</td>
              <td>2.00%</td>
            </tr>
            <tr>
              <td>On the next ₹1,250 Crores of AUM</td>
              <td>1.75%</td>
            </tr>
            <tr>
              <td>On the next ₹3,000 Crores of AUM</td>
              <td>1.60%</td>
            </tr>
            <tr>
              <td>On the next ₹5,000 Crores of AUM</td>
              <td>1.50%</td>
            </tr>
            <tr>
              <td>On AUM exceeding ₹50,000 Crores</td>
              <td>Reduction of 0.05% for every increase of ₹5,000 Crores</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
"""
    }

    # 7. exit-load.html
    pages["exit-load.html"] = {
        "title": "Understanding Exit Load | Mutual Fund Redemption Charges",
        "meta_desc": "Learn about exit loads in mutual funds: why they are levied, holding period thresholds, FIFO redemption principles, and schemes with zero exit load.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Understanding Exit Load", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Liquidity &amp; Redemption</span>
      <h1 class="page-banner-title">Understanding Mutual Fund Exit Load</h1>
      <p class="page-banner-desc">Examine how exit loads operate, why they exist to protect long-term investors, and how holding periods are calculated.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Purpose &amp; Structure</span>
          <h2 class="section-title">Why Do Schemes Levy an Exit Load?</h2>
          <p>
            An exit load is a fee or penalty charged by an AMC when an investor redeems or switches units before a specified holding duration has elapsed.
          </p>
          <p>
            Its primary purpose is to discourage short-term trading and speculative churning. Frequent inflows and outflows force fund managers to maintain excessive cash buffers or liquidate securities prematurely, hurting long-term unitholders.
          </p>
          <div class="regulatory-banner">
            <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <div>
              <strong>Where Does the Fee Go?</strong> Under SEBI regulations, exit load fees collected by an AMC are credited back into the scheme's assets (after deducting GST), directly benefiting the remaining long-term investors.
            </div>
          </div>
        </div>

        <div>
          {make_placeholder("mutual-fund-exit-load-holding-structure.jpg", "Exit Load Calculation & Holding Period Timeline", "4-3", "An illustrative calendar diagram explaining FIFO (First In First Out) redemption tracking for SIP tranches.", "1000x750", "Exit Load Timeline")}
        </div>
      </div>

      <!-- Common Exit Load Rules -->
      <div class="section-header">
        <span class="section-tag tag-gold">Category Standards</span>
        <h2 class="section-title">Typical Exit Load Structures Across Categories</h2>
      </div>

      <div class="card-grid-3 mb-5">
        <div class="feature-card">
          <h4 class="feature-card-title">Equity Mutual Funds</h4>
          <p class="feature-card-text">Typically 1.00% if redeemed within 365 days from the date of unit allotment. Zero exit load for redemptions made after 1 year.</p>
        </div>

        <div class="feature-card">
          <h4 class="feature-card-title">Liquid Funds (Graded)</h4>
          <p class="feature-card-text">Graded scale starting at 0.0070% on Day 1, decreasing daily to 0.0045% on Day 6, and dropping to 0.0000% from Day 7 onwards.</p>
        </div>

        <div class="feature-card">
          <h4 class="feature-card-title">Overnight &amp; ELSS Funds</h4>
          <p class="feature-card-text">Overnight funds have 0% exit load from Day 1. ELSS funds have zero exit load after their mandatory 3-year statutory lock-in.</p>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 8. riskometer.html
    pages["riskometer.html"] = {
        "title": "Understanding Riskometer | SEBI Mutual Fund Risk Gauge",
        "meta_desc": "Explore the SEBI Riskometer: 6 risk levels from Low to Very High, dynamic monthly calculations, credit risk, duration, and liquidity parameters.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Understanding Riskometer", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Risk Disclosure</span>
      <h1 class="page-banner-title">The SEBI Mutual Fund Riskometer</h1>
      <p class="page-banner-desc">Learn how to read the six-tiered visual risk gauge mandated on all scheme documents and marketing materials.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Objective Evaluation</span>
          <h2 class="section-title">How the Riskometer is Calculated</h2>
          <p>
            SEBI introduced a dynamic, formula-driven Riskometer that evaluates actual portfolio holdings on the last day of each calendar month, rather than relying on subjective marketing descriptions.
          </p>
          <p>
            For debt schemes, the calculation assigns objective mathematical scores across three parameters: <strong>Credit Risk</strong> (issuer rating), <strong>Interest Rate Risk</strong> (Macaulay duration), and <strong>Liquidity Risk</strong> (trading depth).
          </p>
          <p>
            For equity schemes, scores are derived from <strong>Market Capitalization</strong> (large, mid, small), <strong>Volatility</strong>, and <strong>Impact Cost</strong> (ease of selling underlying shares without price disruption).
          </p>
        </div>

        <div>
          {make_placeholder("mutual-fund-sebi-riskometer-gauge.jpg", "SEBI Riskometer 6-Tiered Gauge Display", "4-3", "A high-fidelity depiction of the semicircular Riskometer needle spanning Low to Very High.", "1000x750", "Riskometer Visual")}
        </div>
      </div>

      <!-- The 6 Tiers -->
      <div class="section-header">
        <span class="section-tag tag-gold">The 6 Tiers</span>
        <h2 class="section-title">Riskometer Classification Spectrum</h2>
      </div>

      <div class="card-grid-3 mb-5">
        <div class="feature-card" style="border-top: 4px solid #16A34A;">
          <h4 class="feature-card-title">1. Low Risk</h4>
          <p class="feature-card-text">Overnight funds, ultra-short sovereign paper. Minimal capital volatility and maximum credit safety.</p>
        </div>
        <div class="feature-card" style="border-top: 4px solid #84CC16;">
          <h4 class="feature-card-title">2. Low to Moderate Risk</h4>
          <p class="feature-card-text">Liquid funds and money market schemes holding top-tier bank CDs and treasury bills.</p>
        </div>
        <div class="feature-card" style="border-top: 4px solid #EAB308;">
          <h4 class="feature-card-title">3. Moderate Risk</h4>
          <p class="feature-card-text">Short duration debt funds, corporate bond schemes, and conservative hybrid funds.</p>
        </div>
        <div class="feature-card" style="border-top: 4px solid #F97316;">
          <h4 class="feature-card-title">4. Moderately High Risk</h4>
          <p class="feature-card-text">Balanced advantage funds, dynamic asset allocation schemes, and long-term gilt portfolios.</p>
        </div>
        <div class="feature-card" style="border-top: 4px solid #EF4444;">
          <h4 class="feature-card-title">5. High Risk</h4>
          <p class="feature-card-text">Diversified large-cap equity funds, flexi-cap schemes, and aggressive hybrid funds.</p>
        </div>
        <div class="feature-card" style="border-top: 4px solid #991B1B;">
          <h4 class="feature-card-title">6. Very High Risk</h4>
          <p class="feature-card-text">Mid-cap, small-cap, sectoral/thematic, and international equity mutual funds.</p>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 9. diversification.html
    pages["diversification.html"] = {
        "title": "Investment Diversification | Asset Class & Sector Strategy",
        "meta_desc": "Understand mutual fund diversification in India: asset classes, market cap tiers, sector spread, and avoiding unproductive portfolio duplication.",
        "active_nav": "planning",
        "breadcrumbs": [("Investment Planning", "financial-planning.html"), ("Diversification", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Risk Mitigation</span>
      <h1 class="page-banner-title">The Art &amp; Science of Diversification</h1>
      <p class="page-banner-desc">Learn how to build a diversified portfolio across asset classes, sectors, and cap sizes without falling into over-diversification.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Core Principle</span>
          <h2 class="section-title">The Only Free Lunch in Finance</h2>
          <p>
            Nobel laureate Harry Markowitz famously described diversification as the only free lunch in finance. By combining assets whose returns do not move in perfect tandem (imperfect or negative correlation), an investor can reduce overall portfolio volatility without sacrificing long-term expected returns.
          </p>
          <p>
            A well-constructed portfolio achieves diversification on three levels:
          </p>
          <ul style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
            <li><strong>1. Asset Class Diversification:</strong> Spreading wealth across Equities, Fixed Income, and Gold.</li>
            <li><strong>2. Market Cap Diversification:</strong> Blending Large, Mid, and Small Cap company exposure.</li>
            <li><strong>3. Sector &amp; Geographic Diversification:</strong> Ensuring no single economic sector accounts for an outsized portion of assets.</li>
          </ul>
        </div>

        <div>
          {make_placeholder("mutual-fund-portfolio-diversification-matrix.jpg", "Correlation Heatmap Across Asset Classes", "4-3", "An educational correlation matrix showing historical relationships between Indian equities, debt, and gold.", "1000x750", "Diversification Matrix")}
        </div>
      </div>

      <!-- Over-diversification Trap -->
      <div class="section-header">
        <span class="section-tag tag-gold">Common Pitfall</span>
        <h2 class="section-title">The Trap of Over-Diversification</h2>
        <p class="section-subtitle">Why owning 25 mutual funds rarely performs better than owning 4 to 6 well-chosen schemes.</p>
      </div>

      <div class="card-grid-3 mb-5">
        <div class="feature-card">
          <h4 class="feature-card-title">Portfolio Dilution</h4>
          <p class="feature-card-text">Holding dozens of schemes turns your active portfolio into an expensive proxy for the index, while charging active management fees.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">Stock Overlap</h4>
          <p class="feature-card-text">Five large-cap schemes from different AMCs will likely hold 70-80% of the exact same underlying top 30 companies.</p>
        </div>
        <div class="feature-card">
          <h4 class="feature-card-title">Administrative Friction</h4>
          <p class="feature-card-text">Managing capital gains statements, tax filings, and performance tracking becomes needlessly complex and unmanageable.</p>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 10. compounding.html
    pages["compounding.html"] = {
        "title": "Power of Compounding | Mathematical Wealth Accumulation",
        "meta_desc": "Explore the power of compounding in mutual fund investing: compounding formula, exponential growth curves, and the critical role of time horizon.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Power of Compounding", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Mathematical Mechanics</span>
      <h1 class="page-banner-title">The Power of Compounding in Mutual Funds</h1>
      <p class="page-banner-desc">Understand the mathematical snowball effect where your reinvested earnings generate their own earnings over multi-decade cycles.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Exponential Growth</span>
          <h2 class="section-title">Time is the Greatest Multiplier</h2>
          <p>
            In simple interest, returns are paid only on your original principal. In compound growth, your earnings are reinvested back into the fund to generate additional earnings in subsequent periods.
          </p>
          <p>
            In the early years of an investment, the growth curve appears slow and almost linear. However, as the accumulated gains overtake the original principal invested, the growth curve transitions from linear to exponential.
          </p>
          <div class="regulatory-banner">
            <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <div>
              <strong>Non-Guarantee Notice:</strong> While the mathematical principle of compounding is indisputable, mutual fund returns do not compound at a fixed, guaranteed annual rate. Returns fluctuate unevenly year to year.
            </div>
          </div>
        </div>

        <div>
          {make_placeholder("mutual-fund-power-of-compounding-curve.jpg", "Exponential Compounding Hockey Stick Curve", "4-3", "An illustrative growth chart comparing linear savings against exponential compounding over 30 years.", "1000x750", "Compounding Curve")}
        </div>
      </div>

      <!-- Compounding Milestone Table -->
      <div class="section-header">
        <span class="section-tag tag-gold">Illustrative Model</span>
        <h2 class="section-title">The Compounding Acceleration Timeline</h2>
        <p class="section-subtitle">Hypothetical illustration of a fixed ₹10,000 monthly SIP assuming an illustrative 12% annual compounding rate.</p>
      </div>

      <div class="comparison-table-wrapper mb-5">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>Milestone (Years)</th>
              <th>Total Invested Capital</th>
              <th>Illustrative Estimated Value</th>
              <th>Estimated Capital Gain</th>
              <th>Gain-to-Investment Ratio</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Year 5</strong></td>
              <td>₹6,00,000</td>
              <td>₹8,24,864</td>
              <td>₹2,24,864</td>
              <td>Gains = 37% of invested capital</td>
            </tr>
            <tr>
              <td><strong>Year 10</strong></td>
              <td>₹12,00,000</td>
              <td>₹23,23,391</td>
              <td>₹11,23,391</td>
              <td>Gains = 93% of invested capital</td>
            </tr>
            <tr>
              <td><strong>Year 15</strong></td>
              <td>₹18,00,000</td>
              <td>₹50,45,760</td>
              <td>₹32,45,760</td>
              <td>Gains = 180% of invested capital</td>
            </tr>
            <tr>
              <td><strong>Year 20</strong></td>
              <td>₹24,00,000</td>
              <td>₹99,91,479</td>
              <td>₹75,91,479</td>
              <td>Gains = 316% of invested capital</td>
            </tr>
            <tr style="background: #F0FDF4; font-weight: bold; color: var(--green-deep);">
              <td><strong>Year 25</strong></td>
              <td>₹30,00,000</td>
              <td>₹1,89,76,351</td>
              <td>₹1,59,76,351</td>
              <td>Gains = 532% of invested capital</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
"""
    }

    # 11. investment-taxation.html
    pages["investment-taxation.html"] = {
        "title": "Mutual Fund Taxation | Capital Gains Tax Rules in India",
        "meta_desc": "Understand capital gains taxation on Indian mutual funds: holding periods, equity vs specified funds, STCG vs LTCG, and verification instructions.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Mutual Fund Taxation", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Tax Literacy</span>
      <h1 class="page-banner-title">Mutual Fund Capital Gains Taxation in India</h1>
      <p class="page-banner-desc">Learn how the Income Tax Act treats capital gains across different mutual fund categories and holding durations.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="regulatory-banner mb-5" style="border-left: 4px solid var(--danger);">
        <svg class="regulatory-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <div>
          <strong>IMPORTANT TAX DISCLOSURE &amp; VERIFICATION INSTRUCTION:</strong><br>
          Tax laws are subject to frequent legislative amendments (such as Finance Acts and Union Budgets). The concepts described on this educational website reflect general frameworks. Tax treatment depends on fund classification, holding period, transaction date, applicable law, and investor tax residency. <strong>Always verify current tax rates and provisions with a qualified chartered accountant or tax consultant prior to making investment decisions.</strong>
        </div>
      </div>

      <div class="card-grid-2 mb-5" style="align-items: center;">
        <div>
          <span class="section-tag">Statutory Framework</span>
          <h2 class="section-title">Capital Gains Tax Structure</h2>
          <p>
            Mutual fund taxation is governed by the provisions of the Income Tax Act, 1961. The tax incidence occurs only when units are redeemed or switched out of a scheme.
          </p>
          <p>
            The applicable rate depends primarily on the equity exposure of the fund and the duration for which the units were held prior to sale.
          </p>
        </div>
        <div>
          {make_placeholder("mutual-fund-capital-gains-tax-rules.jpg", "Indian Mutual Fund Capital Gains Tax Rules", "4-3", "An infographic displaying holding period thresholds, STCG, and LTCG tax slabs.", "1000x750", "Tax Architecture")}
        </div>
      </div>

      <div class="card-grid-2 mb-5">
        <div class="feature-card">
          <h3 class="feature-card-title">1. Equity-Oriented Mutual Funds</h3>
          <p class="feature-card-text">Schemes where minimum 65% of total proceeds are invested in equity shares of domestic listed companies.</p>
          <ul style="font-size: 0.9rem; color: var(--text-body); display: flex; flex-direction: column; gap: 0.65rem; margin-top: 1rem;">
            <li><strong>Short-Term Capital Gains (STCG):</strong> Applicable when units are held for 12 months or less before redemption.</li>
            <li><strong>Long-Term Capital Gains (LTCG):</strong> Applicable when units are held for more than 12 months before redemption.</li>
            <li><strong>Statutory Exemption:</strong> Under applicable law, LTCG up to a statutory threshold per financial year is exempt from tax, with gains beyond taxed at the statutory LTCG rate.</li>
          </ul>
        </div>

        <div class="feature-card">
          <h3 class="feature-card-title">2. Non-Equity / Specified Debt Mutual Funds</h3>
          <p class="feature-card-text">Schemes that invest not more than 35% in equity shares (pure debt funds, liquid funds, conservative debt portfolios).</p>
          <ul style="font-size: 0.9rem; color: var(--text-body); display: flex; flex-direction: column; gap: 0.65rem; margin-top: 1rem;">
            <li><strong>Tax Treatment:</strong> Under current legislative amendments for specified mutual funds acquired on or after April 1, 2023, capital gains are treated as short-term capital gains regardless of the holding period.</li>
            <li><strong>Applicable Tax Rate:</strong> Gains are added to the investor's taxable income and taxed at their marginal income tax slab rates.</li>
          </ul>
        </div>
      </div>

      <div class="card-grid-2 mb-5">
        <div class="feature-card">
          <h4 class="feature-card-title">Securities Transaction Tax (STT)</h4>
          <p class="feature-card-text">STT is levied on equity mutual fund redemptions (typically 0.001%) at the time of sale. Debt funds do not attract STT.</p>
        </div>

        <div class="feature-card">
          <h4 class="feature-card-title">Tax Deducted at Source (TDS)</h4>
          <p class="feature-card-text">For resident individual investors, no TDS is deducted on capital gains from redemptions. However, TDS applies to IDCW payouts exceeding statutory thresholds.</p>
        </div>
      </div>
    </div>
  </section>
"""
    }

    # 12. investment-for-beginners.html
    pages["investment-for-beginners.html"] = {
        "title": "Beginner's Investment Guide | 7 Foundational Steps",
        "meta_desc": "Start your mutual fund journey with confidence: KYC verification, goal setting, risk tolerance, scheme selection, and SIP automation in India.",
        "active_nav": "resources",
        "breadcrumbs": [("Investor Resources", "investor-resources.html"), ("Beginner's Guide", "")],
        "content": f"""
  <section class="page-banner">
    <div class="container page-banner-content">
      <span class="section-tag tag-navy">Foundational Roadmap</span>
      <h1 class="page-banner-title">The Complete Beginner's Investment Guide</h1>
      <p class="page-banner-desc">Seven essential steps every new investor should complete before allocating their first rupee to mutual funds.</p>
    </div>
  </section>

  <section class="section">
    <div class="container container-narrow">
      <div class="mb-5">
        {make_placeholder("mutual-fund-beginner-investor-guide.jpg", "Beginner Investor Roadmap & Milestone Guide", "16-9", "A young Indian investor reviewing financial goals, emergency funds, and SIP automation steps.", "1200x675", "Beginner Roadmap")}
      </div>

      <div style="display: flex; flex-direction: column; gap: 2rem;">
        <div class="feature-card" style="border-left: 5px solid var(--navy-primary);">
          <h4>Step 1: Build an Emergency Cash Buffer First</h4>
          <p>Before investing in volatile equity mutual funds, establish an emergency cushion equal to 6 months of living expenses in a liquid fund or bank savings account to prevent panic liquidations during personal emergencies.</p>
        </div>

        <div class="feature-card" style="border-left: 5px solid var(--green-primary);">
          <h4>Step 2: Obtain Adequate Life &amp; Health Insurance</h4>
          <p>Protect your family with pure term insurance and comprehensive health cover. Mutual fund investments should never be used as a substitute for insurance protection.</p>
        </div>

        <div class="feature-card" style="border-left: 5px solid var(--gold-accent);">
          <h4>Step 3: Complete Your Centralized KYC (CKYC)</h4>
          <p>KYC is mandatory under SEBI regulations. Ensure your PAN is linked with your Aadhaar, bank account, and mobile number through any SEBI-registered KRA (KYC Registration Agency).</p>
        </div>

        <div class="feature-card" style="border-left: 5px solid #0284C7);">
          <h4>Step 4: Define Time Horizons for Each Life Goal</h4>
          <p>Never invest aimlessly. Segregate your goals into short-term (&lt;3 years &rarr; debt funds), medium-term (3-5 years &rarr; hybrid funds), and long-term (5+ years &rarr; equity funds).</p>
        </div>

        <div class="feature-card" style="border-left: 5px solid var(--green-deep);">
          <h4>Step 5: Start with Simple Broad-Market Index Funds or Flexi-Caps</h4>
          <p>As a novice investor, avoid complex sectoral bets or exotic foreign schemes. Build your foundational core using a Nifty 50 Index Fund or a well-diversified Flexi Cap scheme.</p>
        </div>

        <div class="feature-card" style="border-left: 5px solid var(--navy-surface);">
          <h4>Step 6: Automate Your Monthly Investments via SIP</h4>
          <p>Set up an automated monthly SIP scheduled 1 or 2 days after your salary date. Automating your investments builds discipline and removes emotional hesitation.</p>
        </div>

        <div class="feature-card" style="border-left: 5px solid #D97706);">
          <h4>Step 7: Resist Checking Your Portfolio Daily</h4>
          <p>Market NAVs fluctuate every evening. Obsessive tracking triggers emotional panic during market corrections. Review your portfolio systematically once or twice a year, not every day.</p>
        </div>
      </div>
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
    build_education_pages()
