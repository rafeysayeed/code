/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let init = n;
    return function() {
        const ret = init;
        init += 1;
        return ret;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */