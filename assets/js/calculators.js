/**
 * MUTUAL FUND ADVISORY
 * Financial Calculators & Risk Profiling (Vanilla JS)
 */

// Helper to format Indian Currency
function formatINR(val) {
  if (isNaN(val) || val === null) return '₹0';
  return '₹' + Math.round(val).toLocaleString('en-IN');
}

document.addEventListener('DOMContentLoaded', () => {

  // ==========================================
  // 1. SIP CALCULATOR
  // ==========================================
  const sipAmountRange = document.getElementById('sipAmountRange');
  const sipAmountInput = document.getElementById('sipAmountInput');
  const sipRateRange = document.getElementById('sipRateRange');
  const sipRateInput = document.getElementById('sipRateInput');
  const sipYearsRange = document.getElementById('sipYearsRange');
  const sipYearsInput = document.getElementById('sipYearsInput');

  const sipInvestedDisplay = document.getElementById('sipInvestedDisplay');
  const sipGainDisplay = document.getElementById('sipGainDisplay');
  const sipTotalDisplay = document.getElementById('sipTotalDisplay');
  const sipBarInvested = document.getElementById('sipBarInvested');
  const sipBarGain = document.getElementById('sipBarGain');
  const sipResetBtn = document.getElementById('sipResetBtn');

  function calculateSIP() {
    if (!sipAmountRange) return;

    const monthlyInvestment = parseFloat(sipAmountRange.value) || 5000;
    const annualRate = parseFloat(sipRateRange.value) || 12;
    const years = parseFloat(sipYearsRange.value) || 10;

    const totalMonths = years * 12;
    const monthlyRate = (annualRate / 100) / 12;

    // SIP Future Value formula: M = P * [ (1 + i)^n - 1 ] * (1 + i) / i
    const investedAmount = monthlyInvestment * totalMonths;
    let futureValue = 0;
    if (monthlyRate > 0) {
      futureValue = monthlyInvestment * ((Math.pow(1 + monthlyRate, totalMonths) - 1) / monthlyRate) * (1 + monthlyRate);
    } else {
      futureValue = investedAmount;
    }
    const estimatedGain = futureValue - investedAmount;

    if (sipInvestedDisplay) sipInvestedDisplay.textContent = formatINR(investedAmount);
    if (sipGainDisplay) sipGainDisplay.textContent = formatINR(estimatedGain);
    if (sipTotalDisplay) sipTotalDisplay.textContent = formatINR(futureValue);

    if (sipBarInvested && sipBarGain && futureValue > 0) {
      const investedPct = (investedAmount / futureValue) * 100;
      const gainPct = (estimatedGain / futureValue) * 100;
      sipBarInvested.style.width = `${investedPct}%`;
      sipBarGain.style.width = `${gainPct}%`;
    }
  }

  function syncInputs(rangeEl, inputEl, callback) {
    if (!rangeEl || !inputEl) return;
    rangeEl.addEventListener('input', () => {
      inputEl.value = rangeEl.value;
      callback();
    });
    inputEl.addEventListener('input', () => {
      let val = parseFloat(inputEl.value);
      if (!isNaN(val)) {
        rangeEl.value = val;
        callback();
      }
    });
  }

  if (sipAmountRange && sipAmountInput) {
    syncInputs(sipAmountRange, sipAmountInput, calculateSIP);
    syncInputs(sipRateRange, sipRateInput, calculateSIP);
    syncInputs(sipYearsRange, sipYearsInput, calculateSIP);
    calculateSIP();

    if (sipResetBtn) {
      sipResetBtn.addEventListener('click', () => {
        sipAmountRange.value = 5000;
        sipAmountInput.value = 5000;
        sipRateRange.value = 12;
        sipRateInput.value = 12;
        sipYearsRange.value = 10;
        sipYearsInput.value = 10;
        calculateSIP();
      });
    }
  }

  // ==========================================
  // 2. LUMP SUM CALCULATOR
  // ==========================================
  const lumpAmountRange = document.getElementById('lumpAmountRange');
  const lumpAmountInput = document.getElementById('lumpAmountInput');
  const lumpRateRange = document.getElementById('lumpRateRange');
  const lumpRateInput = document.getElementById('lumpRateInput');
  const lumpYearsRange = document.getElementById('lumpYearsRange');
  const lumpYearsInput = document.getElementById('lumpYearsInput');

  const lumpInvestedDisplay = document.getElementById('lumpInvestedDisplay');
  const lumpGainDisplay = document.getElementById('lumpGainDisplay');
  const lumpTotalDisplay = document.getElementById('lumpTotalDisplay');
  const lumpBarInvested = document.getElementById('lumpBarInvested');
  const lumpBarGain = document.getElementById('lumpBarGain');
  const lumpResetBtn = document.getElementById('lumpResetBtn');

  function calculateLumpSum() {
    if (!lumpAmountRange) return;

    const principal = parseFloat(lumpAmountRange.value) || 100000;
    const rate = parseFloat(lumpRateRange.value) || 11;
    const years = parseFloat(lumpYearsRange.value) || 5;

    // Future Value = P * (1 + r/100)^t
    const futureValue = principal * Math.pow(1 + (rate / 100), years);
    const estimatedGain = futureValue - principal;

    if (lumpInvestedDisplay) lumpInvestedDisplay.textContent = formatINR(principal);
    if (lumpGainDisplay) lumpGainDisplay.textContent = formatINR(estimatedGain);
    if (lumpTotalDisplay) lumpTotalDisplay.textContent = formatINR(futureValue);

    if (lumpBarInvested && lumpBarGain && futureValue > 0) {
      const investedPct = (principal / futureValue) * 100;
      const gainPct = (estimatedGain / futureValue) * 100;
      lumpBarInvested.style.width = `${investedPct}%`;
      lumpBarGain.style.width = `${gainPct}%`;
    }
  }

  if (lumpAmountRange && lumpAmountInput) {
    syncInputs(lumpAmountRange, lumpAmountInput, calculateLumpSum);
    syncInputs(lumpRateRange, lumpRateInput, calculateLumpSum);
    syncInputs(lumpYearsRange, lumpYearsInput, calculateLumpSum);
    calculateLumpSum();

    if (lumpResetBtn) {
      lumpResetBtn.addEventListener('click', () => {
        lumpAmountRange.value = 100000;
        lumpAmountInput.value = 100000;
        lumpRateRange.value = 11;
        lumpRateInput.value = 11;
        lumpYearsRange.value = 5;
        lumpYearsInput.value = 5;
        calculateLumpSum();
      });
    }
  }

  // ==========================================
  // 3. GOAL PLANNING CALCULATOR
  // ==========================================
  const goalTargetRange = document.getElementById('goalTargetRange');
  const goalTargetInput = document.getElementById('goalTargetInput');
  const goalYearsRange = document.getElementById('goalYearsRange');
  const goalYearsInput = document.getElementById('goalYearsInput');
  const goalSavingsRange = document.getElementById('goalSavingsRange');
  const goalSavingsInput = document.getElementById('goalSavingsInput');
  const goalRateRange = document.getElementById('goalRateRange');
  const goalRateInput = document.getElementById('goalRateInput');

  const goalTargetDisplay = document.getElementById('goalTargetDisplay');
  const goalCurrentFvDisplay = document.getElementById('goalCurrentFvDisplay');
  const goalShortfallDisplay = document.getElementById('goalShortfallDisplay');
  const goalMonthlyReqDisplay = document.getElementById('goalMonthlyReqDisplay');
  const goalResetBtn = document.getElementById('goalResetBtn');

  function calculateGoal() {
    if (!goalTargetRange) return;

    const targetAmount = parseFloat(goalTargetRange.value) || 5000000;
    const years = parseFloat(goalYearsRange.value) || 10;
    const currentSavings = parseFloat(goalSavingsRange.value) || 200000;
    const annualRate = parseFloat(goalRateRange.value) || 12;

    const totalMonths = years * 12;
    const monthlyRate = (annualRate / 100) / 12;

    // FV of current lump sum savings
    const currentSavingsFV = currentSavings * Math.pow(1 + (annualRate / 100), years);
    const shortfall = Math.max(0, targetAmount - currentSavingsFV);

    // Monthly SIP needed to bridge shortfall: P = M / [ ((1+i)^n - 1) / i * (1+i) ]
    let monthlySIPNeeded = 0;
    if (shortfall > 0 && monthlyRate > 0) {
      const sipFactor = ((Math.pow(1 + monthlyRate, totalMonths) - 1) / monthlyRate) * (1 + monthlyRate);
      monthlySIPNeeded = shortfall / sipFactor;
    }

    if (goalTargetDisplay) goalTargetDisplay.textContent = formatINR(targetAmount);
    if (goalCurrentFvDisplay) goalCurrentFvDisplay.textContent = formatINR(currentSavingsFV);
    if (goalShortfallDisplay) goalShortfallDisplay.textContent = formatINR(shortfall);
    if (goalMonthlyReqDisplay) goalMonthlyReqDisplay.textContent = formatINR(monthlySIPNeeded);
  }

  if (goalTargetRange && goalTargetInput) {
    syncInputs(goalTargetRange, goalTargetInput, calculateGoal);
    syncInputs(goalYearsRange, goalYearsInput, calculateGoal);
    syncInputs(goalSavingsRange, goalSavingsInput, calculateGoal);
    syncInputs(goalRateRange, goalRateInput, calculateGoal);
    calculateGoal();

    if (goalResetBtn) {
      goalResetBtn.addEventListener('click', () => {
        goalTargetRange.value = 5000000;
        goalTargetInput.value = 5000000;
        goalYearsRange.value = 10;
        goalYearsInput.value = 10;
        goalSavingsRange.value = 200000;
        goalSavingsInput.value = 200000;
        goalRateRange.value = 12;
        goalRateInput.value = 12;
        calculateGoal();
      });
    }
  }

  // ==========================================
  // 4. DEMO RISK EDUCATION QUESTIONNAIRE
  // ==========================================
  const riskForm = document.getElementById('riskQuestionnaireForm');
  const riskResultBox = document.getElementById('riskResultBox');
  const riskCategoryTitle = document.getElementById('riskCategoryTitle');
  const riskCategoryDesc = document.getElementById('riskCategoryDesc');
  const riskResetBtn = document.getElementById('riskResetBtn');

  if (riskForm && riskResultBox) {
    riskForm.addEventListener('submit', (e) => {
      e.preventDefault();

      let totalScore = 0;
      let answeredCount = 0;
      const questions = ['q1', 'q2', 'q3', 'q4', 'q5'];

      questions.forEach(q => {
        const selected = riskForm.querySelector(`input[name="${q}"]:checked`);
        if (selected) {
          totalScore += parseInt(selected.value, 10);
          answeredCount++;
        }
      });

      if (answeredCount < questions.length) {
        alert('Please answer all 5 questions to view the illustrative risk education profile.');
        return;
      }

      let category = '';
      let description = '';

      if (totalScore <= 8) {
        category = 'Lower Risk Tolerance (Conservative Perspective)';
        description = 'Your illustrative answers suggest a focus on capital preservation, steady liquidity, and a sensitivity to short-term volatility. In general financial education, conservative perspectives often lean toward debt, liquid, and conservative hybrid instruments.';
      } else if (totalScore <= 14) {
        category = 'Moderate Risk Tolerance (Balanced Perspective)';
        description = 'Your illustrative answers reflect comfort with moderate fluctuations in pursuit of inflation-beating long-term growth. In educational asset allocation, balanced frameworks typically blend equity and fixed-income assets to balance growth and stability.';
      } else {
        category = 'Higher Risk Tolerance (Growth-Oriented Perspective)';
        description = 'Your illustrative answers indicate a long investment horizon and resilience towards temporary market corrections to target wealth creation. In educational concepts, growth-oriented perspectives often allocate predominantly to diversified equity mutual funds.';
      }

      if (riskCategoryTitle) riskCategoryTitle.textContent = category;
      if (riskCategoryDesc) riskCategoryDesc.textContent = description;

      riskResultBox.classList.add('active');
      riskResultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });

    if (riskResetBtn) {
      riskResetBtn.addEventListener('click', () => {
        riskForm.reset();
        riskResultBox.classList.remove('active');
      });
    }
  }
});
