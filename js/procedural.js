/**
 * Cambridge English Skills Test Simulator
 * Legacy Compatibility Shim for CESTProcedural (v7)
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

  const shim = {
    hashString: (s) => (getEngine().hashString ? getEngine().hashString(s) : 0),
    createPrng: (s) => (getEngine().createPrng ? getEngine().createPrng(s) : () => 0),
    assembleTest: (b, s) => (getEngine().assembleTest ? getEngine().assembleTest(b, s) : null)
  };

  if (typeof window !== 'undefined') {
    window.CESTProcedural = window.CEST || shim;
  }
  if (typeof global !== 'undefined') {
    global.CESTProcedural = global.CEST || shim;
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = shim;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
