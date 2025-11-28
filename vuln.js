function runUserCode(input) {
    // CodeQL will flag this: js/dangerous-eval
    return eval(input);
}

runUserCode("process.exit()");
