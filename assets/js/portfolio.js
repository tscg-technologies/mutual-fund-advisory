/**
 * MUTUAL FUND ADVISORY
 * Interactive Portfolio Allocation & Educational Visualization
 */

document.addEventListener('DOMContentLoaded', () => {
  const profileSelector = document.getElementById('portfolioProfileSelect');
  const allocEquityBar = document.getElementById('allocEquityBar');
  const allocDebtBar = document.getElementById('allocDebtBar');
  const allocHybridBar = document.getElementById('allocHybridBar');
  const allocCashBar = document.getElementById('allocCashBar');

  const allocEquityVal = document.getElementById('allocEquityVal');
  const allocDebtVal = document.getElementById('allocDebtVal');
  const allocHybridVal = document.getElementById('allocHybridVal');
  const allocCashVal = document.getElementById('allocCashVal');

  const profileProfiles = {
    conservative: {
      equity: 20,
      debt: 60,
      hybrid: 10,
      cash: 10,
      desc: 'Illustrative framework emphasizing capital preservation and steady income with lower volatility exposure.'
    },
    moderate: {
      equity: 50,
      debt: 35,
      hybrid: 10,
      cash: 5,
      desc: 'Illustrative framework balancing growth and fixed-income stability over a 5 to 7-year time horizon.'
    },
    aggressive: {
      equity: 75,
      debt: 15,
      hybrid: 5,
      cash: 5,
      desc: 'Illustrative framework prioritizing long-term capital compounding across equity categories with capacity for market drawdowns.'
    }
  };

  function updateAllocation(profileKey) {
    const data = profileProfiles[profileKey];
    if (!data) return;

    if (allocEquityBar) allocEquityBar.style.width = `${data.equity}%`;
    if (allocDebtBar) allocDebtBar.style.width = `${data.debt}%`;
    if (allocHybridBar) allocHybridBar.style.width = `${data.hybrid}%`;
    if (allocCashBar) allocCashBar.style.width = `${data.cash}%`;

    if (allocEquityVal) allocEquityVal.textContent = `${data.equity}%`;
    if (allocDebtVal) allocDebtVal.textContent = `${data.debt}%`;
    if (allocHybridVal) allocHybridVal.textContent = `${data.hybrid}%`;
    if (allocCashVal) allocCashVal.textContent = `${data.cash}%`;

    const descEl = document.getElementById('portfolioProfileDesc');
    if (descEl) descEl.textContent = data.desc;
  }

  if (profileSelector) {
    profileSelector.addEventListener('change', (e) => {
      updateAllocation(e.target.value);
    });
    updateAllocation('moderate');
  }
});
