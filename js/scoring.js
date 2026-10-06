/**
 * Cambridge English Skills Test Simulator
 * Legacy Compatibility Shim for Scoring Engine (v7)
 * Runtime scripts are consolidated into js/engine.js.
 */
(function (root) {
  'use strict';
  const getEngine = () => {
    if (typeof window !== 'undefined' && window.CEST) return window.CEST;
    if (typeof global !== 'undefined' && global.CEST) return global.CEST;
    if (typeof require !== 'undefined') {
      try { return require('./engine.js'); } catch (e) {}
    }
    return {};
  };

  function gradeExam(testData, answersDict) {
    const engine = getEngine();
    return engine.gradeExam ? engine.gradeExam(testData, answersDict) : null;
  }

  function generateReportText(report) {
    const engine = getEngine();
    return engine.generateReportText ? engine.generateReportText(report) : "";
  }

  if (typeof window !== 'undefined') {
    window.gradeExam = gradeExam;
    window.generateReportText = generateReportText;
  }
  if (typeof global !== 'undefined') {
    global.gradeExam = gradeExam;
    global.generateReportText = generateReportText;
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { gradeExam, generateReportText };
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
